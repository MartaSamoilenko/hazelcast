import hazelcast
import time

def main():
    client = hazelcast.HazelcastClient(
        cluster_members=[
            "127.0.0.1:5701",
            "127.0.0.1:5702",
            "127.0.0.1:5703"
        ],
        cluster_name="hello-world"
    )

    queue = client.get_queue("my-bounded-queue").blocking()

    for i in range(1, 101):
        print(f"Producer: putting {i}")
        queue.put(i)
        time.sleep(0.1)

    print("Producer done.")
    client.shutdown()

if __name__ == "__main__":
    main()
