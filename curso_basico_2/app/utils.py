import mock_countrys

def population_by_country(data,country):
    result = list(filter(lambda item: item["country"] == country, data))
    return result

countrys = mock_countrys.countrys
