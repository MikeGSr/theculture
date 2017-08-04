import boto3


rekog = boto3.client('rekognition')

repsonse = rekog.recognize_celebrities(
   Image={
      
       'S3Object': {
           'Bucket': 'theculture2',
           'Name': 'dwash.jpg'
           
       }
   }
)

print(repsonse)
