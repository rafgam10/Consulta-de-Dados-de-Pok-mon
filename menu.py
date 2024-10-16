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

def exibirMovimentosPokemon(data):
    print("\nMovimetos do Pokémon:")
    for ability in data['abilities']:
        print(f"{ability['ability']['name']}")

def MenuOpcao():
    print("\nOpções de Status")
    print(f"1.Digite o nome/id do Pokémon.")
    print(f"2.Exibir as Infomações do Pokémon.")
    print(f"3.Exibir os Movimentos do Pokémon.")
    print(f"4.Sair do Programar.")

