import boto3


BUCKET = 'awsvison20171222'

KEY = 'face.png'
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence", "AgeRange")

def detect_faces(bucket, key,attributes=['ALL']):
    client = boto3.client('rekognition',
                          aws_access_key_id='AKIAJ23WDM7P2RXKWAXA',
                          aws_secret_access_key='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',
                          region_name='us-east-1'
                          )


    response = client.detect_faces(Image = {
             'S3Object':{'Bucket':bucket,
                          'Name':key
                         }
             },
            Attributes=attributes,
             )

    return response['FaceDetails']

for face in detect_faces(BUCKET, KEY):
	print("Face ({Confidence}%)".format(**face))
	# emotions
	for emotion in face['Emotions']:
		print("  {Type} : {Confidence}%".format(**emotion))
	# quality
	for quality, value in face['Quality'].items():
		print("  {quality} : {value}".format(quality=quality, value=value))
	# facial features
	for feature, data in face.items():


            if feature not in FEATURES_BLACKLIST:
                #print("feature=", feature, "data=", data)
                print ("{feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data))

#https://gist.github.com/alexcasalboni/0f21a1889f09760f8981b643326730ff
#http://legacy.python.org/dev/peps/pep-0469/
