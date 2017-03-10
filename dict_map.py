def dict_map(func, obj, deep=False):
    keys = obj.keys()
    values = obj.values()
    func = func_wrapper(func)
    func = deep_func(func) if deep else func
    maping = map(func, values)
    return dict(zip(keys, maping))

def deep_func(func):
    def aux_func(value):
        isDict = type(value) is dict
        return dict_map(func, value, True) if isDict else func(value)
    return aux_func

def func_wrapper(func):
    def aux_func(value):
        try:
            return func(value)
        except Exception:
            return value
    return aux_func
