from spApi import getAlbum, getAlbumTracks

class Album:
    def __init__(self, AccessTk, AlbumID):
        response = getAlbum(AccessTk, AlbumID)

        self.name = response['name']
        self.genres = response['genres']
        self.label = response['label']
        self.popularity = response['popularity']
        self.release_date = response['release_date']
        self.imgURLs = [response['images'][0]['url'], response['images'][1]['url'] , response['images'][2]['url']]
        self.type = response['album_type']
        self.NoTracks = response['total_tracks']
        self.URL = response['external_urls']['spotify']
        self.restrictions = response['restrictions']['reason']
        self.artists = {}
        for i in range(len(response['artists'])):
            self.artists[f'artist_{i+1}'] = response['artists']['name']
            self.artists[f'artist_{i+1}_id'] = response['artists']['name']


        response2 = getAlbumTracks(AccessTk, AlbumID)

        self.tracks = {}
        for i in range(self.NoTracks):
            self.tracks[f'track_{i+1}'] = response2['items']['name']
            self.tracks[f'track_{i+1}_id'] = response2['items']['id']
            self.tracks[f'track_{i+1}_disc_number'] = response2['items']['disc_number']
            
