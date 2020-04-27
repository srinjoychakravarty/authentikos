from collections import namedtuple
from cryptography import x509
from cryptography.x509.oid import NameOID
from OpenSSL import SSL
from socket import socket
from tinydb import TinyDB, Query, where
import concurrent.futures, dateparser, datetime, hashlib, idna, json, os

def get_certificate(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket()
    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD) # most compatible
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE
    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()
    return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)

def get_alt_names(cert):
    try:
        ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        return ext.value.get_values_for_type(x509.DNSName)
    except x509.ExtensionNotFound:
        return None

def get_common_name(cert):
    try:
        names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None

def get_issuer(cert):
    try:
        names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None

def print_basic_info(hostinfo):
    expiry = hostinfo.cert.not_valid_after
    cert_dict = {'peer_name': hostinfo.peername, 'common_name': get_common_name(hostinfo.cert), 'san': get_alt_names(hostinfo.cert), 'issuer': get_issuer(hostinfo.cert), 'not_before': hostinfo.cert.not_valid_before, 'not_after': expiry, 'valid_cert': (expiry > datetime.datetime.now()) }
    return cert_dict

def check_it_out(hostname, port):
    hostinfo = get_certificate(hostname, port)
    ssl_info = print_basic_info(hostinfo)
    return ssl_info

if __name__ == '__main__':
    HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    db = TinyDB(location + "/trustdb.json")
    news_agencies = []
    outer_dict = {}
    for entity in db.search(where('news_agency')):
        current_agency = entity.get('news_agency')
        print(current_agency)
        ratings_dict = dict(entity)
        checksum = ratings_dict.get('checksum')
        del ratings_dict['checksum']    
        try:
            ssl_details = check_it_out(current_agency, 443)
            inner_dict = {checksum: {'ratings_dict': ratings_dict, 'ssl_details': ssl_details}}
            outer_dict.update(inner_dict)
        except:
            inner_dict = {checksum: {'ratings_dict': ratings_dict}}
            outer_dict.update(inner_dict)
            pass
    print(outer_dict)
    print(len(outer_dict.keys()))
    with open('authentikos.txt', 'w') as fp:
        json.dump(outer_dict, fp, indent=4, sort_keys = True, default = str)
