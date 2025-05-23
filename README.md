# DesafioModulosPacotesPython
Trabalhando com Módulos e Pacotes em Python - Desafio Escola da Nuvem - Módulo IA + Python + AWS

Desafio: Trabalhando com Módulos e Pacotes em Python
Objetivo: Praticar a criação e o uso de módulos e pacotes em Python.

Parte 1: Criando um MóduloCrie um arquivo chamado matematica.py.
Neste arquivo, crie as seguintes funções:
soma(a, b) que retorna a soma de dois números.
subtrai(a, b) que retorna a subtração.
modulo(n) que retorna o modulo de um número inteiro positivo.

Parte 2: Criando um PacoteCrie uma pasta chamada meu_pacote.
Dentro da pasta, crie:
__init__.py (pode estar vazio).
mensagens.py com uma função boas_vindas(nome) que retorna a mensagem: "Bem-vindo, [nome]! Vamos aprender Python!"
operacoes.py com uma função multiplica(a, b) que retorna a multiplicação.

Parte 3: Usando Módulos e PacotesCrie um arquivo principal chamado main.py.
Neste arquivo:
Importe o módulo matematica.
Importe os módulos do pacote meu_pacote.
Mostre a mensagem de boas-vindas usando boas_vindas("SeuNome").
Realize e imprima os resultados de:
soma(5, 2)
subtrai(10, 4)
modulo(5)
multiplica(3, 7)

Estrutura de diretórios:

projeto\
│
├── main.py
├── matematica.py
└── meu_pacote\
    ├── __init__.py
    ├── mensagens.py
    └── operacoes.py

Instruções importantes:

1) Todos os arquivos devem estar organizados conforme a estrutura acima;

2) O Python irá reconhecer o pacote meu_pacote porque ele estará na mesma pasta de nível do main.py.

3) Anexei uma imagem com o resultado final que deverá ser retornado, conforme consta no desafio original: Imagem_Resultado.
