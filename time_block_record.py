class TimeBlockRecord(object):    
    current_timeslot_id                       = None
    current_epoch_id                          = None
    current_beacon_validator_id               = None
    validator_committed_hash_of_entropy       = None
    validator_revealed_entropy                = None
    last_entropy_e_i_minus1                   = None
    current_entropy_e_i                       = None
    vdf_input                                 = None
    current_random_seed_r_j                   = None
    epoch_when_r_j_generation_started         = None
    vdf_output_r_i                            = None    
    
    def __init__(self, config):
        self.config = config
        self.shard_validator                  = [None] * config["NSHARDS"]