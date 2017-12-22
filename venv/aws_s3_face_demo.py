import boto3


BUCKET = 'awsvison20171222'

KEY = 'face.png'

def detect_labels(bucket, key, max_labels=10, min_confidence=90):
    client = boto3.client('rekognition',
                          aws_access_key_id='AKIAJ23WDM7P2RXKWAXA',
                          aws_secret_access_key='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',
                          region_name='us-east-1'
                          )


    response = client.detect_labels(Image = {
             'S3Object':{'Bucket':bucket,
                          'Name':key
                         }
             },
             MaxLabels = max_labels,
             MinConfidence = min_confidence
             )

    return response['Labels']

for label in detect_labels(BUCKET, KEY):
    print("{Name} - {Confidence}%".format(**label))