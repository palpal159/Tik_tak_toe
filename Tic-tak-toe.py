board = list(range(1,10))
win_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):
    while True:
        value = input('Куда поставить: ' + player_token + '? ')
        if not (value in '123456789'):
            print('Введите число от 1 до 9.')
            continue
        value = int(value)
        if str(board[value -1]) in'XO':
            print('Эта клетка уже занята')
            continue
        board[value - 1] = player_token
        break

def check_win():
    for i in win_coord:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[0] - 1]
    else:
        return False

def main():
  counter = 0
  while True:
      draw_board()
      if counter % 2 == 0:
          take_input('X')
      else:
          take_input('O')
      if counter > 3:
          winner = check_win()
          if winner:
              draw_board()
              print(winner, 'выиграл!')
              break
      counter += 1
      if counter > 8:
          draw_board()
          print('Ничья!')
          break

main()


