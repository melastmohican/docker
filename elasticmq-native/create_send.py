import boto3
    
VISIBILITY_TIMEOUT = "10800"  # seconds
client = boto3.resource(
    "sqs",
    endpoint_url="http://localhost:9324",
    region_name="DOESNOTMATTER",
    aws_secret_access_key="DOESNOTMATTER",
    aws_access_key_id="DOESNOTMATTER",
    use_ssl=False,
)
response = client.create_queue(
    QueueName="queue1", Attributes={"VisibilityTimeout": VISIBILITY_TIMEOUT}
)

# using boto3.client

sqs = boto3.client(
    "sqs",
    region_name="DOESNOTMATTER",
    endpoint_url="http://localhost:9324/queue/queue1",
    aws_access_key_id="DOESNOTMATTER",
    aws_secret_access_key="DOESNOTMATTER",
)
response = sqs.send_message(
    QueueUrl="http://localhost:9324/queue/queue1",
    MessageAttributes={
        "message_type": {"DataType": "String", "StringValue": "message_type"}
    },
    MessageBody=str("body")
)

# using boto3.resource

client = boto3.resource(
    'sqs',
    endpoint_url="http://localhost:9324",
    region_name="DOESNOTMATTER",
    aws_secret_access_key='DOESNOTMATTER',
    aws_access_key_id='DOESNOTMATTER',
    use_ssl=False
)
queue = client.get_queue_by_name(QueueName='queue1')
response = queue.send_message(
    MessageAttributes={
        "message_type": {"DataType": "String", "StringValue": "message_type"}
    },
    MessageBody=str("body")
)
response_code = response["ResponseMetadata"]["HTTPStatusCode"]
if not (response_code >= 200 and response_code < 300):
    raise Exception(f"Non 200 response after sending message {response_code}")
print(str(response["MessageId"]))