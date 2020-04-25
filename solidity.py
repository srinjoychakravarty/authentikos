from web3 import Web3, HTTPProvider
import binascii, contract_abi, inquirer, json, pprint, subprocess, sys, time

def get_chain_id(network):
    with open('network_ids.json') as json_file: # Opening JSON file
        chains = json.load(json_file)
        chain_item = next((item for item in chains if item["name"] == network), None)
        chain_id = int(chain_item.get('chainId'), 16)
        return chain_id

def setup():
    '''sets up connection to solidity smart contract'''
    network = input("Enter blockchain network: ") or "Rinkeby"
    print(network)
    chain_id = get_chain_id(network)
    contract_address = input("Enter smart contract address: ") or "0xEEC42723E36b3cB362D9cB49b8Cd2a111454FF03"
    print(contract_address)
    wallet_address = input("Enter your wallet address: ") or "0xC7AC16DD7b42EeEc39Ee088a8702883e073D782e"
    print(wallet_address)
    wallet_private_key = input("Enter your private key: ") or "6065a6bd9ccc0d11fd2ffb2111e68519df26b8294489cdc45fd748dd4a4f094b"
    print(wallet_private_key)
    infura_key = input("Enter your infura api key: ") or "6c7e9aed2af146138cc7ef1986d9b558"
    print(infura_key)
    websockets_rinkeby = "wss://rinkeby.infura.io/ws/v3/" + infura_key
    ws3 = Web3(Web3.WebsocketProvider(websockets_rinkeby, websocket_kwargs={'timeout': 60}))
    https_rinkeby = "https://rinkeby.infura.io/v3/" + infura_key
    w3 = Web3(HTTPProvider(https_rinkeby))
    contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)
    return (wallet_address, w3, ws3, contract, chain_id, wallet_private_key)

def list_functions(contract):
    '''lists all smart contract functions '''
    return contract.all_functions()

def enumerate_functions(all_functions):
    '''enumerates all read functions on smart contract '''
    function_set = {str(function).replace('<Function ', '')[:-1] for function in all_functions}
    question = [inquirer.List('function', message = "Which function to call?", choices = function_set)]
    answer = inquirer.prompt(question)
    chosen_function = answer['function']
    return chosen_function

def execute_function(chosen_function):
    '''calls getter functions or executes setter functions via ether transactions'''
    if (chosen_function[0:3] == "get"):
        getter = \
        '''contract.functions.''' + chosen_function + '''.call()'''
        result_from_getter = eval(getter)
        print(f"{chosen_function} called successfully!\nResult: {str(result_from_getter)}")
    else:
        nonce = w3.eth.getTransactionCount(wallet_address)
        params = chosen_function[chosen_function.find('(')+1 : chosen_function.find(')')]
        arguments = params.split(',')
        number_of_args = len(arguments)
        if 'address' in arguments:
            address_at_index = arguments.index("address")
        user_inputs = []
        for x in range(1, number_of_args + 1):
            user_inputs.append(input(f"Please enter Parameter {x}: "))
        txn_details = {'chainId': chain_id, 'gas': 140000, 'gasPrice': w3.toWei('40', 'gwei'), 'nonce': nonce}
        chosen_method = chosen_function.split('(')[0]
        setter = \
        '''contract.functions.''' + chosen_method + '("' + user_inputs[0] + '", "' + user_inputs[1] + '")' + '''.buildTransaction(''' + str(txn_details) + ')'
        txn_dict = eval(setter)
        signed_setter = \
        '''(w3.eth.account.signTransaction(''' + str(txn_dict) + ', private_key = "' + wallet_private_key + '")).rawTransaction'
        signed_txn = eval(signed_setter)
        sent_txn_cmd = \
        '''w3.eth.sendRawTransaction(''' + str(signed_txn) + ')'
        txn_hash = eval(sent_txn_cmd)
        construct_hex = \
        '''(''' + str(txn_hash) + ').hex()'
        txn_hash_hex = "0x" + eval(construct_hex)
        print(txn_hash_hex)
        print(f"{chosen_method}({user_inputs[0]}, {user_inputs[1]}) executed successfully!\nTransaction hash: {txn_hash_hex}")

if __name__ == '__main__':
    wallet_address, w3, ws3, contract, chain_id, wallet_private_key = setup()
    all_functions = list_functions(contract)
    chosen_function = enumerate_functions(all_functions)
    execute_function(chosen_function)
