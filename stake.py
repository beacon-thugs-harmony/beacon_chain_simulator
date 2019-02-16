class Stake(object):
    def __init__(self, beacon_address, validator_address):
        beacon_address.balance = beacon_address.balance+32;
        validator_address.balance = validator_address.balance-32;
        self.beacon_address = beacon_address
        self.validator_address = validator_address
