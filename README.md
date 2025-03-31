# Python Kafka Producer Blueprint

This project demonstrates three different Kafka delivery modes using Python:

- At-most-once delivery
- At-least-once delivery
- Exactly-once delivery

## Cloning the Repository

To clone the repository, use the following command:

```bash
git clone git@github.com:luismr/kafka-python-blueprint.git
```

## Getting Started

### Prerequisites

- Python 3.8 or later
- Apache Kafka 3.x

### Setting Up the Virtual Environment

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

### Installing Dependencies

```bash
pip install -r requirements.txt
```

## Running the Producer

To run the producer, execute:

```bash
python producer.py
```

## Example Usage

Here's a simple example of how to use the Kafka producer:

```python
from src.producer import KafkaProducerBlueprint

# Initialize the producer blueprint with the Kafka broker address
producer_blueprint = KafkaProducerBlueprint(bootstrap_servers='localhost:9092')

# Use the at-most-once delivery mode
producer_blueprint.at_most_once_producer()

# Use the at-least-once delivery mode
producer_blueprint.at_least_once_producer()

# Use the exactly-once delivery mode
producer_blueprint.exactly_once_producer()
```

In this example, replace `'localhost:9092'` with the address of your Kafka broker. You can call any of the delivery mode methods to send messages with the desired delivery guarantees.

## Delivery Modes

### At-most-once Delivery

- Messages may be lost but will never be delivered more than once
- No acknowledgment required from brokers
- No retries on failure
- Best for scenarios where message loss is acceptable

### At-least-once Delivery

- Messages will be delivered at least once
- Acknowledgment required from all replicas
- Retries on failure
- May result in duplicate messages
- Best for scenarios where duplicates are acceptable but message loss is not

### Exactly-once Delivery

- Messages will be delivered exactly once
- Uses idempotent producer and transaction management
- No duplicates and no message loss
- Best for scenarios requiring strict message delivery guarantees

## Testing

Unit tests are included for each producer implementation using pytest and mocks.

To run tests:

```bash
pytest
```

## Kafka Cluster Setup

For setting up a Kafka cluster, refer to the [Kafka Cluster Setup Project](https://github.com/luismr/kafka-cluster-docker-compose).

## Contributing

To contribute to this project, please fork the repository and submit a pull request with your changes. We welcome contributions that improve the project or add new features.

## License

This project is licensed under the MIT License. 