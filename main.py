from NLP.intent_finder import intent_finder
from Output.response import response

# MAIN loop
while(True):
    user_input = input("Input: ")

    # EXIT CONDITION
    if(user_input == "stop"):
        break

    #################### BOT WORK ####################
    # FINDING THE BEST INTENT & FILLING IT IN
    best_intent = intent_finder(user_input)

    # we couldn't extract any worthy intent
    if not best_intent:
        print("Sorry, didn't get you!")
        continue
    
    #################### GRAPH WORK ####################
    # STORING the input now, for the graph construction
    prev_node = best_intent
    #################### END: GRAPH WORK ####################

    
    #################### DATABASE WORK ####################
    # increasing frequencies
    best_intent.freq_local += 1
    best_intent.freq_global += 1
    # FUTURE WORK 
    # SET best_intent.likeliness HERE

    # GIVING THE BUILT IN RESPONSE
    response(best_intent, 0) 
    
    # Future Work: increase call frequencies
    # DATA-BASE STORAGE || API CALLS
    # NOTE: intent.params has all the use-ful data

    # Dump the intent's filled parameters here ...
    if len(best_intent.params) and not best_intent.cancelled:
        print(f"\nSummary for {best_intent.name}:")
        for param in best_intent.params:
            print(f"{param.called_by}: {param.value}")
    #################### END: DATABASE WORK ####################

    # finally, reset the best intent's parameters
    best_intent.reset()
    if(best_intent.name == 'basic_bye'):
        break

    #################### END: BOT WORK ####################

    
print("\nCompleted Execution.")
