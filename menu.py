from funs import *

def exibirInfomacaoPokemon(data):
    #Tem um paramntro de data para colocar o json do pokémon;
    print("\nStatus do Pokémon.")
    print(f"Nome do Pokémon: {data['name']}")
    print(f"Id do Pokémon: {data['id']}")
    print(f"Altura do Pokémon: {data['height']}")
    print(f"Comprimento do Pokémon: {data['weight']}")
    print(f"Tipo do Pokémon: {data['types'][0]['type']['name']}")

def evolucaoPokemon():
    #Terminar está parte de evolução;
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


def switch(opcao, data=None):
    if opcao == 1:
        pokemonR = input("Insira o nome/id do Pokémon:")
        r = requisicaoHTTPDoPokemon(pokemonR)

        if r.status_code == 200:
            data = r.json()
        else:
            print("Conexão falhou!")
            return None

    elif opcao == 2:
        if data:
            exibirInfomacaoPokemon(data)
        else:
            print("Nenhum Pokémon carregado!")

    elif opcao == 3:
        if data:
            exibirMovimentosPokemon(data)
        else:
            print("Nenhum Pokémon carregado!")

    else:
        print("Opção inválida, tente novamente.")
        return None
    
    return data
