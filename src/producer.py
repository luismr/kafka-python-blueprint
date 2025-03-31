from kafka import KafkaProducer

class KafkaProducerBlueprint:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers

    def at_most_once_producer(self):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                 acks=0)
        # Implement at-most-once logic here

    def at_least_once_producer(self):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                 acks='all',
                                 retries=3)
        # Implement at-least-once logic here

    def exactly_once_producer(self):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                 acks='all',
                                 enable_idempotence=True)
        # Implement exactly-once logic here

if __name__ == "__main__":
    bootstrap_servers = 'localhost:9092'
    producer_blueprint = KafkaProducerBlueprint(bootstrap_servers)
    # Call the desired producer method here 