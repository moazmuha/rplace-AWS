import boto3

# Get the service resource.
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='points',
    KeySchema=[
        {
            'AttributeName': 'x',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'y',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'x',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'y',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='points')

# Print out some data about the table.
print("table created succesfully")
