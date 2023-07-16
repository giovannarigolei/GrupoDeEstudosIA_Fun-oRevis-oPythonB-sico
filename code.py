#Importações
import random
import math

#Cartas existentes
cartas = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
print("Bem-vindo a jogo 21!")
car=int(input("Quantas cartas deseja retirar? "))
car2=int(input("Quantas o robô deve retirar? "))

print("")
print("Essas são suas cartas!")
print("")

#Cartas do usuário e valor total
def inicialCartas():
  inicial = random.sample(cartas, car)
  totalUsuario = 0
  x = 0
  while x < car:
    if inicial[x] == 'A':
      totalUsuario += 1
    elif type(inicial[x]) == str:
      totalUsuario += 10
    else:
      totalUsuario += + inicial[x]
    x = x+1   
  return inicial, totalUsuario
  
inicialCartas()
inicial, totalUsuario = inicialCartas()

print(inicial)
difUsuario = math.sqrt((totalUsuario-21)**2)


print("")
print("Essas são as cartas do robô:")
print("")

#Cartas do robo e valor total
def roboCartas():
  robo = random.sample(cartas, car2)
  totalRobo = 0
  x = 0
  while x < car2:
    if robo[x] == 'A':
      totalRobo += 1
    elif type(robo[x]) == str:
      totalRobo += 10
    else:
      totalRobo += robo[x]
    x = x+1   
  return robo, totalRobo
  
roboCartas()
robo, totalRobo = roboCartas()

print(robo)
difRobo = math.sqrt((totalRobo-21)**2)

print("")

# Definindo ganhador
if totalUsuario == totalRobo:
  print("EMPATE!")
elif  totalUsuario > 21 and totalRobo < 21:
  print("VOCÊ PERDEU :(")
elif  totalRobo > 21 and totalUsuario < 21:
  print("VOCÊ GANHOU :)")
elif difRobo<difUsuario:
  print("VOCÊ PERDEU :(")
elif difRobo>difUsuario:
  print("VOCÊ GANHOU :)")
print("")




