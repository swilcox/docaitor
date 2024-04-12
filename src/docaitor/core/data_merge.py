from deepmerge import always_merger


def merge_data(data_list: list[dict]) -> dict:
    result = {}
    for data in data_list:
        result = always_merger.merge(result, data)
    return result
