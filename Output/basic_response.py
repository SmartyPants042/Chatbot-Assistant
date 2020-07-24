from Data.response_dict import basic_response_dict as respond
import random

def basic_response(intent_name):
    """
    this function gets basic type of intents,
    and replies with predef answers
    prints the response
    
    input: 
        intent_name
    return:
        none
    """
    print(random.choice(respond[intent_name]))
    return    