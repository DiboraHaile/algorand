from algosdk import account, mnemonic
from algosdk.v2client import algod
# build transaction
from algosdk import transaction
from algosdk import constants
import json
import base64



def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))



def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)


    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    # params.flat_fee = True
    # params.fee = constants.MIN_TXN_FEE 
    receiver = "C3NOVSWZWPSZ645WGID4E36GQ7RTUUR4QXP54IHBLBMJDXPD2VBTRWQHD4"
    note = "hello".encode()
    amount = 2
    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)
    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)
    account_info = algod_client.account_info(my_address)
    #submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
    json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
    confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transfered: {} microAlgos".format(amount) )    
    print("Fee: {} microAlgos".format(params.fee) ) 

    
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

if __name__ == '__main__':
    # generate_algorand_keypair()
    first_transaction_example('qTM9BFdLSU78PxsTbNHuoxCBaWl/FVs1oYK+CSzksGyXBHKFyLZx3l6/qhqmbVTPLJk3ZJ3azG3ku5tsC7nkZw==','S4CHFBOIWZY54XV7VINKM3KUZ4WJSN3ETXNMY3PEXONWYC5Z4RTZGXMTDI')


#HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA
# My address: S4CHFBOIWZY54XV7VINKM3KUZ4WJSN3ETXNMY3PEXONWYC5Z4RTZGXMTDI
# My private key: qTM9BFdLSU78PxsTbNHuoxCBaWl/FVs1oYK+CSzksGyXBHKFyLZx3l6/qhqmbVTPLJk3ZJ3azG3ku5tsC7nkZw==
# My passphrase: inside visit link rely myth bean zoo brass list east wash any acquire foil win betray problem luggage donor orbit fix decorate grain about similar


# My address: C3NOVSWZWPSZ645WGID4E36GQ7RTUUR4QXP54IHBLBMJDXPD2VBTRWQHD4
# My private key: 2AGG2e61R02fHkidmDHqeCp2qF8bQSk9TUdadjwhaIgW2urK2bPln3O2MgfCb8aH4zpSPIXf3iDhWFiR3ePVQw==
# My passphrase: deposit blossom holiday galaxy month spy visual elite beauty shoe insect pole unable tube sustain donate pioneer crunch casual grant jump analyst drive above inmate

# Genesis ID: testnet-v1.0
# Genesis hash: SGO1GKSzyE7IEPItTxCByw9x8FmnrCDexi9/cOUJOiI=