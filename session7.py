##################################################################################
def fifty_docstring(fn):

    '''
    This function checks if a passed function has a doc string or not and then it checks 
    if the doc string has 50 characters or not  
    '''
    num = 0
    def check_docstring():
        nonlocal num
        s = ""
        num = len(s.join((fn.__doc__).split()))
        if num > 50:
            return True
        else:
            return False
    return check_docstring()


##################################################################################
def outer_fibo():

    ''' 
    This function gives the next number 
    in the fibonacci series.
    '''

    n = 0
    def nextFibonacci(a,b):
        nonlocal n
        if b == 0:
            b = 1
            return a+b
        else:
            n = a+b
            a = b
            b = n
        return n
    return nextFibonacci


######################################################################################
counters = dict()
def counter(fn):

    ''' 
    add, mul and div 
    '''

    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        #print(f'{fn.__name__} has been called {cnt} times')
        counters[fn.__name__] = cnt
        return fn(*args,**kwargs)
    return inner

def add(a,b):
    return a+b, counters

def mul(a,b):
    return a*b, counters

def div(a,b):
    return a/b, counters


#############################################################################################
add_counter = dict()
mul_counter = dict()
div_counter = dict()

def seperate_counter(fn):

    ''' 
    saves the count of each operation in a seperate dictionary 
    '''

    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        if fn.__name__ == "add":
            add_counter[fn.__name__] = cnt
        elif fn.__name__ == "mul":
            mul_counter[fn.__name__] = cnt
        else:
            div_counter[fn.__name__] = cnt
        return fn(*args,**kwargs)
    return inner

def add(a,b):
    return a+b, add_counter

def mul(a,b):
    return a*b, mul_counter

def div(a,b):
    return a/b, div_counter

#########################################################################################