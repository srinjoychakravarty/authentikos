import json, time
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
        txids = []
        for key, value in data.items():
            news_asset = {'data': {'news_agency_asset': {key: value}}}
            print(news_asset)
            metadata_checksum = {'checksum': key}
            prepared_creation_tx = bdb.transactions.prepare(operation = 'CREATE', signers = alice.public_key, asset = news_asset, metadata = metadata_checksum)
            fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx, private_keys = alice.private_key)
            sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)
            time.sleep(1)
            txid = sent_creation_tx['id']
            txids.append(txid)
        return txids

def find_asset(search_term):
    retrieved_object = bdb.assets.get(search = search_term)
    return retrieved_object

def write_data(bdb, alice):
    import_choice = input("\nWould you like to write data to BigChainDB from a json .txt file? [yes (y) | no (n)]\n")
    if (import_choice == "yes" or import_choice == "y"):
        same_dir_choice = input("\nIs your json .txt file in the same directory as this script?[yes (y) | no (n)]\n")
        if (same_dir_choice == "yes" or same_dir_choice == "y"):
            filename = ""
            while (filename == ""):
                filename = input("\nName of file including extenstion (e.g. auth.txt):\n")
                if(filename == ""):
                    print("\nFilename cannot be a blank string! \nPlease enter a filename...\n")
            txids = write_json(filename, bdb, alice)
            print(f"\n Transaction Succesful!\n Transaction IDs: {txids}\n Thanks for using Authentikos...bye now!") 
        elif (same_dir_choice == "no" or same_dir_choice == "n"):
            full_path = ""
            while (full_path == ""):    
                full_path = input("\nEnter full path to file ending in / (e.g /home/eos/hyperpartisan_news_index/ \n")
                if(full_path == ""):
                    print("\nPath cannot be a blank string! \nPlease enter full path directory...\n")
            filename = ""
            while (filename == ""):
                filename = input("\nName of file including extenstion (e.g. auth.txt):\n")
                if(filename == ""):
                    print("\nFilename cannot be a blank string! \nPlease enter a filename...\n")
            full_filename = full_path + filename
            txids = write_json(full_filename, bdb, alice)
            print(f"\n Transaction Succesful!\n Transaction IDs: {txids}\n Thanks for using Authentikos...bye now!") 
        else:
            print(f"\n No directory information! Thanks for using Authentikos...bye now!")         
    else:              
        activity_decision = input("\nWould you like to search for something in BigChainDB? [yes (y) | no (n)]\n")
        if (activity_decision == "yes" or activity_decision == "y"):
            keep_looping = True
            while (keep_looping == True):
                keyword = ""
                while (keyword == ""):
                    keyword = input("\nEnter keyword to search by: \n")
                    if (keyword == ""):
                        print("\nKeyword cannot be a blank string! \nPlease enter something...\n")
                retrieved_obj_list = find_asset(keyword)
                if (len(retrieved_obj_list) == 0):
                    print("\n Your search did not return any results!")
                    repeat_search = input("\nWould you like to search again? [yes (y) | no (n)]\n")
                    if (repeat_search == "no" or repeat_search == "n"):
                        keep_looping = False
                        print("\n Search session closed! Thanks for using Authentikos...bye now!") 
                    elif (repeat_search == "yes" or repeat_search == "y"):
                        keep_looping = True
                    else:
                        keep_looping = False
                        print("\n No search decision! Thanks for using Authentikos...bye now!") 
                        break   
                elif (len(retrieved_obj_list) > 0):
                    print(f"\n Your search was successful: \n {retrieved_obj_list}")
                    repeat_search = input("\nWould you like to search again? [yes (y) | no (n)]\n")
                    if (repeat_search == "no" or repeat_search == "n"):
                        keep_looping = False
                        print("\n Search session closed! Thanks for using Authentikos...bye now!") 
                    elif (repeat_search == "yes" or repeat_search == "y"):
                        keep_looping = True
                    else:
                        print("\n No relevant search decision! Thanks for using Authentikos...bye now!") 
                        break         
        elif (activity_decision == "no" or activity_decision == "n"):
            print("\nThanks for using Authentikos...bye now!") 
        else:
            print("\n No search decision! Thanks for using Authentikos...bye now!") 

if __name__ == '__main__':
    connection_choice = input("\nWelcome to Authentikos! \nWould you like to connect BigChainDB? [yes (y) | no (n)] \n")
    if (connection_choice == "yes" or connection_choice == "y"):
        print("\nconnecting to bigchaindb...")
        bdb = connect_db()
        print(f"\nConnection Successful! \n {bdb}")
        keypair_choice = input("\nWould you like to generate a BigChainDB keypair? [yes (y) | no (n)]\n")
        if (keypair_choice == "yes" or keypair_choice == "y"):
            print("\nGenerating keys...")
            alice = generate_key()
            print(f"\nYour public key is: {alice.public_key}")
            print(f"\nYour private key is: {alice.private_key}")           
            write_data(bdb, alice)
        elif (keypair_choice == "no" or keypair_choice == "n"):
            import_decision = input("\nWould you like to import your own BigChainDB private key? [yes (y) | no (n)]\n")
            if(import_decision == "yes" or import_decision == "y"):
                alice = input("\nType in or Copy/Paste in your private key: \n") or "CCupfJjW4gcve67Tz76qAUyniw55pBAGpbn7wR9iAXTZ"
                print(f"\n Activated Private Key: {alice}\n")
                write_data(bdb, alice)
            elif(import_decision == "no" or import_decision == "n"):
                print("\n Sorry! BigChainDB requires a private key to be imported or generated! Thanks for using Authentikos...bye now!") 
            else:
                 print("\n No key import decision! Thanks for using Authentikos...bye now!") 
        else:
            print("\n No keypair generation decision! Thanks for using Authentikos...bye now!") 
    elif (connection_choice == "no" or connection_choice == "n"):
        print("\nThanks for using Authentikos...bye now!") 
    else:
        print("\n No connection decision! Thanks for using Authentikos...bye now!") 