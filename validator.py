class Validator:
    #Honesty, bias, availability will be 0-1, 1 being 'good'
    def __init__(self, address, honesty, availability, bias):
        self.address = address;
        self.honesty = honesty;
        self.availability = availability;
        self.bias = bias;