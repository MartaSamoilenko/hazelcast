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
    # Reset
    my_map.put("key", 0)

    start = time.time()
    for _ in range(10_000):
        while True:
            old_val = my_map.get("key")
            new_val = old_val + 1
            if my_map.replace_if_same("key", old_val, new_val):
                break
    end = time.time()

    print(f"[Optimistic Lock] Done. Elapsed: {end - start:.2f} seconds.")
    client.shutdown()

if __name__ == "__main__":
    main()
