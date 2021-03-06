import validator_pool
import fuzzer
import random
import utils

class Beacon(object):
    def __init__(self, address):
        self.address = address
        self.validator_pool = validator_pool.ValidatorPool()
        self.stakes = []
        self.revealed_entropy = fuzzer.zero_string()
        self.proposers = []
        self.proposal_hashes = {}

    def stake(self, validator):
        if(validator.address.balance<32):
            return False
        self.validator_pool.add(validator)
        self.address.balance +=32
        validator.address.balance-=32
        return True
    
    def end_of_timeslot(self):
        self.revealed_entropy = fuzzer.zero_string()
        self.proposal_hashes = {}

    def request_single_proposal(self, my_time_block_record):
        if(len(self.proposal_hashes) == 0):
            return my_time_block_record
        # get the randomly selected validator        
        selected_validator = random.choice(self.validator_pool.validators)
        my_time_block_record["current_beacon_validator_id"] = self.validator_pool.validators.index(selected_validator)
        my_time_block_record["validator_committed_hash_of_entropy"] = self.proposal_hashes[selected_validator]
        my_time_block_record["last_entropy_e_i_minus1"] = self.revealed_entropy
        # ask the random validator to propose a block
        if(selected_validator.availiable()):
            entropy = selected_validator.get_entropy()
            if(self.proposal_hashes[selected_validator] == str(hash((entropy)))):                
                my_time_block_record["validator_revealed_entropy"] = entropy                
                self.revealed_entropy = utils.xor(self.revealed_entropy,entropy)                        
                #will include reward here
            else:
                my_time_block_record["validator_revealed_entropy"] = "hash(e_i) != e_i), punish it?"
                pass #will include punishment here
        else:
            my_time_block_record["validator_revealed_entropy"] = "validator no show, punish it?"
            pass #will include punishment here
              
        my_time_block_record["current_entropy_e_i"] = self.revealed_entropy

        return my_time_block_record

    def request_proposal_hash(self, validator):
        self.proposal_hashes[validator] = validator.get_entropy_hash()

    def assign_validators(self,shard, validators):
        #STUB
        shard.validators = validators[0:255]
        return
