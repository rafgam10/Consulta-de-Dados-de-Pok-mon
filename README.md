# Consulta-de-Dados-de-Pokémon

Este projeto é uma aplicação Python que consulta dados da [PokéAPI](https://pokeapi.co/) e exibe informações detalhadas sobre Pokémons, como nome, habilidades, altura, peso e movimentos.

## Funcionalidades

- Consultar informações sobre um Pokémon por nome ou ID.
- Exibir as seguintes informações de um Pokémon:
  - Nome
  - ID
  - Altura
  - Peso
  - Tipo
  - Movimentos/Habilidades
- Menu interativo que permite escolher entre diferentes opções.

## Como Funciona

A aplicação realiza uma requisição HTTP para a PokéAPI para buscar os dados do Pokémon especificado pelo usuário. Após a resposta ser recebida, os dados são tratados e exibidos de forma legível no terminal.

## Pré-requisitos

- Python 3.x
- Biblioteca `requests` (para fazer requisições HTTP)

### Instalação de dependências

Para instalar as dependências necessárias, execute:

```bash
pip install requests
```

### Como Executar

#### 1.Clone este repositório:

```git clone https://github.com/seu-usuario/seu-repositorio.git```

#### 2.Entre no diretório do projeto:

```cd consulta-de-pokemon```

#### 3.Execute o script principal:

```cd python main.py```

#### Exemplo de Uso

-Ao rodar o programa, você verá um menu com as seguintes opções:
```
Opções de Status:
1. Digite o nome/id do Pokémon.
2. Exibir as Informações do Pokémon.
3. Exibir os Movimentos do Pokémon.
4. Sair do Programa.
```

-Insira a sua escolha e siga as instruções para consultar informações detalhadas de um Pokémon.

##### Estrutura do Projeto

-`main.py`: Arquivo principal que inicia o programa e exibe o menu.

-`menu.py`: Contém as funções relacionadas ao menu e exibição de informações do Pokémon.

-`funs.py`: Contém a função que faz a requisição HTTP à PokéAPI.

##### Tecnologias Utilizadas

- **Python 3.x**

- **PokéAPI** para consulta de dados de Pokémon, Acesse a PokéAPI diretamente [clicando aqui](https://pokeapi.co/).

- **Requests** para fazer as requisições HTTP

