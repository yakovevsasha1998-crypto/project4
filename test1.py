def test_list_diff():
    assert [1,2,3,4] == [1,2,4]

def test_str_diff():
    assert 'hello/nworld' == 'hello\nworld'
