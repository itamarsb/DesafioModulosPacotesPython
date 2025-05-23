# matematica.py

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrai(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def modulo(n):
    """Retorna o valor absoluto (módulo) de um número inteiro."""
    if not isinstance(n, int):
        raise ValueError("O número deve ser inteiro.")
    return abs(n)
