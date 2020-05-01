from web3 import Web3, HTTPProvider
from web3.auto import w3
import contract_abi, json, time

with open('authentikos.txt') as json_file:
    data = json.load(json_file)
    checksums = [data.keys()]
    for hash in checksums:
        w3.eth.account.create()

def populate_checksums(contract, wallet_address, wallet_private_key):
    hex_list = []
    with open('authentikos.txt') as json_file:
        data = json.load(json_file)
        key_list = list(data.keys())
        for checksum_key in key_list:
            nonce = w3.eth.getTransactionCount(wallet_address)
            print(nonce)
            eth_addr = str(w3.eth.account.create().address)
            txn_dict = contract.functions.setAgency(checksum_key, eth_addr).buildTransaction({'chainId': 4, 'gas': 90000, 'gasPrice': w3.toWei('40', 'gwei'), 'nonce': nonce})
            signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = wallet_private_key)
            txn_hash = (w3.eth.sendRawTransaction(signed_txn.rawTransaction)).hex()
            print(txn_hash)
            time.sleep(13)

if __name__ == '__main__':
    infura_key = "6c7e9aed2af146138cc7ef1986d9b558"
    https_rinkeby = "https://rinkeby.infura.io/v3/" + infura_key
    w3 = Web3(HTTPProvider(https_rinkeby))
    smart_contract_address = "0xC3737aF68f5471a2607C996525993a8E9AF1862F"
    contract = w3.eth.contract(address = smart_contract_address, abi = contract_abi.abi)
    wallet_address = "0xC7AC16DD7b42EeEc39Ee088a8702883e073D782e"
    priv_key = "6065a6bd9ccc0d11fd2ffb2111e68519df26b8294489cdc45fd748dd4a4f094b"
    populate_checksums(contract, wallet_address, priv_key)
   