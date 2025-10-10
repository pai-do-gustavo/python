def ApresentaJogador(opcao):
    match opcao:
        case 1:
            print(f'jogador 1: bento')
        case 2:
            print(f'jogador 2: vitin')
        case 3:
            print(f'jogador 3: gabriel')
        case 4:
            print(f'jogador 4: militao')
        case 5:
            print(f'jogador 5: casemiro')
        case 6:
            print(f'jogador 6: douglas santos')
        case 7:
            print(f'jogador 7: vinicios junior')
        case 8:
            print(f'jogador 8: bruno guimalhaes')
        case 9:
            print(f'jogador 9: richarlison')
        case 10:
            print(f'jogador 10:rodrygo')
        case 11:
            print(f'jogador 11: paqueta')
        case _:
            print(f'jogador {opcao} nao encontrato.')

def main():
    print('digite um numero de camisa de 1 até 11:')
    opcao = int(input())

    ApresentaJogador(opcao)


if __name__ == '__main__':
    main()