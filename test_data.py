import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?"


class TestData:
    def test_gov(self):
        """

        Here's posetive scenario
        """
        datas = {'valcode': "USD", 'date': '20161009'}
        parampoz = requests.get(url, params=datas)
        assert 200 == parampoz.status_code
        print(parampoz.text)

class TestDataNeg():

    def test_gov(self):
        """

        Here's negative scenario
        """
        datas = {'valcode': "!@#", 'date': '#$%^@!@222222222'}
        paramneg = requests.get(url, params=datas)
        assert 200 == paramneg.status_code
        print(paramneg.text)

class TestDataBR():
    """

            Here's  scenario with put parametr
            """

    def test_gov(self):
        datas = {'valcode': "!@#", 'date': '#$%^@!@222222222'}
        paramz = requests.put(url, params=datas)
        assert 400 == paramz.status_code
        print(paramz.text)