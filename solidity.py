from web3 import Web3, HTTPProvider
import binascii, contract_abi, json, pprint, subprocess, sys, time

wallet_address = '0xC7AC16DD7b42EeEc39Ee088a8702883e073D782e'
wallet_private_key = '6065a6bd9ccc0d11fd2ffb2111e68519df26b8294489cdc45fd748dd4a4f094b'
contract_address = '0xEEC42723E36b3cB362D9cB49b8Cd2a111454FF03'
infura_key = "6c7e9aed2af146138cc7ef1986d9b558"
https_rinkeby = "https://rinkeby.infura.io/v3/" + infura_key
websockets_rinkeby = "wss://rinkeby.infura.io/ws/v3/" + infura_key
w3 = Web3(HTTPProvider(https_rinkeby))
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)
all_functions = contract.all_functions()
# print(all_functions)
# print(contract.functions.countAgencies().call())
# print(contract.functions.contractOwner().call())
print(contract.functions.getAgencies().call())

nonce = w3.eth.getTransactionCount(wallet_address)

agency3 = ("ndtv.com", "0x32804f2B543f4EbEce478D9847d8446650840128")
# agency4 = ("cnbc.com", "0x6aED3Ca3C77a75Dc8d36ce9c306eA2A7aef576e0")
# setAgency(string _address, address _ethIdentity)

txn_dict = contract.functions.setAgency(agency3[0], agency3[1]).buildTransaction({
    'chainId': 4,
    'gas': 140000,
    'gasPrice': w3.toWei('40', 'gwei'),
    'nonce': nonce,
})

signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = wallet_private_key)
txn_hash_hex = (w3.eth.sendRawTransaction(signed_txn.rawTransaction)).hex()
