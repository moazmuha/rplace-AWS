import boto3, sys

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('points')
try:
    create_time = table.creation_date_time
except:
    print("error")

try:
    point = table.get_item(
        Key={
            'x': sys.argv[1],
            'y': sys.argv[2]
        }
    )
    item = point['Item']
    return_str = str(item['x']) + "," + str(item["y"]) + "," + str(item['r']) + "," + str(item["g"]) + "," + str(item['b'])
    print(return_str) 
except:
    print("error")
