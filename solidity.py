from web3 import Web3, HTTPProvider
import binascii, contract_abi, hashlib, inquirer, json, pprint, subprocess, sys, time

def get_chain_id(network):
    with open('network_ids.json') as json_file: # Opening JSON file
        chains = json.load(json_file)
        chain_item = next((item for item in chains if item["name"] == network), None)
        chain_id = int(chain_item.get('chainId'), 16)
        return chain_id

def setup():
    '''sets up connection to solidity smart contract'''
    network = input("Enter blockchain network: \n") or "Rinkeby"
    print(network + "\n")
    chain_id = get_chain_id(network)
    contract_address = input("Enter smart contract address: \n") or "0xC3737aF68f5471a2607C996525993a8E9AF1862F"
    print(contract_address + "\n")
    wallet_address = input("Enter your wallet address: \n") or "0xC7AC16DD7b42EeEc39Ee088a8702883e073D782e"
    print(wallet_address + "\n")
    wallet_private_key = input("Enter your private key: \n") or "6065a6bd9ccc0d11fd2ffb2111e68519df26b8294489cdc45fd748dd4a4f094b"
    print(wallet_private_key + "\n")
    infura_key = input("Enter your infura api key: \n") or "6c7e9aed2af146138cc7ef1986d9b558"
    print(infura_key + "\n")
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
        output = (f"{chosen_function} called successfully!\nResult: {str(result_from_getter)}")
        return output
    else:
        nonce = w3.eth.getTransactionCount(wallet_address)
        params = chosen_function[chosen_function.find('(')+1 : chosen_function.find(')')]
        arguments = params.split(',')
        number_of_args = len(arguments)
        user_inputs = []
        for x in range(1, number_of_args + 1):
            if (x == 1):
                news_agency_str = input("\nEnter news agency url [string]\n")
                encoded_str = news_agency_str.encode('utf-8')
                new_agency_checksum = hashlib.md5(encoded_str)
                checksum_hash = new_agency_checksum.hexdigest()
                print(f"\nNews agency url {news_agency_str} checksummed to {checksum_hash}\n")
                user_inputs.append(checksum_hash)
            elif (x == 2):
                incorrect_addr_format = False
                while (incorrect_addr_format == False):
                    eth_addr = input("\nEnter agency ethereum address [hexadecimal]\n") or "0x0000000000000000000000000000000000000000"
                    print(f"\nEthereum address {eth_addr} paired to {news_agency_str}\n")
                    incorrect_addr_format = w3.isChecksumAddress(eth_addr)
                    if (incorrect_addr_format == False):
                        print("\nEthereum Address not valid. Please try again...\n")
                    else:
                        user_inputs.append(eth_addr)
                        break
        out_of_gas = True                  
        while (out_of_gas == True):
            gas_choice = input("\nWhat gas limit would you like to set? (min. 150100) \n") or 150100 
            gas_choice = int(gas_choice) 
            if(gas_choice < 150100):
                print(f"\nGas limit of {gas_choice} set too low! Please increase it...\n")
            else:
                out_of_gas = False   
        txn_details = {'chainId': chain_id, 'gas': gas_choice, 'gasPrice': w3.toWei('40', 'gwei'), 'nonce': nonce}
        chosen_method = chosen_function.split('(')[0]
        setter = \
        '''contract.functions.''' + chosen_method + '("' + str(user_inputs[0]) + '", "' + str(user_inputs[1]) + '")' + '''.buildTransaction(''' + str(txn_details) + ')'
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
        output = (f"{chosen_method}({user_inputs[0]}, {user_inputs[1]}) executed successfully!\nTransaction hash: {txn_hash_hex}")
        return output

if __name__ == '__main__':
    print("\nWelcome to Authentikos! What would you like to do?\n")
    wallet_address, w3, ws3, contract, chain_id, wallet_private_key = setup()
    loop_again = True
    while (loop_again == True):
        all_functions = list_functions(contract)
        bonus_function = "getLastAgency() "
        all_functions.append(bonus_function)
        chosen_function = enumerate_functions(all_functions)
        if (chosen_function == "getLastAgency()"):
            print("i got in bob")
        else:
            output = execute_function(chosen_function)
            print(output)
            choice = input("\nWould you like to quit? (yes [y] | no [n]) \n")
            if (choice == "yes" or choice == "y" or choice == "exit" or choice == "q" or choice == "quit"):
                loop_again = False
                print("\nThanks for using Authentikos...bye now!") # Print a message that we are all finished.
            