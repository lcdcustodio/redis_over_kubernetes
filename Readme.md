Redis over Kubernetes
===========

Redis cluster with redundancy on Kubernetes using StatefulSets, a headless service, and interact with it using Flask App for read and write operations.

------------

1- High Level Design
===========================


![Alt text](/pictures/hld.png "Solution Architecture")


### StatefulSets

StatefulSet is the workload API object used to manage stateful applications.

Manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods.

Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling.

If you want to use storage volumes to provide persistence for your workload, you can use a StatefulSet as part of the solution. Although individual Pods in a StatefulSet are susceptible to failure, the persistent Pod identifiers make it easier to match existing volumes to the new Pods that replace any that have failed.


### What is a Headless Service?

When there is no need of load balancing or single-service IP addresses.We create a headless service which is used for creating a service grouping. That does not allocate an IP address or forward traffic.So you can do this by explicitly setting ClusterIP to “None” in the mainfest file, which means no cluster IP is allocated.

For example, if you host MongoDB on a single pod. And you need a service definition on top of it for taking care of the pod restart.And also for acquiring a new IP address. But you don’t want any load balancing or routing. You just need the service to patch the request to the back-end pod. So then you use Headless Service since it does not have an IP.

Kubernetes allows clients to discover pod IPs through DNS lookups. Usually, when you perform a DNS lookup for a service, the DNS server returns a single IP which is the service’s cluster IP. But if you don’t need the cluster IP for your service, you can set ClusterIP to None , then the DNS server will return the individual pod IPs instead of the service IP.Then client can connect to any of them.

### Use Cases of Headless Service

- Create Stateful service
- Deploying RabbitMQ to Kubernetes requires a stateful set for RabbitMQ cluster nodes.
- Deployment of Relational databases


2- Installation
===========================

First of all, let’s clone the repository:

```
    git clone https://github.com/lcdcustodio/redis_over_kubernetes.git
    cd redis_over_kubernetes
```

Next step is to deploy Redis cluster on Kubernetes through following command:

```
    kubectl apply -f .\deploy\redis-statefulset.yaml
```

Once command above is finished, let's check if Redis cluster is up and running through the following  command:

```
    kubectl get statefulset
```

![Alt text](/pictures/out2_1.png "Solution Architecture")


Next step is create a headless service for the Redis StatefulSet through following command:

```
    kubectl apply -f .\deploy\redis-headless-service.yaml
```

The outcome from command line below can be demonstrated through following command: 

```
    kubectl get service redis-headless
```

> keep going Installation Topic with missing steps

3- Use Case: Redis as a caching system
===========================

### Step 1 - Connect to Redis

This demo is done through a python code and its popular Redis client library called redis-py:

![Alt text](/pictures/out3_1.png "Solution Architecture")


### Step 2 - Set and Get Cached Data

You can use Redis to store data in key-value pairs, where the key is a string and the value can be a string, number, or any other serialized data. Here's an example of how you can set and get cached data using Redis in Python:

![Alt text](/pictures/out3_2.png "Solution Architecture")

In this example, the key "my_key" is set with the value "my_value" in the Redis cache using the r.set() method. Later, the value associated with the key "my_key" is retrieved using the r.get() method and stored in the cached_data variable.


### Step 3 - Set Expiration for Cached Data

You can also set an expiration time for the data you store in Redis cache. This is useful if you want the data to be automatically removed from the cache after a certain period of time. Here's an example:


![Alt text](/pictures/out3_3.png "Solution Architecture")

In this example, the r.setex() method is used to set the data with a specified expiration time in seconds (in this case, 3600 seconds or 1 hour). The data will be automatically removed from the cache after the specified expiration time.

### Step 4 - Use Cached Data in Your Application

You can use the cached data in your application to improve performance by first checking if the data is available in Redis cache before fetching it from the original data source. Here's an example:

![Alt text](/pictures/out3_4.png "Solution Architecture")

In this example, the r.get() method is used to check if the data is available in Redis cache. If it's not available, the data is fetched from the original data source, and then it's stored in Redis cache using the r.set() method for future use.

