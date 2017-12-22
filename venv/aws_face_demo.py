import boto3

client = boto3.client('rekognition',
                      aws_access_key_id='AKIAJUDW5BIKGCZ4FMVA',
                      aws_secret_access_key='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',
                      region_name='us-east-1'
                      )

p = open('./2016090911081720022.jpg','rb')

response = client.detect_faces(Image = {
             'Bytes':bytearray(p.read())
             },
             Attributes=[
                 'ALL'
                 ]
             )
p.close()
print(response)