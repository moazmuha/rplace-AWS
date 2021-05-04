import boto3
import time
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('points')
try:
    create_time = table.creation_date_time
    now = datetime.now()
    last_update = now - timedelta(seconds=10)

    now = now.strftime('%FT%T+13:00')
    last_update = last_update.strftime('%FT%T+13:00')

    fe = Key('timestamp').between(last_update,now);
    response = table.scan(
                    FilterExpression=fe
    )

    items = response['Items']
    return_str = ''
    for item in items:
        return_str += str(item['x']) + "," + str(item["y"]) + "," + str(item['r']) + "," + str(item["g"]) + "," + str(item['b']) + ","
    return_str = return_str[0:len(return_str)-1]
    print(return_str)
except:
    print("error")