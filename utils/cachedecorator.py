def cached(function):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result 
            return result

    return wrapper