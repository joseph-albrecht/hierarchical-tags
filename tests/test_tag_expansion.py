import pytest
import csv
from hierarchical_tags.tag_expansion import expand_tags
from hierarchical_tags.tag_expansion import expand_tags_string
from hierarchical_tags.tag_expansion import expand_tags_in_csv

def test_expand_tags_should_return_an_iterator_with_all_sub_tags():
    expected_sub_tags = ['sub', 'sub/tags', 'sub/tags/list']
    actual_sub_tags = [sub for sub in expand_tags('sub/tags/list')]
    assert expected_sub_tags == actual_sub_tags

def test_expand_tags_with_different_delimiter():
    expected_sub_tags = ['sub', 'sub:tags', 'sub:tags:list']
    actual_sub_tags = [sub for sub in expand_tags('sub:tags:list', ':')]
    assert expected_sub_tags == actual_sub_tags

def test_expand_tags_string_should_return_string_with_all_sub_tags():
    expected_sub_tags = "sub sub/tags sub/tags/string"
    actual_sub_tags = expand_tags_string("sub/tags/string")
    assert expected_sub_tags == actual_sub_tags

def test_expand_tags_in_a_single_tsv(tmpdir):
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
    file_path = str(unprocessed_file)
    open_unprocessed_file = unprocessed_file.open(mode='w')
    writer = csv.writer(open_unprocessed_file, delimiter='\t')
    for line in in_lines:
        writer.writerow(line)
    open_unprocessed_file.close()
    expand_tags_in_csv(str(file_path))

    print (file_path)
    with open(file_path, 'r') as processed_file:
        reader = csv.reader(processed_file, delimiter='\t')
        for i, row in enumerate(reader):
            assert row[2] == out_lines[i][2]
            
                       
    
    
    
    


    
    
