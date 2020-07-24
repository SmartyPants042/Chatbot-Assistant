from NLP.intent_finder import intent_finder
from Output.response import response

# The user asks the bot to stop
user_said_bye = False

# The MAIN chat loop
while(True and not user_said_bye):
    user_input = input("Input: ")

    # EXIT CONDITION
    if(user_input == "stop"):
        break

    # FINDING THE BEST INTENT
    best_intent = intent_finder(user_input)

    # we couldn't extract any worthy intent
    if not best_intent:
        print("Sorry, didn't get you!")
        continue

    # else, print("RESPONSE SUCCESS")
    # the input now, for the graph construction
    prev_node = best_intent

    # increasing frequencies
    best_intent.freq_local += 1
    best_intent.freq_global += 1
    # FUTURE WORK 
    # SET best_intent.likeliness HERE

    response(best_intent) 
    
    # Future Work: increase call frequencies
    # DATA-BASE STORAGE || API CALLS
    # NOTE: intent.params has all the use-ful data

    # Dump the intent's filled parameters here ...
    if len(best_intent.params) and not best_intent.cancelled:
        print(f"\nSummary for {best_intent.name}:")
        for param in best_intent.params:
            print(f"{param.called_by}: {param.value}")

    # finally, reset the best intent's parameters
    best_intent.reset()

    if(best_intent.name == 'basic_bye'):
        user_said_bye = True
        break

    
print("\nCompleted Execution.")
