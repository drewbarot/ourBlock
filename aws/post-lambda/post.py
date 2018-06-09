import boto3
from elasticsearch import Elasticsearch,RequestsHttpConnection

def post(event,context):
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
  
post({'body':{'key':'value'}},None)