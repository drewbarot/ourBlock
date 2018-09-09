#!/usr/bin/python3

import time
from web3 import Web3, HTTPProvider
import contract_abi

contract_address = Web3.toChecksumAddress('0x32732aa7ff722de173fc0165cb9f55f07bda7a30')
wallet_private_key   = '267ce4750edc5da3db0379537885025b6a31f012fb22ef2b59487a67b7f79193'
wallet_address       = Web3.toChecksumAddress('0xf2c5c9bb7acd064ccb568a655b0007298b3b1c90')

w3 = Web3(HTTPProvider('https://ropsten.infura.io/TQqgYbZ0R31BSFiHJATb'))

w3.eth.enable_unaudited_features()

contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

def send_ether_to_approve_contract(amount_in_ether):

    wei_amount = w3.toWei(amount_in_ether,'ether');

    nonce = w3.eth.getTransactionCount(wallet_address)

    txn_dict = {
            'to': Web3.toChecksumAddress(contract_address),
            'value': wei_amount,
            'gas': 2000000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'nonce': nonce,
            'chainId': 3
    }

    signed_transaction = w3.eth.account.signTransaction(txn_dict, wallet_private_key)

    hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    receipt = None

    count = 0
    
    while receipt is None and (count < 30):

        receipt = w3.eth.getTransactionReceipt(hash)

        print(receipt)

        time.sleep(10)


    if receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'receipt': receipt}


def check_whether_address_is_approved(address):

    return contract.functions.isApproved(address).call()


def broadcast_a_location(latitude, longitude, crime_classification):

    nonce = w3.eth.getTransactionCount(wallet_address)
    
    message = 'Lat: ' + str(latitude) + ' Long: ' + str(longitude) + ' Message: ' + str(crime_classification)
    txn_dict = contract.functions.broadcastOpinion(message).buildTransaction({
        'chainId': 3,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

    signed = w3.eth.account.signTransaction(txn_dict, private_key=wallet_private_key)

    result = w3.eth.sendRawTransaction(signed.rawTransaction)

    tx_receipt = w3.eth.getTransactionReceipt(result)

    count = 0
    
    while tx_receipt is None and (count < 30):

        time.sleep(10)

        tx_receipt = w3.eth.getTransactionReceipt(result)


    if tx_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    processed_receipt = contract.events.OpinionBroadcast().processReceipt(tx_receipt)

    print(processed_receipt)

    output = "Address {} broadcasted the opinion: {}"\
        .format(processed_receipt[0].args._soapboxer, processed_receipt[0].args._opinion)
    print(output)

    return {'status': 'added', 'processed_receipt': processed_receipt}

def sendCrime(latitude, longitude, crime):

    send_ether_to_approve_contract(0.020001)

    is_approved = check_whether_address_is_approved(wallet_address)
    
    print(is_approved)

    broadcast_a_location(latitude, longitude, crime)

    print(latitude, longitude, crime)