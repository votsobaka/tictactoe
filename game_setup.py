from random import randint, choice
import time
import os


class TicTacToe:
    def __init__(self):
        self.game_board = [[" ", " ", " "],
                           [" ", " ", " "],
                           [" ", " ", " "]]
        self.clear = lambda: os.system("cls")
        self.p_list = ["pc", "player"]
        self.turn = 1

    def start(self):
        ### выше так же доска заполняется, можно функцию вынести
        self.game_board = [[" ", " ", " "],
                           [" ", " ", " "],
                           [" ", " ", " "]]
        print("Welcome to Tic-Tac-Toe!")
        
        ### печать доски - лучше функцию, ты много раз этот код используешь
        print("   1   2   3"
              f"\n1: {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} "
              f"\n-------------"
              f"\n2: {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} "
              f"\n-------------"
              f"\n3: {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]} ")
        
		### получается, что у тебя вызовы функций-ходов все в цепочке, лучше, думаю, было бы здесь сделать цикл где вызывать 
		### функции-ходы, что-то наподобие:
		### while game-is-not-over
		###		player_move
		###		check_win
		###		pc_move
		###		check_win
        
        self.rnd_first()

    def rnd_first(self):
        print("\nCalculating who's gonna have the first turn...")
        time.sleep(1)
        rnd = choice(self.p_list)
        if rnd == "player":
            self.player_move(rnd)
        else:
            self.pc_move(rnd)
        return

	### в целом выглядит, что ход игрока и компа могли бы иметь общий код-функцию.
	### она бы ставила нужный символ в выбранную клетку, например. типа
    ###
    ### def common_move
    ###     if player
    ###         move = get_player_move # внутри get_player_move функции можно считывание инпута делать
    ###     else
    ###         move = get_pc_move # внутри get_pc_move - рандомный ход
    ###     
    ###     check_move(move) # проверка, что ход валиден
    ###     дальше ставим в доску правильный символ, передаём ход и что там ещё надо делать
    ###     
    ###     ну и часть с получением мува и чек-мувом в цикл забодяжить, чтобы вызывать это до тех пор, пока не попадём в пустую клетку
    
    
    def player_move(self, order):
        move = input("\nIt's your turn! Choose row and column by numbers (without spaces): ")
        move = list(move)
        if self.game_board[int(move[0]) - 1][int(move[1]) - 1] == "X" or self.game_board[int(move[0]) - 1][int(move[1]) - 1] == "0":
            print("Please pick free space!")
            self.player_move(order)
        else:
            if order == "player":
                self.game_board[int(move[0]) - 1][int(move[1]) - 1] = "X"
            else:
                self.game_board[int(move[0]) - 1][int(move[1]) - 1] = "0"
            self.clear()
            print("\n   1   2   3"
                  f"\n1: {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} "
                  f"\n-------------"
                  f"\n2: {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} "
                  f"\n-------------"
                  f"\n3: {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]} ")
        time.sleep(1)
        self.turn = 1
        self.next_turn(order, turn=self.turn)
        return

    def pc_move(self, order):
        print("It's COMP turn.")
        time.sleep(1)
        move = [randint(0, 2), randint(0, 2)]
        while self.game_board[move[0]][move[1]] == "X" or self.game_board[move[0]][move[1]] == "0":
            move = [randint(0, 2), randint(0, 2)]
        else:
            if order == "pc":
                self.game_board[move[0]][move[1]] = "X"
            else:
                self.game_board[move[0]][move[1]] = "0"
            self.clear()
            print("\n   1   2   3"
                  f"\n1: {self.game_board[0][0]} | {self.game_board[0][1]} | {self.game_board[0][2]} "
                  f"\n-------------"
                  f"\n2: {self.game_board[1][0]} | {self.game_board[1][1]} | {self.game_board[1][2]} "
                  f"\n-------------"
                  f"\n3: {self.game_board[2][0]} | {self.game_board[2][1]} | {self.game_board[2][2]} ")
        time.sleep(1)
        self.turn = 0
        self.next_turn(order, turn=self.turn)
        return

    def next_turn(self, order, turn):
        empty_space = " "
        check_list = str(self.game_board)
        check = self.check_win_condition(self.game_board)
        if check:
            print("Game finished!")
            if turn == 1:
                print("You won!")
            elif turn == 0:
                print("PC won!")
            # TODO: add continue option
            # cont = input("Would you like to play again? (y/n)").lower()
            # if cont == "y":
            #     self.start()
            #     return
            # else:
            #     print("Thank you for playing!")
                return
        elif not check and empty_space not in check_list:
            print("Game finished! It's a tie!")
            return
        else:
            if turn == 1:
                self.pc_move(order)
                return
            elif turn == 0:
                self.player_move(order)
                return

    def check_win_condition(self, board):
        t_board = list(zip(*board))
        for x in range(len(board)):
            if board[x][:3] == ["X", "X", "X"] or board[x][:3] == ["0", "0", "0"]:
                return True
            elif t_board[:3][x] == ("X", "X", "X") or t_board[:3][x] == ("0", "0", "0"):
                return True
        if board[0][0] != " " and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return True
        elif board[2][0] != " " and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            return True
        else:
            return False
