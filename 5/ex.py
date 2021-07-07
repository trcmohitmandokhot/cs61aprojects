# Function Composition Example 61A Fall 2013 Lecture 5 Video 7
def square(x):
    return x*x

def triple(x):
    return 3*x

def combo1(f,g):
    def h(x):
        return f(g(x))
    return h
# Call function 
# square_then_triple = combo1(triple,square)
# result = square_then_triple(3)
# 27
