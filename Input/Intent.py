class Intent():
    """
    The super class for defining any intent.
    inputs:
        name: 
            the name of the intent
        trigger: 
            the word(s) used to initiate any intent
        params:
            the 'fill in the blanks' for any intent
        importance:
            is it really important? scale [-1, 0, 1]
            -1: basic intents (for basic_intent_name)
            +0: normal intents (default)
            +1: important intents (DEFINE IT EXPLICITLY)

    other_parameters:
        likeliness:
            The default score of how likely an intent is to be called.
            Sort-of like the constant to the intent__finder
        freq_local:
            DataBase part; stores the local number of time this
            intent is called    
        freq_global:
            DataBase part; stores the global number of time this
            intent is called
        cancelled:
            if the user denys to save this
    """
    
    def __init__(
        self,
        name,
        triggers,
        params,
        importance=0
    ):

        #################### INPUT PARAMETERS ####################
        
        self.name = name
        self.triggers = triggers
        self.params = params

        if(self.name[:5] == 'basic'):
            self.importance = -1
        else:
            self.importance = importance

        
        #################### OTHER PARAMETERS ####################
        
        # the probability that the user actually
        # intended this, based on frequencies?
        # FUTURE WORK
        self.likeliness = None
        
        # FUTURE WORK: Sort the intents,
        # and better the 'bruteforce', as we move
        # onto more statistical approaches
        # GET THIS FROM THE DATABASE
        self.freq_local = 0
        self.freq_global = 0

        # if the intent is still to be fulfilled
        self.cancelled = False


    # Resetting ALL the parameters' values
    def reset(self):
        for param in self.params:
            param.value = None
        
        self.cancelled = True
    