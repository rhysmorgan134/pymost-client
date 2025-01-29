from src.PyMost import PiMost
import time
def recv_most_message(most_message):
    print("most message received")
    print(most_message)


data = PiMost(recv_most_message)
time.sleep(5)
data.force_switch()
while True:
    pass