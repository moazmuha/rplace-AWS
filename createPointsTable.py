import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.

table = dynamodb.create_table(
    TableName='points',
    KeySchema=[
        {
            'AttributeName': 'point',
            'KeyType': 'HASH'  
        },
        {
            'AttributeName': 'timestamp',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'point',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'timestamp',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
# Wait until the table exists.
print("please wait...")
table.meta.client.get_waiter('table_exists').wait(TableName='points')

# Print out some data about the table.
print("table created succesfully")