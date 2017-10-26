import pytest
from src.tag_expansion import expand_tags

def test_expand_tags_should_return_an_iterator_with_all_sub_tags():
    expected_sub_tags = ['sub', 'sub/tags', 'sub/tags/set']
    actual_sub_tags = [sub for sub in expand_tags('sub/tags/set')]
    assert expected_sub_tags == actual_sub_tags
    
    
