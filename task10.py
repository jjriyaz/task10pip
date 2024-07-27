import random

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def audio_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def playlist_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0
class User:
    def __init__(self, name):
        self.name = name

    def rate_audio(self, audio, rating):
        audio.add_rating(rating)

    def rate_playlist(self, playlist, rating):
        playlist.add_rating(rating)

class MusicPlayer:
    def __init__(self):
        self.users = []
        self.playlists = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist
    def search_audio_by_name(self, name):
        # Implement audio search logic by name
        pass
    def search_Playlist_by_name(self, name):
        # Implement audio search logic by name
        pass


# Example usage:
player = MusicPlayer()

# Creating users
user1 = player.create_user("vijay")
user2 = player.create_user("ajith")
user3 = player.create_user("surya")

# Creating playlists
playlist1 = player.create_playlist("Pop Hits", "Pop")
playlist2 = player.create_playlist("Rock Classics", "Rock")

# Adding audio to playlists
audio1 = Audio("Song 1", "https://example.com/song1.mp3")
audio2 = Audio("Song 2", "https://example.com/song2.mp3")
audio3 = Audio("Song 3", "https://example.com/song3.mp3")

playlist1.add_audio(audio1)
playlist1.add_audio(audio2)
playlist2.add_audio(audio3)

# Users give the random rating in audios and playlists
user1.rate_audio(audio1, random.randint(1, 5))
user2.rate_audio(audio1, random.randint(1, 5))
user3.rate_audio(audio2, random.randint(1, 5))

user1.rate_playlist(playlist1, random.randint(1, 5))
user2.rate_playlist(playlist1, random.randint(1, 5))
user3.rate_playlist(playlist2, random.randint(1, 5))

# Calculating average ratings
average_rating_audio1 = audio1.audio_average_rating()
average_rating_playlist1 = playlist1.playlist_average_rating()

#print average rating

print(f"Average rating for Playlist 1: {average_rating_playlist1}")
print(f"Average rating for Audio 1: {average_rating_audio1}")