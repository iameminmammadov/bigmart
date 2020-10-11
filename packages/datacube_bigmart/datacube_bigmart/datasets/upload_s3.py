import boto3
client_s3 = boto3.resource('s3')
client_s3.meta.client.upload_file('Train.csv', 'bigmart-dataset', 'Train.csv')
client_s3.meta.client.upload_file('Test.csv', 'bigmart-dataset', 'Test.csv')

