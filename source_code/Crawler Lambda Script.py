import json

import boto3

def lambda_handler(event, context):
    
    try:

        region = 'ap-south-1'
        crawler_name = 'edp-crawler'
    
        # Create a Glue client
        glue_client = boto3.client('glue', region_name=region)
    
        print("dummy crawler started !!!!!")
        raise Exception("born to die")
    
        # Start the Glue Crawler
        # glue_client.start_crawler(
        #     Name=crawler_name
        # )
        # print("acutal crawler started !!!!!")
    except Exception as e:
        print("Exception ===",e)
        