from os import truncate
import random

def show():
  print('')
  print(lista[0],lista[1],lista[2])
  print(lista[3],lista[4],lista[5])
  print(lista[6],lista[7],lista[8])
  print('')


def step1():
  lista[start] = 'x'

def verifyStart():
  if start == 0:
    return 8
  elif start == 2:
    return 6
  elif start == 6:
    return 2
  else:
    return 0

def step2():
  opposite = verifyStart()
  if lista[opposite] == 'o':
    for i in corner:
      if lista[i] != 'x' and lista[i] != 'o':
        lista[i] = 'x'
        break
      else:
        continue
  else:
    lista[opposite] = 'x'

def verify():
  indice = 9
  for i in possibilities:
    controlO = 0
    controlX = 0
    for j in i:
      if lista[j] == 'o':
        controlO += 1
      elif lista[j] == 'x':
        controlX += 1
      else:
        indice = j
    if controlX == 2 and controlO != 1:
      return indice
  for i in possibilities:
    controlO = 0
    controlX = 0
    for j in i:
      if lista[j] == 'o':
        controlO += 1
      elif lista[j] == 'x':
        controlX += 1
      else:
        indice = j
    if controlO == 2 and controlX != 1:
      return indice

  return indice

def stepFinal():
  choice = verify()

  if choice != 9:
    lista[choice] = 'x'
  else:
    for i in corner:
      if lista[i] != 'x' and lista[i] != 'o':
        lista[i] = 'x'
        break


def move():
    print('Seu movimento!')
    index = int(input("Sua jogada: "))
    lista[index - 1] = 'o'


corner = [0, 2, 6, 8]
start = random.sample(corner, 1)[0]

# possibilities = [[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]
possibilities = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

def move():
  lista[int(input())-1] = 'o'

def continua_jogo():
  decisao = input("Deseja tentar nocamente? (Sim/Não) ").lower()
  return decisao

def velha(lista):
  for i in lista:
    if i != 'x' and i != 'o':
      return False
  return True


def verify_win():
  for i in possibilities:
    controlX = 0
    for j in i:
      if lista[j] == 'x':
        controlX += 1
    if controlX == 3:
      return True
  return False




continuar = True

while continuar == True:
  lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  jogo = 0
  while jogo < 1:
    jogo += 1
    print('Inicio do Jogo!\nEu sou o X e eu começo!')

    # if verify_win():
    #   show()
    #   print("X ganhou")
    #   break
    # elif velha(lista):
    #   show()
    #   print("Velha")
    #   break

#----------------------------------------------------
    step1()
    show()
    move()

    step2()
    show()
    move()

    stepFinal()
    if verify_win():
      show()
      print("X ganhou")
      break
    elif velha(lista):
      show()
      print("Velha")
      break
    show()
    move()

    stepFinal()
    if verify_win():
      show()
      print("X ganhou")
      break
    elif velha(lista):
      show()
      print("Velha")
      break

    show()
    move()


    stepFinal()
    if verify_win():
      show()
      print("X ganhou")
      break
    elif velha(lista):
      show()
      print("Velha")
      break

    show()





  game = continua_jogo()
  if game.startswith('S') or game.startswith('s'):
    print('Boa sorte!')
    continuar = True
  elif game.startswith('N') or game.startswith('n'):
    print('Finalizando jogo!')
    continuar = False
    break
  else:
    print('Digite uma opção valida!')