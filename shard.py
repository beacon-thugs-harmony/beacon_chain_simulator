
class Shard(object):

    def __init__(self):
        pass

    def request_block(self):
        for validator in self.validators:
            print (validator.address.address)
        return
