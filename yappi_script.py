############------------ DOCUMENTATION ------------############
# https://pypi.org/project/yappi/

############------------ IMPORTS ------------############
import yappi


############------------ FUNCTION(S) ------------############
def this_is_a_function():
    for i in range(1000000000):  # do something CPU heavy
        pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    yappi.set_clock_type("cpu") 
    # Use set_clock_type("wall") for wall time
    yappi.start()
    this_is_a_function()
    yappi.get_func_stats().print_all()
    # yappi.get_thread_stats().print_all()

    '''
    Clock type: CPU
    Ordered by: totaltime, desc

    name                                  ncall  tsub      ttot      tavg      
    ..ppi_script.py:9 this_is_a_function  1      18.41965  18.41965  18.41965

    '''