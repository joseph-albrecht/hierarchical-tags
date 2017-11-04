import pytest
import csv
from hierarchical_tags.tag_expansion import expand_tags
from hierarchical_tags.tag_expansion import expand_tags_string
from hierarchical_tags.tag_expansion import expand_tags_in_csv

def test_expand_tags_should_return_an_iterator_with_all_sub_tags():
    expected_sub_tags = ['sub', 'sub/tags', 'sub/tags/list']
    actual_sub_tags = list(expand_tags('sub/tags/list'))
    assert expected_sub_tags == actual_sub_tags

def test_expand_tags_with_different_delimiter():
    expected_sub_tags = ['sub', 'sub:tags', 'sub:tags:list']
    actual_sub_tags = list(expand_tags('sub:tags:list', ':'))
    assert expected_sub_tags == actual_sub_tags

def test_expand_tags_string_should_return_string_with_all_sub_tags():
    expected_sub_tags = "sub sub/tags sub/tags/string"
    actual_sub_tags = expand_tags_string("sub/tags/string")
    assert expected_sub_tags == actual_sub_tags

def test_expand_tags_with_a_single_tsv(tmpdir):
    #make tsv lines
    header = ['front', 'back', 'Tags']
    unprocessed_row_one = ['d', 'b', 'sub/tags/list']
    unprocessed_row_two = ['a', 'b', 'second/list']
    processed_row_one = ['a', 'b', 'sub sub/tags sub/tags/list']
    processed_row_two = ['a', 'b', 'second second/list']

    in_lines = [header, unprocessed_row_one, unprocessed_row_two]
    out_lines = [processed_row_one, processed_row_two]

    #make file
    unprocessed_file = tmpdir.join('in_file.tsv')
    path = str(unprocessed_file)

    with open(path, 'w') as new_file:
        writer = csv.writer(new_file, delimiter='\t')
        for line in in_lines:
            writer.writerow(line)

    expand_tags_in_csv(path)

    with open(path, 'r') as processed_file:
        reader = csv.reader(processed_file, delimiter='\t')
        for i, row in enumerate(reader):
            assert row[2] == out_lines[i][2]

            

def test_expand_tags_with_multiple_tsv(tmpdir): #make tsv lines
    header = ['front', 'back', 'Tags']
    unprocessed_row_one = ['d', 'b', 'sub/tags/list']
    unprocessed_row_two = ['a', 'b', 'second/list']
    processed_row_one = ['a', 'b', 'sub sub/tags sub/tags/list']
    processed_row_two = ['a', 'b', 'second second/list']

    in_lines = [header, unprocessed_row_one, unprocessed_row_two]
    out_lines = [processed_row_one, processed_row_two]

    #make files
    paths = []
    for i in range(5):
        unprocessed_file = tmpdir.join('in_file' + str(i) + '.tsv')
        path = str(unprocessed_file)
        with open(path, 'w') as new_file:
            writer = csv.writer(new_file, delimiter='\t')
            for line in in_lines:
                writer.writerow(line)
        paths.append(path)
        expand_tags_in_csv(path)

    for path in paths:
        with open(path, 'r') as processed_file:
            reader = csv.reader(processed_file, delimiter='\t')
            for i, row in enumerate(reader):
                assert row[2] == out_lines[i][2]
                      
    
    
    
    


    
    
