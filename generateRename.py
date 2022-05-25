import os
import re

DELIMITER='/'
LIBRARY_PATH='./Audiobooks'
METADATA_FILENAME='metadata.abs'
OUTPUT_FILE='./fixLibrary.sh'
HEADER='#!/usr/bin/sh\n\n'

class Book:
    def __init__(self, filename):
        f = open(filename)
        fields = ['title', 'subtitle', 'narrators', 'series', 'sequence']
        for line in f:
            for field in fields:
                pattern = f"{field}=(.*)"
                m = re.match(pattern,line)
                if m:
                    setattr(self, field, m.group(1))

            if re.match('\[CHAPTER\]', line):
                break
        f.close()
        
        self.__parseSeries()


    def __parseSeries(self):
        if hasattr(self, 'series'):
            allSeries=self.series.split(', ')
            self.series=[]
            for series in allSeries:
                series=series.split(' #')
                self.series.append({
                    'name':series[0],
                    'sequence':series[1] if len(series)>1 else None
                    })


def main():
    f=open(OUTPUT_FILE, 'w')
    f.write(HEADER)
    for root, dirs, files in os.walk(LIBRARY_PATH):
        if METADATA_FILENAME in files:
            book = Book(DELIMITER.join([root,METADATA_FILENAME]))
            newFolder=f"{book.series[0]['sequence']}. " if len(book.series)==1 and book.series[0]['sequence'] else ''
            newFolder+=book.title
            newFolder+=f' - {book.subtitle}' if book.subtitle else ''
            newFolder+=f' {{{book.narrators}}}' if book.narrators else ''

            path=root.split(DELIMITER)
            if newFolder != path[len(path)-1]:
                path[len(path)-1] = newFolder
                f.write (f'mv "{root}" "{DELIMITER.join(path)}"\n')
    return

main()
