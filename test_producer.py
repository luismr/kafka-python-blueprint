import pytest
from unittest.mock import patch, MagicMock
from producer import KafkaProducerBlueprint

@patch('producer.KafkaProducer')
def test_at_most_once_producer(mock_kafka_producer):
    mock_producer_instance = MagicMock()
    mock_kafka_producer.return_value = mock_producer_instance
    producer_blueprint = KafkaProducerBlueprint('localhost:9092')
    producer_blueprint.at_most_once_producer()
    mock_kafka_producer.assert_called_with(bootstrap_servers='localhost:9092', acks=0)

@patch('producer.KafkaProducer')
def test_at_least_once_producer(mock_kafka_producer):
    mock_producer_instance = MagicMock()
    mock_kafka_producer.return_value = mock_producer_instance
    producer_blueprint = KafkaProducerBlueprint('localhost:9092')
    producer_blueprint.at_least_once_producer()
    mock_kafka_producer.assert_called_with(bootstrap_servers='localhost:9092', acks='all', retries=3)

@patch('producer.KafkaProducer')
def test_exactly_once_producer(mock_kafka_producer):
    mock_producer_instance = MagicMock()
    mock_kafka_producer.return_value = mock_producer_instance
    producer_blueprint = KafkaProducerBlueprint('localhost:9092')
    producer_blueprint.exactly_once_producer()
    mock_kafka_producer.assert_called_with(bootstrap_servers='localhost:9092', acks='all', enable_idempotence=True) 