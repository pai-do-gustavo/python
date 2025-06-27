def right_justify(palavra, TamanhoPalavra):
    espaco = '-'
    resultado = espaco * (5 - TamanhoPalavra)
    return resultado + palavra

palavra = str(input('digite uma palavra'))
TamanhoPalavra = len(palavra)

justificado = (right_justify(palavra, TamanhoPalavra)) # chamada de funcao recebe argumento

print(justificado)