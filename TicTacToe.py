import os, sys
run = True
error = False
win = False
turn = 0

row_1 = [1, 2, 3]
row_2 = [4, 5, 6]
row_3 = [7, 8, 9]

board = [
   row_1,
   row_2,
   row_3
]
#                                         this is game start up and call to action
print("let's play Tic Tac Toe\n\n")
for row in board:
   for slot in row:
       print(f"{slot} ", end=' ')
   print()
print(' ')

players = input("to quit enter 'Q'\nplayer one name: "), input('player two name: ')

tt = ['this is a place hold', input(players[0] + ', enter playable number: ')]

if 'q' in tt:
   sys.exit()
a = tt[turn + 1]
                                          # function to process turn input
def game():

   global error, run, turn, a, win
                                   # this processes player one input
   if turn % 2 == 0:
       if int(a) in row_1:
           row_1[int(a) - 1] = 'X'
       elif int(a) in row_2:
           row_2[int(a) - 4] = 'X'
       elif int(a) in row_3:
           row_3[int(a) - 7] = 'X'
       else:
           print('invalid move, ', tt[0])
           error = True
                                 # this processes player two input
   elif turn % 2 == 1:

       if int(a) in row_1:
           row_1[int(a) - 1] = 'O'
       elif int(a) in row_2:
           row_2[int(a) - 4] = 'O'
       elif int(a) in row_3:
           row_3[int(a) - 7] = 'O'
       else:
           print('invalid move, ', players[1])
           error = True

   else:
       print('function error')
       error = True

game()
        # this organizes data for wining outcomes, and continues program.
while not error:

   col_1 = [row_1[0], row_2[0], row_3[0]]
   col_2 = [row_1[1], row_2[1], row_3[1]]
   col_3 = [row_1[2], row_2[2], row_3[2]]
   back_dag = [row_1[0], row_2[1], row_3[2]]
   for_dag = [row_1[2], row_2[1], row_3[0]]

   columns = [
       col_1,
       col_2,
       col_3
   ]
                        # this process runs if player one has won
   if turn % 2 == 0:

       for row in board:
           for x in row:
               if row.count('X') == 3:
                   print(players[0], 'wins!')
                   win = True

       if col_1.count('X') == 3:
           print(players[0], 'wins!')
           win = True
       if col_2.count('X') == 3:
           print(players[0], 'wins!')
           win = True
       if col_3.count('X') == 3:
           print(players[0], 'wins!')
           win = True
       if back_dag.count('X') == 3:
           print(players[0], 'wins!')
           win = True
       if for_dag.count('X') == 3:
           print(players[0], 'wins!')
           win = True
                             # this runs if player two has won
   elif turn % 2 == 1:

       for row in board:
           for x in row:
               if row.count('O') == 3:
                   print(players[1], 'wins!')
                   win = True
       if col_1.count('O') == 3:
           print(players[1], 'wins!')
           win = True
       if col_2.count('O') == 3:
           print(players[1], 'wins!')
           win = True
       if col_3.count('O') == 3:
           print(players[1], 'wins!')
           win = True
       if back_dag.count('O') == 3:
           print(players[1], 'wins!')
           win = True
       if for_dag.count('O') == 3:
           print(players[1], 'wins!')
           win = True

               # This transfers player input to game board and updates game
   if not win:

       turn += 1
       print("let's play Tic Tac Toe\n turn " + str(turn) + "\n\n")
       for row in board:
           for slot in row:
               print(f"{slot} ", end=' ')
           print()
           print(' ')
       new_input = input(players[turn % 2] + ', enter a playable number: ') # .upper for responce to eliminate repeat qQ
       tt.append(new_input)
       # this is for quiting game when player responds "Q" to quit
       if 'Q' in new_input:
           sys.exit()
       if 'q' in new_input:
           sys.exit()
                            # this runs if game board is full and no winner
       if turn >= 8:
           print("it's a draw")
           restart = input("to play again enter 'R'\nto quit enter 'Q'\n\n").upper()
           tt.append(restart)
           if 'Q' in tt:
               sys.exit()
           elif 'R' in tt:
               os.execv(sys.executable, ['python'] + sys.argv)

       a = tt[turn + 1]
       game()
                                # this runs if the game is won
   if win:

       for row in board:
           for slot in row:
               print(f"{slot} ", end=' ')
           print()
       restart = input("to play again enter 'R'\nto quit enter 'Q'\n\n").upper()
       tt.append(restart)
       if 'Q' in tt:
           sys.exit()
       elif 'R' in tt:
           os.execv(sys.executable, ['python'] + sys.argv)

                # this runs if player input is not allowed
while error:

   print('turn ' + str(turn) + "\n\n")
   for row in board:
       for slot in row:
           print(f"{slot} ", end=' ')
       print()

   tt[turn + 1] = input(tt[turn % 2] + ', try again: ')
   if 'q' or 'Q' in tt:
       sys.exit()
   a = tt[turn + 1]
   error = False
   game()

# this has been Levi's Tic Tac Toe game