# For multiple words to be present in a trigger,
# separate them with whitespaces.
# eg: "stocks show" will mean that both need to be present
# in the user_input for accepting this intent.

trigger_dict = {
    'basic_hello': [
        'hey',
        'hello',
        'hi',
        'sup',
        'wassup',
        'yo',
    ],

    'basic_agree': [
        'y',
        'yes',
        'ok',
        'k',
        'gg',
        'done',
        'sahi',
        'yeah',
        'yee',
        'yep',
        'fine',
        'aight',
        'cool',
        'kull',
        'suii',
        'coolz',
    ],

    'basic_deny': [
        'n',
        'no',
        'nope',
        'nah',
        'nahi',
    ],

    'basic_challenge': [
        'bot',
        'human',
        'hooman',
        'god',
    ],

    'basic_bye': [
        'bye',
        'byee',
        'goodbye',
    ],

    'reminder': [
        'set',
        'remind',
        'reminder',
    ],

    'stock_display': [
        'show',
        'display'
    ]
}