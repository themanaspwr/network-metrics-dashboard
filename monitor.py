import time
import random
import queue  # Import the queue module

def monitor_network(data_queue):  # Pass the queue as an argument
    while True:
        packet_loss = random.uniform(0, 5)
        latency = random.uniform(10, 25)
        packet_gain = random.uniform(20, 40)

        data_queue.put({  # Put the data into the queue
            'packetLoss': packet_loss,
            'latency': latency,
            'packetGain': packet_gain,
            'time': time.time()
        })

        time.sleep(1)

if __name__ == "__main__":
    data_queue = queue.Queue()  # Create a queue
    monitor_network(data_queue) #pass the queue