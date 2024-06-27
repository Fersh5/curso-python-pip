import random;

options=('piedra','papel','tijera')

computer_wins=0
user_wins=0
rounds=1

while True:
  print(f'{"•"*20:^}')
  print(f'{"ROUND":^12} {rounds:^5}')
  print(f'{"•"*20:^}')
  print(f'{"Computer wins: ":<12} {computer_wins:^5}')
  print(f'{"User wins: ":<12} {user_wins:^7}\n')


  user_opt = (input('piedra, papel o tijera => '))
  user_opt = user_opt.lower()

  if not user_opt in options:
    print('Esa opcion no es valida')
    continue
  c_opt = random.choice(options)

  print(f'User option => {user_opt}')
  print(f'Computer option => {c_opt}\n')

  if user_opt == c_opt:
    print('Empate\n')
  elif user_opt == 'piedra':
    if c_opt == 'tijera':
      print('piedra gana a tijera')
      print('User gano!')
      user_wins+=1
    else:
      print('Papel gana a piedra')
      print('Computer gano!!')
      computer_wins+=1
  elif user_opt == 'papel':
    if c_opt == 'piedra':
      print('papel gana a piedra')
      print('User gano !')
      user_wins+=1
    else:
      print('tijera gana a piedra')
      print('Computer gano !')
      computer_wins+=1
  elif user_opt == 'tijera':
    if c_opt == 'piedra':
      print('piedra gana a tijera')
      print('Computer gana !')
      computer_wins+=1
    else:
      print('tijera gana a papel')
      print('User gana !')
      user_wins+=1
  rounds += 1
  if computer_wins == 2:
    print('El ganador es la computadora')
    break
  if user_wins == 2:
    print('El ganador es el usuario')
    break