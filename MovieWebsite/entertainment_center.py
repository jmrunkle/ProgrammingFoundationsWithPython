import media
from fresh_tomatoes import open_movies_page

toy_story = media.Movie(
    title='Toy Story',
    synopsis=(
        'Story of a boy whose toys come to life.'),
    poster=(
        'https://upload.wikimedia.org/wikipedia/en/'
        '1/13/Toy_Story.jpg'),
    youtube='https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie(
    title='Avatar',
    synopsis='A marine on an alien planet.',
    poster=(
        'https://upload.wikimedia.org/wikipedia/en/'
        'b/b0/Avatar-Teaser-Poster.jpg'),
    youtube='https://www.youtube.com/watch?v=uZNHIU3uHT4')

movies = [toy_story, avatar]
open_movies_page(movies)