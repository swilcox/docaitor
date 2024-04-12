from ..data_merge import merge_data


def test_merge_data():
    a = {"a": [1, 2, 3]}
    b = {"a": [4, 5], "b": "Bubba"}
    assert merge_data([a, b]) == {"a": [1, 2, 3, 4, 5], "b": "Bubba"}


def test_merge_data_overwrite():
    a = {"a": [1, 2, 3], "b": "Bob"}
    b = {"a": [4, 5], "b": "Bubba"}
    assert merge_data([a, b]) == {"a": [1, 2, 3, 4, 5], "b": "Bubba"}
