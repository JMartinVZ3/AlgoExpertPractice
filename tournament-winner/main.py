competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"],
]
results = [0, 0, 1]

def tournamentWinner(competitions, results):
    lista = []
    for i in range(0, len(competitions)):
        if results[i] == 0:
            lista.append(competitions[i][1])
        else:
            lista.append(competitions[i][0])
    
    return max(set(lista), key = lista.count)

print(tournamentWinner(competitions, results))