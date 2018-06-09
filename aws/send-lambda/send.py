import boto3

def send(event,context):
  sqs = boto3.resource('sqs')
  try:
    sqs.create_queue(QueueName=event['id'])
  except:
    pass
  queue = sqs.get_queue_by_name(QueueName=event['id'])
  response = queue.send_message(MessageBody=event['body'])