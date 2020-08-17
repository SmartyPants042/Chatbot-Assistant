import nltk
from Output.ask import ask

# def user_data_extraction()

def likeliness_finder(user_input, intent, trigger_threshold=1, param=None):
    """
    checks how likely is this given intent the intent of the user. 

    input: 
        user_input:
            user's current text input
        intent:
            intent object
        trigger_threshold: 
            How strict we want to be with trigger words comparisons.
            * 1 represents that we match all the trigger words
            of any trigger string in the intent with the user's input.
            * 0 represents that even if the NONE of the trigger words
            are activated, we will still consider our input as our intent.
            More about this in intent_finder.
            Q: So then, what's the use of zero? 
            A: Note that it will still fill in the param values it finds.
            These param values are extracted from the user input.
        param:
            whether we have to check for a certain parameter or not.
            When its given, we are looking at the base case of this 
            recursive function.

    returns: 
        the calculated likeliness of the 
        intended object using NLP tools.

        * A negative score means 
        the trigger is not activated.
        ** (WE EXIT IMMEDIATEDLY FOR NOW)

    NOTE: 
        THIS IS A RECURSIVE FUNCTION
        How? this function is called from intent_scorer, 
        with the hopes of getting the score. We calculate the score and 
        we fill in the pre-filled parameter values.    

        This function is called again, to fill in the uniflled-parameter
        values. This represents the 'base case' of this function.
        So, to fill in each of the parameters speparately, 
        we have asked the user for input (as handled by the 'ask' function.)
        Now, we validate using the likeliness finder. Only then can we 
        return each filled parameter's values. In this base case, 
        we fill em one by one. 
    """

    #################### SETTING UP THE BASIC NLP TOOLS ####################

    # NLP TASK 0: TOKENIZATION, REMOVING PUNCTUATION AND CASING
    word_tokens = nltk.tokenize.word_tokenize(user_input)
    tokenized_words = [word.lower() for word in word_tokens if word.isalnum()]

    # print("tokens: ", tokenized_words)

    # NLP TASK 1: REMOVING STOP WORDS
    # TIME COMPLEXITY O(N*M): 
    # N = LENGTH OF USER INPUT
    # M = LENGTH OF STOP WORDS
    # SO, O(1) TO FILTER THE SENTENCE
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_words = [
        word for word in tokenized_words if not word in stop_words
    ]

    #################### BASE CASE OF THIS FUNCTION #####################
    # Given a parameter to store the value in
    # IMMEDIATE WORK NEEDED. 
    # THIS IS THE LAST STAGE OF THE BOT RESPONSE,
    # before it goes on to the next main loop iteration.
    if param:
        return user_input

    #################### THE REST OF THE RECURSION ####################
    # The score to be returned at the end
    score = 0

    # Here, we are trying to match each possible trigger string,
    # each consisting of some 'trigger'/'key' words (seperated by a space).
    # For each word of the trigger words that match
    # any of the user words, we increase its point. 
    # If all of the trigger words are satisfied, 
    # we say that the intent governing the trigger strings 
    # has been satisfied.
    # TLDR; if the trigger is activated according to threshold,
    # cool, else byee 
    flag = False
    for trigger_string in intent.triggers:

        # getting all the trigger words
        list_trigger_words = trigger_string.split()
        num_triggers = len(list_trigger_words)
        temp_num_triggers = 0
        for word in list_trigger_words:
            # comparing with the FILTERED INPUT
            # if word found, we increase the words counter
            if word in filtered_words:
                temp_num_triggers += 1
        
        # the trigger words of the trigger string
        # have been satisfied according to the threshold.
        # We have found the intent we are looking for. Done.
        if temp_num_triggers/num_triggers >= trigger_threshold:
            flag = True
            score += 1
            break

    # no trigger found, the intent sent to us 
    # is not the one we need to execute
    if not flag:
        return -1

    #################### FINDING THE PRE-FILLED PARAMETERS ####################
    # IMMEDIATE WORK NEEDED
    # pass for now
    for params in intent.params:
        pass
    
    # returns the score that determines 
    # whether this intent should be filled or not
    return score

    #################### ASKING FOR THE NEW PARAMETERS ####################
    # done in intent_filler, handled separately
