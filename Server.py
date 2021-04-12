# This class is to collect messages sent by Clients and generate report about QPS with Queue as IPC
# Helper Functions:
# 1. Collect()
# 2. Summary()

def Summary():
    """[summary]
    It is undetermined whether save records in file or plot lively. It seems former is better.
    """

def Collect():
    """[summary]
    Keep collecting record from client processes,
    then save them in file.
    """

from multiprocessing.connection import Listener
add = ('localhost', 6001)

if __name__ == "__main__":
    with Listener(add) as listener:
        # Demo of collecting record
        print("Start server:")
        while True:
            with listener.accept() as conn:
                    print(conn.recv())
    