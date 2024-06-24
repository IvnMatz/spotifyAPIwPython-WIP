from route import Cpath
Cpath()
from spApi import getAccessToken, getID
from ArtistClass import Artist

clientid = ""
secret = ""

token = getAccessToken(clientid, secret)

ID = getID(token, "Kanye West", "artist")

Kanye = Artist(token, ID)

print(Kanye.ttracks['track_0'])
print(Kanye.ttracks['track_1_id'])
