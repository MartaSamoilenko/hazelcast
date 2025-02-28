# hazelcast

- ### start the project
    ```
    docker-compose up -d
    ```
    check the containers
    ```
    docker ps -a
    ```
    ![alt text](image-1.png)

Observing the cluster in Management Center.
![alt text](image.png)

No Locks vs Pesimistic Lock vs Optimistic Lock

![](image-2.png)
![](image-7.png)
---
![](image-3.png)
![](image-5.png)
---
![](image-4.png)
![alt text](image-6.png)

## Running the Queue
```
python queue_consumer.py ConsumerA
```
```
python queue_consumer.py ConsumerB
```
```
python queue_producer.py
```

### Result:

![alt text](image-8.png)
![alt text](image-9.png)
![alt text](image-10.png)

