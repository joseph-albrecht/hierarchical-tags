#!/anaconda/bin/python3
'''
It can be frustrating adding many tags to anki when they're hierarchical.
This script takes a .tsv and unpacks the hierarchical tag column so that
when making cards you don't have to type the same pathname over and over.
This way you can write the deepest tag path and this script will unpack
it to list out all of the tag-directories the card is in.
'''
import sys
import csv
from shutil import move

def expand_tags(tag, delimiter='/'):
    subtags = tag.split(delimiter)
    for i in range(1, len(subtags) + 1):
        yield delimiter.join(subtags[:i])

def expand_tags_string(tag_string, delimiter='/'):
    expanded_tags = []
    original_tags = tag_string.split()
    for original_tag in original_tags:
        for expandend_tag in expand_tags(original_tag):
            expanded_tags.append(expandend_tag)

    return ' '.join(expanded_tags)

def expand_tags_in_csv(csv_file, delimiter='/'):
    with open(file, 'r') as infile, open('[temp]' + file, 'w') as outfile:
        reader = csv.DictReader(infile, delimiter="\t")
        writer = csv.writer(outfile, delimiter="\t")
        for row in reader:
            row['Tags'] = expand_tags_string(row['Tags'])
            writer.writerow(row.values()) #use .values so that we don't print
                                          #the header row over and over
    #replace the original file with the newly unpacked file
    move(outfile.name, file)

def main():
    _, delimiter, *filenames = sys.argv
    for file in filenames:
        expand_tags_in_csv(file, delimiter)

if __name__ == '__main__':
    main()
