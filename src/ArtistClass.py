from spApi import *

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

        #atributes related to top tracks (simplified information)
        response2 = aTopTracks(AccessTk, ArtistID)

        self.NoTracks = len(response2['tracks'])
        self.ttracks = {}
        for i in range(self.NoTracks):
            self.ttracks[f'track_{i+1}'] = response2['tracks'][i]['name']
            self.ttracks[f'track_{i+1}_id'] = response2['tracks'][i]['id']

        #Albums related atributes
        response3 = ArtistAlbums(AccessTk, ArtistID, "album")

        self.NoAlbums = len(response3['items'])
        self.album = {}
        for i in range(self.NoAlbums):
            self.album[f'album_{i+1}'] = response3['items'][i]['name']
            self.album[f'album_{i+1}_id'] = response3['items'][i]['id']
            
        response4 = relatedArtists(AccessTk, ArtistID)

        self.NoRelated_Artists = len(response4['artists'])
        self.related_Artists = {}
        for i in range(self.NoRelated_Artists):
            self.related_Artists[f'r_artist_{i+1}'] = response4['artists'][i]['name']
            self.related_Artists[f'r_artist_{i+1}_id'] = response4['artists'][i]['id']
