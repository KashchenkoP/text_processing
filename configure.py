import selectors
import socket
import json

mongo_connection_url = 'mongodb://192.168.100.115:27310'

kafka_producer = {
    'bootstrap_servers': ['localhost:9092'],
    'client_id': 'twitter-text_processing-python-producer-#',
    'key_serializer': str.encode,
    'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    'acks': 1,
    'compression_type': None,
    'retries': 0,
    'batch_size': 16384,
    'linger_ms': 0,
    'partitioner': None,
    'buffer_memory': 33554432,
    'max_block_ms': 60000,
    'max_request_size': 1048576,
    'metadata_max_age_ms': 300000,
    'retry_backoff_ms': 100,
    'request_timeout_ms': 30000,
    'receive_buffer_bytes': 32768,
    'send_buffer_bytes': 131072,
    'socket_options': [(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)],
    'reconnect_backoff_ms': 50,
    #'reconnect_backoff_max_ms': 1000,
    'max_in_flight_requests_per_connection': 5,
    'security_protocol': 'PLAINTEXT',
    'ssl_context': None,
    'ssl_check_hostname': True,
    'ssl_cafile': None,
    'ssl_certfile': None,
    'ssl_keyfile': None,
    'ssl_password': None,
    'ssl_crlfile': None,
    'api_version': None,
    'api_version_auto_timeout_ms': 20,
    'metric_reporters': [],
    'metrics_num_samples': 2,
    'metrics_sample_window_ms': 30000,
    'selector': selectors.DefaultSelector,
    'sasl_mechanism': None,
    'sasl_plain_username': None,
    'sasl_plain_password': None
    #'sasl_kerberos_service_name': 'text_processing'
}