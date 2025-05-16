print('valor do primeiro trecho:')
MinutoPrimeiroTrecho = 8 * 60
SegundoPrimeiroTrecho = 35

#print('tempo do primeiro trecho em segundos:', totalTempoPrimeiroTrecho)

print('tempo do segundo trecho: 7min e 12seg')
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12 * 3

#print('tempo do segundo trecho em segundos:', totalTempoSegundoTrecho)

print('tempo do terceiro trecho: 8 min e 15 seg')
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15


#print('tempo do terceiro trecho em segundos:', totalTempoTerceiroTrecho)

#soma o total de minutos e converte os todos os segundos em minutos
totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

#soma valor total dos segundos
totalTempoTodosTrechosSegundos = (segundoPrimeiroTrecho + segundosSegundoTrecho + segundoTerceiroTrecho)

restanteMinutos = int(totalTempoTodosTrechosMinutos/ 60)
restanteSegundos = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMinutos + restanteMinutos
totalSegundos = totalTempoTodosTrechosSegundos + restanteSegundos
print('soma de tempo de todos os trechos:', totalSegundos, 'segundos')
print('soma de tempo de todos os trechos:', totalMinutos, 'minutos')

horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
print(horaInicialSegundos)
print(minutoInicialSegundos)
horarioInicialSegundos = horaInicialSegundos + minutoInicialSegundos


print(horarioInicialSegundos)
tempoTrechoMinutoSegundos = totalMinutos * 60
print(tempoTrechoMinutoSegundos)
horaChegada = int(((horarioInicialSegundos + tempoTrechoMinutoSegundos) / 60) / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutoSegundos)/60) % 60)

print('o tempo de chegada foi de ', horaChegada, ';', minutoChegada, restanteSegundos)



