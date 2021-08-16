############------------ IMPORTS ------------############
import time
import timeit


############------------ FUNCTION(S) ------------############
def test_function():
    print("Test Function Starting")
    time.sleep(5)
    print("5 seconds have elapsed;  function ended.")

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print(timeit.Timer(test_function).timeit(number=1))
    # 5.000440147