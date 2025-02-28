# hazelcast

- ### start the project
    ```
    docker-compose up -d
    ```
    check the containers
    ```
    docker ps -a
    ```
    ![alt text](images/image-1.png)

Observing the cluster in Management Center.
![alt text](images/image.png)

No Locks vs Pesimistic Lock vs Optimistic Lock

![](images/image-2.png)
![](images/image-7.png)
---
![](images/image-3.png)
![](images/image-5.png)
---
![](images/image-4.png)
![](images/image-6.png)

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

![](images/image-8.png)
![](images/image-9.png)
![](images/image-10.png)

