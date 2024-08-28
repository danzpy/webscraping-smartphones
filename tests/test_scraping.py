import requests

def test_status_code_200():
    '''
    Verifica se a conexão com a url foi bem sucedida.
    '''
    url = 'https://www.kabum.com.br/celular-smartphone/smartphones'

    response = requests.get(url)

    assert response.status_code == 200