from menu import *

# Start do Menu:
MenuOpcao()
escolha = int(input("Digite a sua escolha:"))

data = None  # Variável para armazenar o JSON do Pokémon

while escolha != 4:
    data = switch(escolha, data)
    MenuOpcao()
    escolha = int(input("Digite a sua escolha:"))

print("Saindo do Programa...")
