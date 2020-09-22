# -*- coding: utf-8 -*-
from math import pi
import sys
import errno

'''class TerminalColor:
    ERRO = '\033[1;32m' NÃO FUNCIONOU COR
    NORMAL = '\033[0;0m'''


def circulo(raio):
    return pi * float(raio) ** 2
    
def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][59:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor númerico.')
        sys.exit(errno.EINVAL)
    
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área da circunferência:', area)
        
    
