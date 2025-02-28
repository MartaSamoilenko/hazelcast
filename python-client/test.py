import hazelcast
client = hazelcast.HazelcastClient(
    cluster_members=["127.0.0.1:5701", "127.0.0.1:5702", "127.0.0.1:5703"],
    cluster_name="hello-world"
)
m = client.get_map("my-distributed-map").blocking()
print("Final value:", m.get("key"))
client.shutdown()
