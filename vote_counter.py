import csv

def sortByVotes(results): #Refactorizacion 1
    return sorted(results.items(), key=lambda item:item[1], reverse=True)

def showWinner(sortedbyvotes): #Refactorizacion 2
    if sortedbyvotes[0][1] == sortedbyvotes[1][1]: 
        tied_candidates = [candidate for candidate, votes in sortedbyvotes if votes == sortedbyvotes[0][1]]
        print("Tie between " + " and ".join(tied_candidates))
    else:
        print(f"winner is {sortedbyvotes[0][0]}")

def showResults(results): #Refactorizacion 3
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

def getReader(csvfile, delimiter=','): #Refactorizacion 4
    reader = csv.reader(csvfile, delimiter= delimiter)
    next(reader)  # Saltar el encabezado
    return reader

def getCountsperCandidate(reader): #Refactorizacion 5
    results = {}
    for row in reader:
        candidate = row[1]
        try:
            votes = int(row[2])
        except:
            votes = 0
        
        if candidate in results:
            results[candidate] += votes
        else:
            results[candidate] = votes
    return results 

def getResults(file_path):#Refactorizacion 6
    results = {}
    with open(file_path, newline='') as csvfile:
        reader = getReader(csvfile)
        results = getCountsperCandidate(reader)

    return results


def count_votes(file_path):
    results = getResults(file_path)
    showResults(results)
    sortedbyvotes = sortByVotes(results)
    showWinner(sortedbyvotes)

# Ejemplo de uso
count_votes('votes.csv')
