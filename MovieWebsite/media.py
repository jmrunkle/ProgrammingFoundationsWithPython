import webbrowser

class Movie(object):
    """docstring for Movie"""
    def __init__(self, title, synopsis, poster, youtube):
        super(Movie, self).__init__()
        self.title = title
        self.synopsis = synopsis
        self.poster = poster
        self.youtube = youtube

    def title(self):
        return self.title

    def synopsis(self):
        return self.synopsis

    def poster(self):
        return self.poster

    def youtube(self):
        return self.youtube

    def show_trailer(self):
        url = self.youtube()
        webbrowser.open(url)

kwargs = {
    'title': None,
    'synopsis': None,
    'poster': None,
    'youtube': None}
assert Movie(**dict(kwargs, **{'title':'title'})).title == 'title'
assert Movie(**dict(kwargs, **{'synopsis':'synopsis'})).synopsis == 'synopsis'
assert Movie(**dict(kwargs, **{'poster':'poster'})).poster == 'poster'
assert Movie(**dict(kwargs, **{'youtube':'youtube'})).youtube == 'youtube'
