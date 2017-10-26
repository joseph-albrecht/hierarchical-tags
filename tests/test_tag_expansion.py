import pytest
from hierarchical_tags.tag_expansion import expand_tags
from hierarchical_tags.tag_expansion import expand_tags_string

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
    
    
