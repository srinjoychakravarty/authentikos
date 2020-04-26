import json
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'http://localhost:9984'
bdb = BigchainDB(bdb_root_url)
alice = generate_keypair()
with open('authentikos_wax.txt') as json_file:
    data = json.load(json_file)
    for key, value in data.items():
        news_asset = {'data': {'news_agency_asset': {key: value}}}
        print(news_asset)
        metadata_checksum = {'checksum': key}
        prepared_creation_tx = bdb.transactions.prepare(operation = 'CREATE', signers = alice.public_key, asset = news_asset, metadata = metadata_checksum)
        fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx, private_keys = alice.private_key)
        bdb.transactions.send_commit(fulfilled_creation_tx)

    
