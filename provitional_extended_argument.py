# variable length positional extended arguments

import time

charac = ["a", "b", "c", "d", "e"]
print(charac)
print(*charac)

def custom_print(*objects):
    print(f"Objects is type {type(objects)}: {objects}")
    #can be iterated as per need

custom_print("one", "two")

class Logger:
    '''write data to a database everytime a logger event occurs'''

    def __init__(self, table):
        self.table = table
        self.num_events = 0

    def write(self, message):
        print(f"{time.ctime()}: {self.num_events}: {self.table}:: {message}")

    def __call__(self, message, *messages): # implements *args specific name
        # self.write(message)
        # self.num_events +=1
        for msg in [message] + list(messages):
            self.num_events +=1
            self.write(msg)


logger = Logger("log_table")
logger("connection aborted")
logger("Checking data witten")

print("first", "second", "third")
logger("1st", "2nd") # error prev works after change
