Entercloud Engine Messenger 
===

Migration included - legacy Kafka 7 cluster into a dockerized Kafka 8.

Why?
---


* No dependency on an external componet hosts, or linking to another service. 
* Entercloud Engine Messenger nodes are configured to work together out of the box

Run
---
#update the docker image here at the update 
```bash
docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=`docker-machine ip \`docker-machine active\`` --env ADVERTISED_PORT=9092 spotify/kafka
```


# 
```bash
export KAFKA=`docker-machine ip \`docker-machine active\``:9092
kafka-console-producer.sh --broker-list $KAFKA --topic message_test
```

```bash
export ZOOKEEPER=`docker-machine ip \`docker-machine active\``:2181
kafka-console-consumer.sh --zookeeper $ZOOKEEPER --topic message_test
```

Running the networking system
-----------------



#update the docker source dockerfile 
Take the same parameters as the spotify/kafka image with some new ones:
 * `CONSUMER_THREADS` - the number of threads to consume the source kafka 7 with
 * `TOPICS` - whitelist of topics to mirror
 * `ZK_CONNECT` - the zookeeper connect string of the source kafka 7
 * `GROUP_ID` - the group.id to use when consuming from kafka 7



# update dockerfile source  , topics env , zk_connect, grpup-id
```bash
docker run -p 2181:2181 -p 9092:9092 \
    --env ADVERTISED_HOST=`boot2docker ip` \
    --env ADVERTISED_PORT=9092 \
    --env CONSUMER_THREADS=1 \
    --env TOPICS=my-topic,some-other-topic \
    --env ZK_CONNECT=kafka7zookeeper:2181/root/path \
    --env GROUP_ID=mymirror \
    spotify/kafkaproxy
```

In the box  - update box settings 
---
* **Entercloud engine messenger**

  The LXC started from specific directory

* **spotify/kafkaproxy**

  The docker image with Kafka, Zookeeper and a Kafka 7 proxy that can be
  configured with a set of topics to mirror.

Public Builds
---

https://registry.hub.docker.com/u/spotify/kafka/

https://registry.hub.docker.com/u/spotify/kafkaproxy/

Build from Source
---

    docker build -t spotify/kafka kafka/
    docker build -t spotify/kafkaproxy kafkaproxy/

Todo
---

* Not particularily optimzed for startup time.
* Better docs

