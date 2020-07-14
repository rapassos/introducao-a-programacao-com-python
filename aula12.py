###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 14/Jul/2020
###############################################

import requests

def buscaLogradouro(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    #print(response.status_code)
    #texto = response.text
    json = response.json()
    #print(json['logradouro'])
    return json

def dadosPokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    #print(response.status_code)
    dados = response.json()
    return dados

def getResponse(url):
    response = requests.get(url)
    #print(response.status_code)
    return response.text


if __name__ == "__main__":
    pass
    #print(buscaLogradouro('09861700'))
    #print(buscaLogradouro('09861700')['logradouro'])
    #print(dadosPokemon('pikachu'))
    #print(dadosPokemon('pikachu')['sprites']['front_shiny'])
    print(getResponse('https://web.digitalinnovation.one/'))


