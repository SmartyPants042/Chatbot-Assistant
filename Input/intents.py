# NOTE: intents expanded from reference: intent_list
# Any additions must be reflectd in both 
# this file and the intent_list 

# input dictionary for the triggers
from Data.trigger_dict import trigger_dict as triggers

# super class for all the intents
from Input.Intent import Intent

# getting the parameter handler
from Input.param_handler import param_handler as param

class basic_hello(Intent):
    name = 'basic_hello'
    triggers = triggers[name]
    params = []

    def __init__(self):
        Intent.__init__(
            self, 
            name=basic_hello.name, 
            triggers=basic_hello.triggers,
            params=basic_hello.params
        )
        
class basic_agree(Intent):
    name = 'basic_agree'
    triggers = triggers[name]
    params = []

    def __init__(self):
        Intent.__init__(
            self, 
            name=basic_agree.name, 
            triggers=basic_agree.triggers,
            params=basic_agree.params
        )

class basic_deny(Intent):
    name = 'basic_deny'
    triggers = triggers[name]
    params = []

    def __init__(self):
        Intent.__init__(
            self, 
            name=basic_deny.name, 
            triggers=basic_deny.triggers,
            params=basic_deny.params
        )

class basic_challenge(Intent):
    name = 'basic_challenge'
    triggers = triggers[name]
    params = []

    def __init__(self):
        Intent.__init__(
            self, 
            name=basic_challenge.name, 
            triggers=basic_challenge.triggers,
            params=basic_challenge.params
        )

class basic_bye(Intent):
    name = 'basic_bye'
    triggers = triggers[name]
    params = []

    def __init__(self):
        Intent.__init__(
            self, 
            name=basic_bye.name, 
            triggers=basic_bye.triggers,
            params=basic_bye.params
        )

class reminder(Intent):
    name = 'reminder'
    triggers = triggers[name]
    params = [
        param('name'),
        param('date_time'),
        param('number', called_by='frequency'),
    ]

    def __init__(self):
        Intent.__init__(
            self, 
            name=reminder.name, 
            triggers=reminder.triggers,
            params=reminder.params,
            importance=0,
        )
