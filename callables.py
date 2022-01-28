# callables

# object that implements the dunder call method
# objects that have a non-null tp_call struct member in its C-level object
# test with callable()
# functions, lambdas, classes, methods are all callables
# objects | class instance | implementing __call__ becomes callables
# usecases ::
# - Standard API
# - Seperation of concerns/ single responsibility
# - container for storing complex state relevant for a function's call

from pprint import pprint
import time

def sum_numbers(a,b):
    return a+b

pprint(dir(sum_numbers))
print(sum_numbers.__call__(3,4))

# print(list(1,2,3,4))
print(callable(list)) # true
print(dir(list)) # no __call__ PyCallable_Check -> check for a non null obj returns True False


print(callable(lambda a, b: a+b))


for fn in [list, set, lambda x: f"{time.ctime()} {x}"]: #all callable
    print(fn("eh"))


class Logger:
    '''write data to a database everytime a logger event occurs'''

    def __init__(self, table):
        self.table = table
        self.num_events = 0

    def write(self, message):
        print(f"{time.ctime()}: {self.num_events}: {self.table}:: {message}")

    def __call__(self, message):
        self.num_events +=1
        self.write(message)


logger = Logger("log_table")
logger("connection aborted")
logger("Checking data witten")
