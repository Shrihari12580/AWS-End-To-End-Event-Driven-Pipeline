# import json
# import boto3

# def lambda_handler(event, context):

#     print("event content : ",event )

#     glue = boto3.client('glue')
#     body = json.loads(event['Records'][0]['body'])
#     message_json = json.loads(body['Message'])

#     bucket_name = message_json["Records"][0]["s3"]["bucket"]["name"]
#     file_name = message_json["Records"][0]["s3"]["object"]["key"]

#     print("bucket_name :", bucket_name)
#     print("file_name :", file_name)
    
#     glue.start_job_run(
#         JobName='edp-glue-job',
#         Arguments={
#             '--bucket_name':bucket_name,
#             '--file_name':file_name,
#         }
#     )


import json
import boto3

def lambda_handler(event, context):
    
    try:

        print("event content : ",event )

        glue = boto3.client('glue')
        body = json.loads(event['Records'][0]['body'])
        message_json = json.loads(body['Message'])

        bucket_name = message_json["Records"][0]["s3"]["bucket"]["name"]
        file_name = message_json["Records"][0]["s3"]["object"]["key"]

        print("bucket_name :", bucket_name)
        print("file_name :", file_name)
    
        raise Exception("glue job not started")
    
        glue.start_job_run(
            JobName='edp-glue-job',
            Arguments={
                '--bucket_name':bucket_name,
                '--file_name':file_name,
            }
        )
    except Exception as e:
        print("exception =",e)
        raise
