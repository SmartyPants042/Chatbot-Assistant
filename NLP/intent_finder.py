from Data.intent_list import intent_list
from Input import intents
from NLP.likeliness_finder import likeliness_finder
from NLP.intent_filler import intent_filler

# NOTE: THRESHOLD OF SCORES IS >0 (FOR NOW)
def intent_finder(user_input, threshold=0, super_intent=None):
    """
    Finds the best intent (if there is) WITH the filled values
    (ALL: prefilled + newly-asked).
    Simultaneously resets the parameters all the other intents.

    inputs:
        user_input:
            the user input text
        threshold:
            How strict do we want to be, with finding intents.
            We compare this with the score returned from the 
            likeliness_finder function.
            =0: Not strict (no conditions met)
            =1: Strict (trigger string) [RECOMMENDED]
            >1: VERY STRICT (trigger string + filled parameters)
        super_intent:
            when we ask user for confirmation on important intents,
            we'll have intent checking for agree/deny, with the super
            intent as the intent that we are confirming for.
    return: 
        the best intent with the maximum score above threshold
    """

    #################### FINDING THE INTENTS AND SCORES ####################
    scored_intents = intent_scorer(user_input)

    # if the max score does not pass the threshold,
    # we haven't found any intent worthy
    if(scored_intents[0][0] < threshold):
        # reset all intents
        intent_resetter()
        return None

    #################### FILLING IN THE INTENT PARAMETERS ####################
    # Find the first fully fleshed intent
    # We iterate through the sorted list of socred intents.
    # FUTURE WORK: FIGURE OUT WHY THE USER KILLED THIS INTENT
    # USING STATISTICAL METHODS
    intent_filling_success = intent_filler(scored_intents[0][1])
    i = 1
    while(not intent_filling_success and i < len(scored_intents)):
        intent_filling_success = intent_filler(scored_intents[i][1])
        i += 1

    # We went through all the intents on-by-one
    # if any of them had success in getting filled, we'll reset the rest
    # else, we'll reset all of em
    if i < len(scored_intents):
        i -= 1
        best_intent = scored_intents[i][1]
    else:
        best_intent = None    
    
    #################### RESET UNSUCCESSFUL INTENTS ####################
    intent_resetter(best_intent, super_intent)
    
    #################### RETURN FULLY FILLED BEST INTENT ####################
    return best_intent

# bruteforce method of finding intent
# we iterate through all the intents, 
# creating one single object for each one.
# we then calculate the scores for each, 
# based on trigger and pre-filled values. 
def intent_scorer(user_input):
    """
    input:
        user_input:
            The user input text to process.

    return:
        A sorted list of tuples of (scores_of_intent, intent)
    
    
    TIME COMPLEXITY: O(N*M + NlogN)
    WHERE: 
        N = NUMBER OF INTENTS
        M = COMPLEXITY OF FINDING THE LIKELINESS(SCORE)
    """
    scored_intents = []

    # iterating through all the intents
    # getting the most likely intent
    for intent in intent_list:
        # all the items in intent_list are strings 
        # of the class names
        assert(type(intent) == str)

        # getting the classes one by one
        class_name = getattr(intents, intent)()

        # how likely is that the user meant this intent
        # likeliness_finder also fills in the 
        # pre-said parameter values,
        # which we reset, for all the intents except the best.
        # It does NOT ask for new parameter inputs.
        score = likeliness_finder(user_input, class_name)
    
        # FUTURE WORK: ADD OTHER PARAMETERS
        # SUCH AS freq_local, freq_global, likeliness
        # FIND A FORMULA TO COMBINE THESE,
        # then add this to the score.

        scored_intents.append((score, class_name))

    # the score acts as key for the sorting
    def scoring_function(item):
        return item[0]

    scored_intents = sorted(scored_intents, key=lambda item: item[0] , reverse=True)
    return scored_intents

def intent_resetter(best_intent=None, super_intent=None):
    """
    If there is a best intent given, resets all but the best
    else, resets all.

    In case of super_intents, we definitely have a best_intent.
    We iterate through the intent list, and reset all except
    the best_intent and super_intent.

    inputs:
        best_intent: 
            the best scoring intent
        super_intent:
            the important intent that triggers confirmation, 
            and thus this function.
    
    return:
        None
    """

    if best_intent:
        for intent in intent_list:
            intent_class = getattr(intents, intent)()
            # if not the best intent, we reset it.
            if intent_class.name != best_intent.name:
                if not super_intent:
                    intent_class.reset()
    else:
        for intent in intent_list:
            intent_class = getattr(intents, intent)()
            intent_class.reset()

    return
