
# AWS-End-To-End-Event-Driven-Pipeline

# The problem statement :-
Conventional ETL pipelines have trouble with loose connection between components, failover handling, and real-time data ingestion.  
Manual triggers lead to tight integration, poor error recovery, and delay.  
In order to react to new data arrivals in almost real-time, organizations require a scalable and event-driven architecture
that has strong error handling and automation techniques.

# Objective :-
•	Using AWS services create and deploy a serverless, event-driven data pipeline that:- Sends event alerts to S3 to import data.

•	It is processed using ETL pipeline. AWS Glue is used to automate metadata management. Allows for Athena querying. 

•	Puts in place notifications, retries, and error handling.


# Solution Architecture workflow :- 

1.	s3 source bucket :- File uploads in s3 bucket which cause an event to occur.

2.	SNS :- This event is published to the SQS queue via SNS (Source Notification).

3.	SQS queue :- SQS queue stores the incoming events in it.

4.	ETL Lambda :- SQS initiates the Glue job and begins processing.

5.	AWS Glue :- Completes an ETL task and saves the output to a target S3 bucket (Target Path).

6.	S3 (Target Path):- It initiates the Lambda (Crawler Lambda) to launch Glue Crawler.

7.	Glue Crawler :- It crawls the data from target s3 path and adds the new data schema to the Glue Catalog.

8.	Athena: Utilizes the catalog to query processed data.

9.	Dead Letter Queue :- The Dead Letter Queue or DLQ records unsuccessful SQS messages.

10.	SNS (DLQ SNS) :- This SNS is subscribed by Lambda to send out email notifications in the event of an error.

11.	EventBridge :- Records failed Glue jobs and sends them to SQS for further processing.

12.	Notification via email  Lambda: Uses SES or a comparable system to send email warnings.


# Key Focus Area :-

•	Event-Driven Triggers :- S3, SNS, Lambda, and EventBridge are the main areas of focus.

•	AWS Lambda is a serverless computing solution that eliminates infrastructure administration.

•	Automated ETL: crawlers and glue jobs.

•	EventBridge handles Glue job failures, while DLQ handles SQS failures.

•	Observation and Monitoring :- Email notifications of malfunctions through Lambda and SNS.

# AWS Tools & Services Used:

•	Storage :- Amazon S3

•	Messaging :- Amazon SNS, SQS

•	Compute :- AWS Lambda

•	ETL & Cataloging :- AWS Glue, Glue Crawler

•	Querying :- Amazon Athena

•	Failure Detection :- Amazon EventBridge

•	Notification :- Email via Lambda & SES

•	Monitoring :- Amazon CloudWatch


