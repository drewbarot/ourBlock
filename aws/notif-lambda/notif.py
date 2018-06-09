import boto3

def notif(event,context):
  sqs = boto3.resource('sqs')
  queue = sqs.get_queue_by_name(QueueName=event['id'])
  messages = []
  for message in queue.receive_messages():
    messages.append(message.body)
    message.delete()
  return messages