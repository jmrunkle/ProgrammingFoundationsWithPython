

def read_text():
    try:
        quotes = open(
            '/Users/jmrunkle/GitHub/'
            'ProgrammingFoundationsWithPython/ProfanityEditor/'
            'movie_quotes.txt')
        content = quotes.read()
        print content
        quotes.close()
    except IOError, ioe:
        print 'Got an error reading the file!'
        raise ioe


read_text()