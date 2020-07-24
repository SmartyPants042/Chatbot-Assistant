from Output.ask import ask

def intent_filler(intent):
    """
    Fills in the unfilled parameter values for the best intent (given).
    inputs:
        intent: the most likely intent
    returns:
        False if unsuccessful in fill-in-the-blanks
        True if the intent is now fully filled.
    """

    # Now, we have the given intent likely as to what the user intended. 
    # So, we go through all of the UNFILLED parameters in that intent.
    for param_object in intent.params:
        # if the parameter value is unfilled
        if not param_object.value:
            user_response = ask(intent, param_object)

            # UNSUCCESSFUL RESPONSE EXTRACTION.
            # SKIPPING THIS INTENT (by cancelling it.)
            # FUTURE WORK NEEDED.
            if not user_response:
                return False

            param_object.value = user_response        
    return True