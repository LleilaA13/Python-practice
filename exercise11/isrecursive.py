
from __future__ import print_function
import types

DEBUG=2     # Detailed reports
DEBUG=1     # Show the function calls only
DEBUG=0     # None

class RecursionDetectedError(Exception):
    pass

def norecurse(func):
    '''Decorator that throws an exception if the function is recursive'''
    func.called = False
    def f(*args, **kwargs):
        if DEBUG: print('Calling', func.__name__, func.called, *args)
        if func.called:
            print("Recursion detected in " + func.__name__)
            func.called = False  # If you are going to continue the execution…
            raise RecursionDetectedError
        func.called = True
        result = func(*args, **kwargs)
        func.called = False
        if DEBUG: print('returning', result, 'from', func.__name__)
        return result
    return f

def isRecursiveP(func):
    '''Decorator that sets the function attribute "recursive" as True
       if recursion is detected during the execution.'''
    func.called    = False
    func.recursive = False
    def f(*args, **kwargs):
        if func.called:
            # print "Recursion detected!"
            func.recursive = True
        func.called = True
        result = func(*args, **kwargs)
        func.called = False
        return result
    return f

def decorate_function(f, dec):
    '''Applies the decorator (dec) to function f and stores the previous,
       non-decorated version of f'''
    newf = dec(f)
    newf.oldf = f
    return newf

def undecorate_function(f):
    '''Removes the decorator (dec attribute) from function f'''
    return getattr(f, 'oldf', f)

# TODO Use the decorator module

def decorate_module(module, decorator=norecurse):
    '''Decorates functions and class methods defined in the module
       (by default, with decorator=norecurse)'''
    for f in dir(module):
        ff = getattr(module,f)
        if getattr(ff, '__module__', None) == module.__name__:
            if isinstance(ff, types.FunctionType):
                if DEBUG>1: print('decorating', f)
                ff = decorate_function(ff,decorator)
                setattr(module,f,ff)
            elif isinstance(ff, type):
                if DEBUG>1: print('decorating', f, 'methods')
                for m in dir(ff):
                    if DEBUG>1: print('   decorating',m)
                    mm = getattr(ff, m)
                    if isinstance(mm, types.FunctionType):
                        mm = decorate_function(mm, decorator)
                        setattr(ff, m, mm)

def undecorate_module(module):
    '''Removes the previoulsy added decorations'''
    for f in dir(module):
        ff = getattr(module,f)
        if isinstance(ff, types.FunctionType):
            if DEBUG>1: print('undecorating', f)
            ff = undecorate_function(ff)
            setattr(module,f,ff)
        elif isinstance(ff, type):
            if DEBUG>1: print('undecorating', f, 'methods')
            for m in dir(ff):
                if DEBUG>1: print('   undecorating',m)
                mm = getattr(ff, m)
                if isinstance(mm, types.FunctionType):
                    mm = undecorate_function(mm)
                    setattr(ff, m, mm)