from IPython.display import display
from ipywidgets.widgets.interaction import interactive

def f(a, b):
    display(a + b)
    return a+b

w = interactive(f, a=10, b=20)
print(type(w))

display(w)
