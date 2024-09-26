class Song:
  count = 0  # Class attribute to track total songs
  artists = []  # Class attribute to store unique artists
  genres = []  # Class attribute to store unique genres
  genre_count = {}  # Class attribute to store genre counts
  artist_count = {}  # Class attribute to store artist counts

  def __init__(self, name, artist, genre):
    self.name = name
    self.artist = artist
    self.genre = genre
    Song.add_song_to_count()  # Increment count on object creation
    Song.add_to_genres(genre)  # Add genre to class list
    Song.add_to_artists(artist)  # Add artist to class list
    Song.add_to_genre_count(genre)  # Update genre count
    Song.add_to_artist_count(artist)  # Update artist count

  @classmethod
  def add_song_to_count(cls):
    cls.count += 1

  @classmethod
  def add_to_genres(cls, genre):
    if genre not in cls.genres:
      cls.genres.append(genre)

  @classmethod
  def add_to_artists(cls, artist):
    if artist not in cls.artists:
      cls.artists.append(artist)

  @classmethod
  def add_to_genre_count(cls, genre):
    if genre in cls.genre_count:
      cls.genre_count[genre] += 1
    else:
      cls.genre_count[genre] = 1

  @classmethod
  def add_to_artist_count(cls, artist):
    if artist in cls.artist_count:
      cls.artist_count[artist] += 1
    else:
      cls.artist_count[artist] = 1

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

print(f"Total Songs: {Song.count}")  # Access class attribute
print(f"Unique Artists: {Song.artists}")
print(f"Unique Genres: {Song.genres}")

# You can access artist and genre counts after creating some songs
print(f"Genre Count: {Song.genre_count}")
print(f"Artist Count: {Song.artist_count}")
