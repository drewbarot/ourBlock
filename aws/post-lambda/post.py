import boto3
from elasticsearch import Elasticsearch,RequestsHttpConnection
import json

def post(event,context):
  event = json.loads(event['body'])
  def connectES(esEndPoint):
    print ('Connecting to the ES Endpoint {0}'.format(esEndPoint))
    try:
      esClient = Elasticsearch(
      hosts=[{'host': esEndPoint, 'port': 443}],
      use_ssl=True,
      verify_certs=True,
      connection_class=RequestsHttpConnection)
      return esClient
    except Exception as E:
      print("Unable to connect to {0}".format(esEndPoint))
      print(E)
      exit(3)
  es = connectES('search-hacktps-2xwfbumjkznhuydichzbdudpe4.us-east-2.es.amazonaws.com')
  es.index(index='data',doc_type='crime',body=event['body'])
  return { 
    'isBase64Encoded': True,
    'statusCode': 200,
    'body': ''
    'headers': {
       'Content-Type': 'application/json', 
       'Access-Control-Allow-Origin': '*' 
   }
  }