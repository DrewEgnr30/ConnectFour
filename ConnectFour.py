

import numpy as np

import matplotlib.pyplot as plt

import re

class ConnectFour:

    def __init__(self):

        self.columns = 7
        self.rows = 6
        self.column = None
        self.row = None
        self.board = None
        self.player1 = 1
        self.player2 = 2
        self.currentplayer = 1
        self.winner = None

    def initializeBoard(self):

        self.board = np.zeros([self.rows, self.columns])

    def showBoard(self):

        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.pcolor(self.board, edgecolors = 'k', cmap = 'jet')
        plt.gca().invert_yaxis()
        plt.show()

    # def newTurn(self):
    #
    #     for turn in range(2):
    #
    #         if self.currentplayer == self.player1:
    #
    #             self.makeMove()
    #             self.currentplayer = self.player2
    #             self.showBoard()
    #
    #         else:
    #
    #             self.makeMove()
    #             self.currentplayer = self.player1
    #             self.showBoard()
    #             break

    def player1Turn(self):

        self.currentplayer = self.player1
        self.makeMove()
        self.showBoard()

    def player2Turn(self):

        self.currentplayer = self.player2
        self.makeMove()
        self.showBoard()

    def makeMove(self):

        continue_flag = 1

        while continue_flag:
            self.row = None
            prompt = "Player {}, which column would you like to place your piece into? (1-7)".format(self.currentplayer)
            player_move = input(prompt)
            regex = re.match("(^[1-7]{1}$)", player_move)

            if regex == None:

                    self.column = -1
            else:

                self.column = int(player_move) -1

            ## check to see if it is a valid move or the if the current player has won
            result = self.checkMove()

            if result == "valid":

                count = 0

                for r in self.board[:, self.column]:

                    if r != 0:

                        self.row = count - 1
                        break

                    count += 1

                if self.row == None:

                    self.row = self.rows - 1

                self.board[self.row, self.column] = self.currentplayer
                continue_flag = 0

            elif result == "invalid":

                continue_flag = 1
                print("Invalid move.  Please choose a number between 1 and 7")


    def checkMove(self):

        regex = re.match("([0-6]{1})", str(self.column))

        if regex != None and 0 in self.board[:, self.column]:

            result = "valid"

        else:

            result = "invalid"

        return result

    def checkWin(self):

        column_sum_array = None
        row_sum_array = None
        diagonal_ur_sum_array = None
        diagonal_dr_sum_array = None
        row_sum = None
        column_sum = None
        diagonal_ur_sum = None
        diagonal_dr_sum = None
        rows_ur = None
        columns_ur = None
        rows_dr = None
        columns_dr = None

        ### Check for horizontal win

        for c in range(self.columns - 3):

            column_sum_array = [self.board[self.row, c], self.board[self.row, c + 1], self.board[self.row, c + 2], self.board[self.row, c + 3]]

            if 0 not in column_sum_array:

                column_sum = sum(column_sum_array)

                if column_sum / self.currentplayer == 4:

                    return self.currentplayer

        ### Check for vertical win

        for r in range(self.rows - 3):

            row_sum_array = [self.board[r, self.column], self.board[r + 1, self.column], self.board[r + 2, self.column], self.board[r + 3, self.column]]

            if 0 not in row_sum_array:

                row_sum = sum(row_sum_array)

                if row_sum / self.currentplayer == 4:

                    return self.currentplayer

        ### Check for diagonal win

        ### Check up-right diagonal

        rows_ur = [3, 4, 5]
        columns_ur = [0, 1, 2, 3]

        for r in rows_ur:

            for c in columns_ur:

                diagonal_ur_sum_array = [self.board[r, c], self.board[r - 1, c + 1], self.board[r - 2, c + 2], self.board[r - 3, c + 3]]

                if 0 not in diagonal_ur_sum_array:

                    diagonal_ur_sum = sum(diagonal_ur_sum_array)

                    if diagonal_ur_sum / self.currentplayer == 4:

                        return self.currentplayer

        ### Check down-right diagonal

        rows_dr = [0, 1, 2]
        columns_dr = [0, 1, 2, 3]

        for r in rows_dr:

            for c in columns_dr:

                diagonal_dr_sum_array = [self.board[r, c], self.board[r + 1, c + 1], self.board[r + 2, c + 2], self.board[r + 3, c + 3]]

                if 0 not in diagonal_dr_sum_array:

                    diagonal_dr_sum = sum(diagonal_dr_sum_array)

                    if diagonal_dr_sum / self.currentplayer == 4:

                        return self.currentplayer

        return 0

    def playGame(self):

        self.initializeBoard()
        self.showBoard()

        for r in range(int((self.rows * self.columns) / 2)):

            self.player1Turn()

            if self.checkWin() == self.player1:

                self.winner = self.player1
                break

            self.player2Turn()

            if self.checkWin() == self.player2:

                self.winner = self.player2
                break

        if self.winner != None:

            print("The winner is Player {}!!!".format(self.winner))

        else:

            print("Match is a draw.")




if __name__ == "__main__":

    game = ConnectFour()
    game.playGame()

