from google.transit import gtfs_realtime_pb2
from urllib.request import urlopen,Request
import requests

feed = gtfs_realtime_pb2.FeedMessage()

access = requests.post('http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token=01ea202dcd17b1e00993772a52d7d4739657f936c3fc0fe2e496b251354801c9')
if(access):
    response = requests.get('http://api.olhovivo.sptrans.com.br/v2.1/Posicao')
    print(response)
# feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print(entity.trip_update)