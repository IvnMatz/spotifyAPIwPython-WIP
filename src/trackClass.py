from spApi import getTrack, getAudioAnalysis, getAudioFeatures

class Track:
    def __init__(self, AccessTk, trackID):
        response = getTrack(AccessTk, trackID)

        self.name = response['name']
        self.id = response['id']
        self.explicit = response['explicit']
        self.disc_number = response['disc_number']
        self.track_number = response['track_number']
        self.durationMs = response['duration_ms']
        self.URL = response['external_urls']['spotify']
        self.endpoint = response['href']

        self.is_playable = response['is_playable']
        self.restrictions = response['restrictions']['reason']
        self.popularity = response['popularity']
        self.preview_url = response['preview_url']

        #artists
        self.NoArtists = len(response['artists'])
        self.artists = {}
        for i in range(self.NoArtists):
            self.artists[f'artist_{i+1}'] = response['artists'][i]['name']
            self.artists[f'artist_{i+1}_id'] = response['artists'][i]['id']

        #albums
        self.NoAlbums = len(response['album'])
        self.albums = {}
        for i in range(self.NoAlbums):
            self.albums[f'album_{i+1}'] = response['album'][i]['name']
            self.albums[f'album_{i+1}_id'] = response['album'][i]['id']

        #Audio Features Atributes
        response = getAudioFeatures(AccessTk, trackID)

        self.acousticness = response['acousticness']
        self.analysis_url = response['analysis_url']
        self.danceability = response['danceability']
        self.energy = response['energy']
        self.instrumentalness = response['instrumentalness']
        self.key = response['key']
        self.liveness = response['liveness']
        self.loudness = response['loudness']
        self.mode = response['mode']
        self.valence = response['valence']
        self.time_signature = response['time_signature']
        self.tempo = response['tempo']
        self.speechiness = response['speechiness']

