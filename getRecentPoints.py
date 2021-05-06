import boto3
import time
from datetime import datetime, timedelta
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('points')

try:
    create_time = table.creation_date_time
    # get current time
    now = datetime.now()
    # time 6 seconds from now
    last_update = now - timedelta(seconds=6)

    now = now.strftime('%FT%T+13:00')
    last_update = last_update.strftime('%FT%T+13:00')

    # query points table for points added within the last 6 seconds
    fe = Key('timestamp').between(last_update,now);
    response = table.scan(
                    FilterExpression=fe
    )

    items = response['Items']
    # return string of all points
    return_str = ''
    for item in items:
        point = str(item['point'])
        x = point.split(',')[0]
        y = point.split(',')[1]
        rgb = str(item['rgb'])
        r = rgb.split(',')[0]
        g = rgb.split(',')[1]
        b = rgb.split(',')[2]
        return_str += x + "," + y + "," + r + "," + g + "," + b + ","
    return_str = return_str[0:len(return_str)-1]
    print(return_str)
except:
    print("error")