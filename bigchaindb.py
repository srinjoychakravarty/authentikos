import json
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

def connect_db():
    bdb_root_url = 'http://localhost:9984'
    bdb = BigchainDB(bdb_root_url)
    return bdb

def generate_key():
    alice = generate_keypair()
    return alice

def write_json(filename, bdb, alice):
    with open(filename) as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            news_asset = {'data': {'news_agency_asset': {key: value}}}
            print(news_asset)
            metadata_checksum = {'checksum': key}
            prepared_creation_tx = bdb.transactions.prepare(operation = 'CREATE', signers = alice.public_key, asset = news_asset, metadata = metadata_checksum)
            fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx, private_keys = alice.private_key)
            bdb.transactions.send_commit(fulfilled_creation_tx)

def find_asset(search_term):
    retrieved_object = bdb.assets.get(search = search_term)
    return retrieved_object

if __name__ == '__main__':

    connection_choice = input("\nWelcome to Authentikos! \nWhat would you like to connect BigChainDB? [yes (y) | no (n)] \n")
    print(connection_choice)
    if (connection_choice == "yes" or "y"):
        print("\nconnecting to bigchaindb...")
        bdb = connect_db()
        print(f"\nConnection Successful! \n {bdb}")
        keypair_choice = input("\nWuld you like to gemerate a BigChainDB keypair? [yes (y) | no (n)]\n")
        if (keypair_choice == "yes" or "y"):
            print("\ngenerating keys...")
            alice = generate_key()
            print(f"\nYour public key is: {alice.public_key}")
            print(f"\nYour private key is: {alice.private_key}")
        else:
            print("\nThanks for using Authentikos...bye now!")   
    else:
        print("\nThanks for using Authentikos...bye now!") 
        
    # filename = 'authentikos.txt'
    # write_json(filename, bdb, alice)
    # retrieved_obj = find_asset()

