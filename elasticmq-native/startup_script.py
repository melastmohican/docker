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