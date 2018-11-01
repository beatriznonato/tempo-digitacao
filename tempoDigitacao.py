import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
vez = 1
repeat = 5

print('Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO. É necessário que você digite essa palavra '+str(repeat)+ ' vezes.')
input('Aperte a tecla enter para começar.')
while vez <= repeat:
    inicio = t.clock()
    input('Digite a palavra: ')
    fim = t.clock()
    tempo = round(fim-inicio,2)
    tempos.append(tempo)
    vezes.append(vez)
    vezstr = str(vez)+'° vez'
    legenda.append(vezstr)
    vez += 1

plt.xticks(vezes,legenda)
plt.plot(vezes,tempos)
plt.show()
