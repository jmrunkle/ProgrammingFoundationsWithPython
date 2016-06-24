import webbrowser
import time
import sys

for _ in range(3):
    for __ in range(10):
        sys.stdout.write('* ')
        sys.stdout.flush()
        time.sleep(1)
    print ''
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    webbrowser.open(url)