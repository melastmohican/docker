import boto3

# Create SQS client
sqs = boto3.client('sqs', aws_access_key_id=None, aws_secret_access_key=None, endpoint_url='http://localhost:9324')

queue_url = 'http://localhost:9324/queue/queue0'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=10,
    WaitTimeSeconds=20
)

if response.get('Messages') is not None:
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)
else:
    print('No messages received.')