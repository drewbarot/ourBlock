import boto3
from elasticsearch import Elasticsearch,RequestsHttpConnection

def search(event,context):
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
  query = event['query']
  es = connectES('https://search-hacktps-2xwfbumjkznhuydichzbdudpe4.us-east-2.es.amazonaws.com') #add endpoint
  data = []
  if query=='':
    data = es.search(size=10000,from_=0)
  else:
    data = es.search(size=10000,from_=0,q='"'+query+'"~5')
  #incorporate vishal's code
  return data