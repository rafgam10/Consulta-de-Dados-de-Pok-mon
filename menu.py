def exibirInfomacaoPokemon(data):
    #Tem um paramntro de data para colocar o json do pokémon;
    print("\nStatus do Pokémon.")
    print(f"Nome do Pokémon: {data['name']}")
    print(f"Id do Pokémon: {data['id']}")
    print(f"Altura do Pokémon: {data['height']}")
    print(f"Comprimento do Pokémon: {data['weight']}")
    print(f"Tipo do Pokémon: {data['types'][0]['type']['name']}")

def evolucaoPokemon():
    pass

def exibirMovimentosPokemon():
    pass



