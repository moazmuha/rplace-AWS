from boto3.dynamodb.conditions import Key, Attr
import boto3, sys

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Get the points table
table = dynamodb.Table('points')

#Grabb all the points in the table 
try:
    create_time = table.creation_date_time
    response = table.scan()
    items = response['Items']
    # return string of all points
    return_str = ''
    for item in items:
        return_str += str(item['x']) + "," + str(item["y"]) + "," + str(item['r']) + "," + str(item["g"]) + "," + str(item['b']) + ","
    return_str = return_str[0:len(return_str)-1]
    print(return_str)
except:
    print("error")


