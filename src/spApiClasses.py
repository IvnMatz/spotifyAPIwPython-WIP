from spApi import *
import requests

class Artist:
    def __init__(self, AccessTk, ArtistID):
        response = getArtist(AccessTk, ArtistID)

        # atributes
        self.name = response['name']
        self.ID = response['id']
        self.followers = response['followers']['total']
        self.genres = response['genres']
        self.profURL = response['external_urls']['spotify']
        self.imgURLs = [response['images'][0]['url'] , response['images'][1]['url'] , response['images'][2]['url'] ]
        self.popularity = response['popularity']
        self.endpoint = response['href']


class Album:
    def __init__(self, AccessTk, albumID):
        response = getAlbum(AccessTk, albumID)

        #atributes
        self.name = response['name']