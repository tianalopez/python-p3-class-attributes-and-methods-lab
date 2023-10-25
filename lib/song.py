class Song:
    count = 0
    artists = []
    genres=[]
    genre_count = {}
    artist_count={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls, genre):
        try: cls.genre_count.update({genre: cls.genre_count[genre] +1})
        except: cls.genre_count[genre] = 1
        if not cls.genres.count(genre):
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        try: cls.artist_count.update({artist: cls.artist_count[artist] + 1})
        except: cls.artist_count[artist] = 1

        if not cls.artists.count(artist):
            cls.artists.append(artist)
