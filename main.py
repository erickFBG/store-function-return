output = {}
def memorize(func):
    '''
    This decorator stores the return values of a function in a dictionary
    called memo, where the keys of the dictionary correspond to the 
    arguments of the function, and the value is the return result of the 
    function. The first time the function is called, the decorator checks
    if the input is already in the memo. If it's not, it executes the 
    function and stores its return value in the memo. Otherwise,
    it returns the value stored in the memo.

    A variable named output was created to store the data of the class,
    where it will create a dictionary with a list of data, and the key 
    is the name of the function that was executed.
    '''
    memo = {}
    def helper(*args):
        if args not in memo:
            fname = func.__name__
            memo[args] = func(*args)
            if fname in output:
                output[fname].append(memo[args])
            else:
                output[fname] = [memo[args]]
        return memo[args]
    return helper