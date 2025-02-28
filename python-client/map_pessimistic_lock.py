import hazelcast
import time

LOCK_KEY = "my_lock_key"
TARGET_KEY = "key"          

def acquire_lock(my_map):
    """Busy-wait (spin) until we set my_lock_key from 'unlocked' -> 'locked'."""
    while True:
        current_state = my_map.get(LOCK_KEY)
        if current_state is None:
            my_map.put_if_absent(LOCK_KEY, "unlocked")
            current_state = "unlocked"

        if current_state == "unlocked":
            if my_map.replace_if_same(LOCK_KEY, "unlocked", "locked"):
                break
        time.sleep(0.001)

def release_lock(my_map):
    """Set my_lock_key from 'locked' -> 'unlocked'."""
    my_map.replace_if_same(LOCK_KEY, "locked", "unlocked")


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
    
    my_map.put(TARGET_KEY, 0)
    
    my_map.put_if_absent(LOCK_KEY, "unlocked")

    start_time = time.time()
    for _ in range(10_000):
        acquire_lock(my_map)
        try:
            val = my_map.get(TARGET_KEY)
            val += 1
            my_map.put(TARGET_KEY, val)
        finally:
            release_lock(my_map)
    end_time = time.time()

    print(f"Pessimistic-like (manual) lock done in {end_time - start_time:.2f} s.")
    client.shutdown()

if __name__ == "__main__":
    main()
