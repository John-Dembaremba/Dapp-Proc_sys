from web3 import Web3, contract
import json

from . import abi_addr

ganache_url = 'http://127.0.0.1:7545'

class WebAPI(object):

    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        self.Accounts = self.web3.eth.accounts

    def checkConnection(self):
        return self.web3.isConnected()
    
    def contract_interact(self):
        contract = self.web3.eth.contract(address=abi_addr.get_addr(), abi=abi_addr.get_abi())
        return contract

    def post_jobs(self, user, name, product_type, product, requiments, date, delivery_period):
        self.web3.eth.defaultAccount = user

        contract = self.contract_interact()

        txt_hash = contract.functions.addTransaction(
            name, 
            product_type, 
            product, 
            requiments,
            date, 
            delivery_period,
        ).transact()
        
        txt_receipt = self.web3.eth.wait_for_transaction_receipt(txt_hash)

        txt_logs = contract.events.Jobs().processReceipt(txt_receipt)
    
        return txt_receipt

    def apply_jobs(self, user, job_id, name, unit_price, total_price, zimra, praz, doc_validity):
        self.web3.eth.defaultAccount = user

        contract = self.contract_interact()

        txt_hash = contract.functions.addSuppliers(
            job_id, 
            name, 
            unit_price,
            total_price,
            zimra, 
            praz, 
            doc_validity,

        ).transact()
        
        txt_receipt = self.web3.eth.wait_for_transaction_receipt(txt_hash)
        
        return txt_receipt

    def award_bidder(self, user, job_id, name, unit_price, total_price, zimra, praz, doc_validity):
        self.web3.eth.defaultAccount = user

        contract = self.contract_interact()

        txt_hash = contract.functions.award_bider(
            job_id, 
            name, 
            unit_price,
            total_price,
            zimra, 
            praz, 
            doc_validity,

        ).transact()
        
        txt_receipt = self.web3.eth.wait_for_transaction_receipt(txt_hash)
        
        return txt_receipt

      
    def get_events_jobs(self):
        try:
            event_filter = self.contract_interact().events.Jobs().createFilter(fromBlock=0, toBlock='latest')
            return event_filter.get_all_entries() 
        except KeyError:
            return None

    def get_new_events_jobs(self):
        try:
            event_filter = self.contract_interact().events.Jobs().createFilter(fromBlock=0, toBlock='latest')
            return event_filter.get_new_entries() 
        except KeyError:
            return None

    def get_events_bidders(self):
        event_filter = self.contract_interact().events.Bidders().createFilter(fromBlock=0, toBlock='latest')
        return event_filter.get_all_entries() 
        

    def get_winner_events_bidders(self):
        try:
            event_filter = self.contract_interact().events.Winner().createFilter(fromBlock=0, toBlock='latest')
            return event_filter.get_all_entries() 
        except KeyError:
            return None

    
    def get_block(self, block_number):
        contract = self.web3.eth.get_block(block_number, full_transactions=False)
        return contract


