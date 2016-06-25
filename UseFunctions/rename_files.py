
from os import walk
from os import rename
from re import sub

def rename_files(path):
    # get filenames
    for root, dirs, files in walk(path):
        for file in files:
            filename = root + '/' + file
            renamed = sub(r'\d+', '', file)
            new_filename = root + '/' + renamed
            print 'Changing %s to %s' % (file, renamed)
            rename(filename, new_filename)
    # for each file, rename
    pass

rename_files(r'/Users/jmrunkle/GitHub/ProgrammingFoundationsWithPython/UseFunctions/prank')