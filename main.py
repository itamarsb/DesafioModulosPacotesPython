# main.py

# Importações de módulo e pacote
import matematica
from meu_pacote.mensagens import boas_vindas
from meu_pacote.operacoes import multiplica

def main():
    nome = "Itamar"
    print(boas_vindas(nome))
    
    resultado_soma = matematica.soma(5, 2)
    resultado_subtrai = matematica.subtrai(10, 4)
    resultado_modulo = matematica.modulo(5)
    resultado_multiplica = multiplica(3, 7)

    print(f"Soma: {resultado_soma}")
    print(f"Subtração: {resultado_subtrai}")
    print(f"Módulo: {resultado_modulo}")
    print(f"Multiplicação: {resultado_multiplica}")

if __name__ == "__main__":
    main()
