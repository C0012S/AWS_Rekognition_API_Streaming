# Create Stream Processor
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_stream_processor

import boto3
import csv

with open('Srek_credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name="us-east-1")

response = client.create_stream_processor(
    Input={
        'KinesisVideoStream': {
            'Arn': ''
        }
    },
    Output={
        'KinesisDataStream': {
            'Arn': ''
        }
    },
    Name='myStreamProcessor',
    Settings={
        'FaceSearch': {
            'CollectionId': 'StreamingCollection',
            'FaceMatchThreshold': 85.5
        }
    },
    RoleArn='',
    Tags={
        'Role': 'Singer'
    }
)

print(response)
