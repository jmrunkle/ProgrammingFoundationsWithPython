import urllib

def read_text():
    content = ''
    try:
        quotes = open(
            '/Users/jmrunkle/GitHub/'
            'ProgrammingFoundationsWithPython/ProfanityEditor/'
            'movie_quotes.txt')
        content = quotes.read()
        if check_profanity(content):
            print 'This text has profanity and is unacceptable!'
        else:
            print content
        quotes.close()
    except IOError, ioe:
        print 'Got an error reading the file!'
        raise ioe


def check_profanity(text):
    try:
        connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=%s' % text)
        content = connection.read()
        ret = 'true' in content
        connection.close()
        return ret
    except IOError, ioe:
        print 'Got an error accessing WDYL!'
        raise ioe
    return False


assert check_profanity('shit')
assert not check_profanity('shot')


read_text()