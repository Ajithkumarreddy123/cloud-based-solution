import json
import boto3
from urllib.parse import unquote_plus
from datetime import datetime
from decimal import Decimal  

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('imageDetails')  # Make sure this matches your table name

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])

        try:
            # Call Rekognition to detect labels
            response = rekognition.detect_labels(
                Image={'S3Object': {'Bucket': bucket, 'Name': key}},
                MaxLabels=10,
                MinConfidence=75
            )

            # Extract label names and convert confidence to Decimal
            labels = []
            confidence_scores = {}
            for label in response['Labels']:
                labels.append(label['Name'])
                confidence_scores[label['Name']] = Decimal(str(round(label['Confidence'], 2)))

            # Store in DynamoDB
            table.put_item(
                Item={
                    'imageName': key,
                    'Labels': labels,
                    'ConfidenceScores': confidence_scores,
                    'Timestamp': datetime.utcnow().isoformat() + 'Z'
                }
            )

            print(f"✅ Successfully processed and saved: {key}")
        
        except Exception as e:
            print(f"❌ Error processing {key}: {e}")
            raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Rekognition and DynamoDB storage completed.')
    }
