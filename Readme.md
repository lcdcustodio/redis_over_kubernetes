Redis over Kubernetes
===========

Redis cluster with redundancy on Kubernetes using StatefulSets, a headless service, and interact with it using Flask App for read and write operations.

------------

1- High Level Design
===========================


![Alt text](/pictures/hld.png "Solution Architecture")


# StatefulSets

StatefulSet is the workload API object used to manage stateful applications.

Manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods.

Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling.

If you want to use storage volumes to provide persistence for your workload, you can use a StatefulSet as part of the solution. Although individual Pods in a StatefulSet are susceptible to failure, the persistent Pod identifiers make it easier to match existing volumes to the new Pods that replace any that have failed.


# What is a Headless Service?

When there is no need of load balancing or single-service IP addresses.We create a headless service which is used for creating a service grouping. That does not allocate an IP address or forward traffic.So you can do this by explicitly setting ClusterIP to “None” in the mainfest file, which means no cluster IP is allocated.

For example, if you host MongoDB on a single pod. And you need a service definition on top of it for taking care of the pod restart.And also for acquiring a new IP address. But you don’t want any load balancing or routing. You just need the service to patch the request to the back-end pod. So then you use Headless Service since it does not have an IP.

Kubernetes allows clients to discover pod IPs through DNS lookups. Usually, when you perform a DNS lookup for a service, the DNS server returns a single IP which is the service’s cluster IP. But if you don’t need the cluster IP for your service, you can set ClusterIP to None , then the DNS server will return the individual pod IPs instead of the service IP.Then client can connect to any of them.

# Use Cases of Headless Service

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
    kubectl apply -f redis-statefulset.yaml
```

Once command above is finished, let's check if Redis cluster is up and running through the following  command:

```
    kubectl get statefulset
```

![Alt text](/pictures/out1.png "Solution Architecture")


Next step is create a headless service for the Redis StatefulSet through following command:

```
    kubectl apply -f redis-headless-service.yaml
```

The outcome from command line below can be demonstrated through following command: 

```
    kubectl get service redis-headless
```
