import boto3, sys
import time
from datetime import datetime, timedelta

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Get the points table
table = dynamodb.Table('points')

# Ensure table exists
try:
    create_time = table.creation_date_time
except:
    print("points table DNE")

# place new point with timestamp
try:
    table.put_item(
    Item={
            'timestamp': datetime.now().strftime('%FT%T+13:00'),
            'x': sys.argv[1],
            'y': sys.argv[2],
            'r': sys.argv[3],
            'g': sys.argv[4],
            'b': sys.argv[5]
        }
    )
except:
    print("putItems failed")
