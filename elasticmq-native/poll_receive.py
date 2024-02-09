import boto3

VISIBILITY_TIMEOUT = "10800"  # seconds
# boto3.client    
sqs = boto3.client(
    "sqs",
    region_name="DOESNOTMATTER",
    endpoint_url="http://localhost:9324/queue/queue1",
    aws_access_key_id="DOESNOTMATTER",
    aws_secret_access_key="DOESNOTMATTER",
)
response = sqs.receive_message(
    QueueUrl="http://localhost:9324/queue/queue1",
    MaxNumberOfMessages=1,
    MessageAttributeNames=["message_type"],
    VisibilityTimeout=int(VISIBILITY_TIMEOUT),  # 0 - 43200
    WaitTimeSeconds=0,  # 0 - 20 (delay of message retrieval)
)
message = response.get("Messages")
print(message)

# boto3.resource
client = boto3.resource(
    'sqs',
    endpoint_url="http://localhost:9324",
    region_name="DOESNOTMATTER",
    aws_secret_access_key='DOESNOTMATTER',
    aws_access_key_id='DOESNOTMATTER',
    use_ssl=False
)
queue = client.get_queue_by_name(QueueName='queue1')
response = queue.receive_messages(
    MaxNumberOfMessages=1,
    MessageAttributeNames=["message_type"],
    VisibilityTimeout=int(VISIBILITY_TIMEOUT),
    WaitTimeSeconds=0
)
message = response.pop()
# ^ NOTE This message object is very different then the message object below
print(message)
