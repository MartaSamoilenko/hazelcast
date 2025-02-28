import hazelcast
import time
import sys

def main(consumer_name):
    client = hazelcast.HazelcastClient(
        cluster_members=[
            "127.0.0.1:5701",
            "127.0.0.1:5702",
            "127.0.0.1:5703"
        ],
        cluster_name="hello-world"
    )

    queue = client.get_queue("my-bounded-queue").blocking()

    while True:
        item = queue.take()
        print(f"{consumer_name} got value {item}")
        time.sleep(0.2) 

if __name__ == "__main__":
    consumer_name = sys.argv[1] if len(sys.argv) > 1 else "Consumer1"
    main(consumer_name)
