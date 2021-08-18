############------------ IMPORTS ------------############
from memory_profiler import profile


############------------ FUNCTION(S) ------------############
@profile
def this_is_a_function():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    pass