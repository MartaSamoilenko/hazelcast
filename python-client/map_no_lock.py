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

    my_map = client.get_map("my-distributed-map").blocking()
    
    my_map.put_if_absent("key", 0)

    start_time = time.time()
    for _ in range(10_000):
        val = my_map.get("key")
        val += 1
        my_map.put("key", val)
    end_time = time.time()

    print(f"[No Lock] Done. Elapsed: {end_time - start_time:.2f} seconds.")
    client.shutdown()

if __name__ == "__main__":
    main()
