import functools

class MyClass:
    "Demostration class for functools"

    def __call__(self,e,f=6):
        "Docstring for myclass .__call__"
        print('Called object with ',(self,e,f))

def show_details(name,f):
    "Show details of callable object."
    print('{} : '.format(name))
    print('object:',f)
    print('__name__:',end = ' ' )
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('__doc__',repr(f.__doc__))

o = MyClass()

show_details('instance',o)
o('e goes here')
print()

p = functools.partial(o,e='default for e',f=8)
functools.update_wrapper(p,o)
show_details('instance wrapper',p)
p()
