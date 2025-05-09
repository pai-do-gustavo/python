precoCapa = 24.95
descontoLivraria = precoCapa * 0.40
precoCapaLivraria = precoCapa - descontoLivraria

freteRestanteExemplar = 3.00
freteRestantesExemplares = 0.75

custoAtacadoPrimeiroExemplar = precoCapaLivraria + freteRestanteExemplar
custoAtacado = custoAtacadoPrimeiroExemplar + ((precoCapaLivraria + freteRestanteExemplar) * 59)

print('o custo total de atacado de 60 copias é de :', custoAtacado)