import boto3
import json

def notif(event,context):
  event = json.loads(event['body'])
  sqs = boto3.resource('sqs')
  queue = sqs.get_queue_by_name(QueueName=event['id'])
  messages = []
  for message in queue.receive_messages():
    messages.append(message.body)
    message.delete()
  return { 
        'isBase64Encoded': True
        'statusCode': 200,
        'body': json.dumps(messages),
        'headers': {
           'Content-Type': 'application/json', 
           'Access-Control-Allow-Origin': '*' 
       }
}