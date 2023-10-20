import os
os.system("cls")

pamela = int(input("Votos Pamela: "))
carol = int(input("Votos Carol: "))
fanny = int(input("Votos Fanny: "))

votos = pamela+carol+fanny
candidatos = [pamela,carol,fanny]

if pamela == carol == fanny : print("Elecciones anuladas: ")

elif pamela >= votos/2 + 1 :
    ganador = pamela
    candidatos.remove(pamela)
    if max(candidatos) == carol : 
        puesto2 = "Carol" 
        puesto3 = "Fanny"
        print("Primer puesto: ",ganador)
        print("Segundo puesto: ",puesto2)
        print("Tercer puesto: ",puesto3)
    elif max(candidatos) == fanny : 
        puesto2 = "Fanny" 
        puesto3 = "Carol"
        print("Primer puesto: ",ganador)
        print("Segundo puesto: ",puesto2)
        print("Tercer puesto: ",puesto3)
    elif carol == fanny : print("Elecciones anuladas")

elif carol >= votos/2 + 1 :
    ganador = carol
    candidatos.remove(carol)
    if max(candidatos) == pamela : 
        puesto2 = "Pamela" 
        puesto3 = "Fanny"
        print("Primer puesto: ",ganador)
        print("Segundo puesto: ",puesto2)
        print("Tercer puesto: ",puesto3)
    elif max(candidatos) == fanny : 
        puesto2 = "Fanny" 
        puesto3 = "Pamela"
        print("Primer puesto: ",ganador)
        print("Segundo puesto: ",puesto2)
        print("Tercer puesto: ",puesto3)
    elif pamela == fanny : print("Elecciones anuladas")

elif fanny >= votos/2 + 1 :
    ganador = fanny
    candidatos.remove(fanny)
    if max(candidatos) == carol :
        puesto2 = "Carol"
        puesto3 = "Pamela"
        print("Primer puesto: ",ganador)
        print("Segundo puesto: ",puesto2)
        print("Tercer puesto: ",puesto3)
    elif max(candidatos) == fanny : 
        puesto2 = "Pamela" 
        puesto3 = "Carol"
        print("Primer puesto: ",ganador)
        print("Segundo puesto: ",puesto2)
        print("Tercer puesto: ",puesto3)
    elif carol == pamela : print("Elecciones anuladas")

else : print ("Segunda vuelta")