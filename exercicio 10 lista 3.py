def classificarJogador(idade):
    if 5 <= idade <= 7:
        print("Categoria: Infantil A (5 - 7 anos)")
    elif 8 <= idade <= 10:
        print("Categoria: Infantil B (8 - 10 anos)")
    elif 11 <= idade <= 13:
        print("Categoria: Juvenil A (11 - 13 anos)")
    elif 14 <= idade <= 17:
        print("Categoria: Juvenil B (14 - 17 anos)")
    elif idade >= 18:
        print("Categoria: Sênior (18 anos ou mais)")
    else:
        print("Idade inválida.")

idade = int(input("Digite a idade do jogador: "))
classificarJogador(idade)