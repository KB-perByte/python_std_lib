# day - 2
# variable length positional extended arguments - extended

import time

class Logger:
    '''write data to a database everytime a logger event occurs'''

    def __init__(self, table):
        self.table = table
        self.num_events = 0

    def write(self, message, show_counts: bool):
        print(f"{time.ctime()}: {self.num_events if show_counts else ''}: {self.table}:: {message}")

    def __call__(self, message, *messages, **kwargs): # implements *args specific name
        # self.write(message)
        # self.num_events +=1
        show_counts = kwargs.get("show_counts", False)
        for msg in [message] + list(messages):
            self.num_events +=1
            self.write(msg, show_counts)


logger = Logger("log_table")
logger("connection aborted")
logger("Checking data witten")

print("first", "second", "third")
logger("1st", "2nd") # error prev works after change
