############------------ DOCUMENTATION ------------############
# Timeit utility: https://docs.python.org/3/library/timeit.html


############------------ IMPORTS ------------############
import time
import timeit


############------------ FUNCTION(S) ------------############
def this_is_a_function():
    time.sleep(5)


############------------ TEST(S) ------------############
def test_function_one():
    print( timeit.Timer(this_is_a_function).timeit(number=1) )


def test_function_two():
    print( timeit.Timer(this_is_a_function).timeit(number=2) )


def test_function_three():
    print( timeit.Timer(this_is_a_function).timeit(number=10) )

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    test_function_one()
    ## first run
    # 5.000404831999999

    ## second run
    # 5.003282615

    test_function_two()
    ## first run
    # 10.005152463999998

    ## second run
    # 10.006699564000002

    test_function_three()
    ## first run
    # 50.027108164

    ## second run
    # 50.016481751