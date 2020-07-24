from Input import params

# Future Work: Option to set default value

# TIME COMPLEXITY: O(N) IF LINEAR SEARCH
# O(1) IF USING HASH TABLE

def param_handler(param_type, called_by=None):
    if called_by is None:
        param_object = getattr(params, param_type)()
    else:
        param_object = getattr(params, param_type)(called_by)
    return param_object
