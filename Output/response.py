from Data.response_dict import basic_response_dict as responsd
from Input import intents
from NLP.likeliness_finder import likeliness_finder
from Output.ask import ask_sure
from Output.basic_response import basic_response

def response(intent, importance_threshold=0):
    """
    Gives the generic, built in response.
    input:
        intent:
            the intent object which we have to respond
            to, the selected 'likely' one
        importance_threshold:
            How important is this intent?
            We'll ask user for confirmation if its important
            else, we'll just accept it.
    return:
        None
    """

    # if the intent is basic, 
    # we reply with preset answers 
    if(intent.name[:5] == 'basic'):
        basic_response(intent.name)
        return

    # if the intent is important    
    if intent.importance >= importance_threshold:
        # confirm with user
        user_sure = ask_sure(intent)
        if user_sure:
            basic_response('basic_agree')
            # for param in intent.params: 
            #     print(param.value)
        else:
            intent.cancelled = True
            basic_response('basic_deny')
    
    return
