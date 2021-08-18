############------------ DOCUMENTATION ------------############
# https://pypi.org/project/yappi/

############------------ IMPORTS ------------############
import yappi


############------------ FUNCTION(S) ------------############
def a():
    for _ in range(10000000):  # do something CPU heavy
        pass

yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()
a()

yappi.get_func_stats().print_all()
# yappi.get_thread_stats().print_all()

'''
Clock type: CPU
Ordered by: totaltime, desc

name                                  ncall  tsub      ttot      tavg      
..ts/performance/yappi_script.py:9 a  1      0.185855  0.185855  0.185855

'''