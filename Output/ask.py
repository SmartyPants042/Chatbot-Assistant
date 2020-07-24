import NLP.intent_finder as finder
import NLP.likeliness_finder as recurse
import nltk

def ask(intent, param):
    """
    NOTE:
        This function is NOT controlled by the main loop. 
        Its execution runs independent. 
        FUTURE WORK: HANDLE SMALL TALK
    inputs:
        takes in a param and its intent, 
        asks questions to fill it in.
    
    return:
        the user response if we were able to figure it out
        None if we couldn't get it.
    """

    user_response = input(f"Tell the {intent.name}'s {param.called_by}: ")

    # input extraction logic
    extracted_user_input = validate_input(user_response, intent, param)

    # if we are able to extract, we exit peacefully
    if extracted_user_input:
        return extracted_user_input
    
    # or, ... we GOIN TO SPAM THE USER! WHOO 
    # (I am high now. Plx halp.)
    # Why u reading this, huh? Get a life.
    # Bruh Sound Effect #2.
    oops = 1
    while oops <= 3:
        user_response = input("Couldn't Get it ... Please repeat: ")
        
        extracted_user_input = validate_input(user_response, intent, param)
        
        # phew, we got 'em
        if extracted_user_input:
            return extracted_user_input
        
        # aww shet, here we go again
        oops += 1

    # Mission Failed. We'll get em next time!
    return None

def ask_sure(intent):
    """
    confirms with the user for the important intents.
    FUTURE WORK: Small_Talk handling
    """

    user_input = input("Are you sure? ")
    most_likely_intent = finder.intent_finder(user_input, super_intent=intent)
    
    # found some intent
    try:
        if most_likely_intent.name != 'basic_agree':
            return False
    # no worthy intent found
    except:
        return False

    return True

def validate_input(user_response, intent, param):
    """
    inputs:
        user_response:
            what the user responds to our query,
        intent:
            the 'predicted' intent
        param:
            the parameter we want to fill
    return:
        The entity useful in the user input.
        None if none found.

    NOTE:
        This relies on the base case of the function
        'likeliness_finder'.  
    """

    extracted_user_input = recurse.likeliness_finder(
        user_input=user_response,
        intent=intent,
        param=param)
    
    return extracted_user_input