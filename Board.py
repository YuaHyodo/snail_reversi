"""

This file is part of the snail_reversi

Copyright (c) 2022 YuaHyodo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

BLACK = True
WHITE = False
EMPTY = 'empty'
PASS = 'pass'

class Sq:
    def __init__(self):
        self.state = EMPTY
        #self.state_dict = {BLACK: 'X', WHITE: 'O', EMPTY: '-'}

    def change(self, color):
        self.state = color
        return

class Board:
    def __init__(self, sfen=None):
        self.size = (8, 8)#(横幅, 高さ)
        self.init_board()
        if sfen == None:
            self.set_startpos()
        else:
            self.set_sfen(sfen)

        self.check_squares = ((-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                                   (-1, 0),  (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                                   (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
                                   (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                                   (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                                   (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
                                   (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7))

    def __str__(self):
        output = ''
        k = '\n'
        state_str = {BLACK: 'x', WHITE: 'o', EMPTY: '-'}
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                output += state_str[self.squares[y][x].state]
            output += k
        return output

    def init_board(self):
        """
        [[1段目],
         [2段目],
         ・・・,
         [8段目]]
        """
        self.squares = []
        for y in range(self.size[1]):
            rank = []
            for x in range(self.size[0]):
                rank.append(Sq())
            self.squares.append(rank)
        return

    def set_startpos(self):
        self.squares[3][3].change(WHITE)
        self.squares[3][4].change(BLACK)
        self.squares[4][3].change(BLACK)
        self.squares[4][4].change(WHITE)
        self.turn = BLACK
        return

    def set_sfen(self, sfen):
        sq_states = sfen[0:65]
        turn_of = sfen[64]
        d1 = {'X': BLACK, 'O': WHITE, '-': EMPTY}
        index = 0
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.squares[y][x].state = d1[sq_states[index]]
                index += 1
        self.turn = {'B': BLACK, 'W': WHITE}[turn_of]
        return

    def change_turn(self):
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
        return

    def return_sfen(self):
        sfen = ''
        state_str = {BLACK: 'X', WHITE: 'O', EMPTY: '-'}
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                sfen += state_str[self.squares[y][x].state]
        color_str = {BLACK: 'B', WHITE: 'W'}
        sfen += color_str[self.turn]
        sfen += '1'
        return sfen

    def usix_move_to_index(self, usix_move):
        d1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        index = [int(usix_move[1]) - 1,
                     d1[usix_move[0]]]
        return index

    def index_to_usix_move(self, index):
        d1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        usix_move = d1[index[1]] + str(index[0] + 1)
        return usix_move

    def move_from_usix(self, usix_move):
        if usix_move == PASS:
            self.change_turn()
            return
        index = self.usix_move_to_index(usix_move)
        self.squares[index[0]][index[1]].change(self.turn)
        flip_list = self.flip_stones(usix_move)
        for i in flip_list:
            self.squares[i[0]][i[1]].change(self.turn)
        self.change_turn()
        return

    def is_legal(self, usix_move):
        index = self.usix_move_to_index(usix_move)
        sq = self.squares[index[0]][index[1]]
        my_color = self.turn
        if self.turn == BLACK:
            opponent_color = WHITE
        else:
            opponent_color = BLACK
        if sq.state != EMPTY:
            return False
        for i in range(len(self.check_squares)):
            if i % 7 == 0:
                opponent_stone = False
                direction_skip = False
            if direction_skip:
                continue
            index2 = self.check_squares[i]
            index3 = [(index[0] + index2[0]), (index[1] + index2[1])]
            if min(index3) < 0:
                continue
            if max(index3) > 7:
                continue
            sq = self.squares[index3[0]][index3[1]]
            if (sq.state == EMPTY) or (not opponent_stone and sq.state == my_color):
                opponent_stone = False
                direction_skip = True
                continue
            if opponent_stone and sq.state == my_color:#相手の石を挟んでいる
                return True
            if sq.state == opponent_color:
                opponent_stone = True
        return False

    def gen_legal_moves(self):
        self.legal_moves = []
        for y in range(8):
            for x in range(8):
                usix_move = self.index_to_usix_move([x, y])
                if self.is_legal(usix_move):
                    self.legal_moves.append(usix_move)
        if len(self.legal_moves) == 0:
            self.legal_moves.append(PASS)
        return self.legal_moves

    def flip_stones(self, usix_move):
        index = self.usix_move_to_index(usix_move)
        flip_index_list = []
        my_color = self.turn
        if self.turn == BLACK:
            opponent_color = WHITE
        else:
            opponent_color = BLACK
        for i in range(len(self.check_squares)):
            if i % 7 == 0:
                opponent_stone = False
                direction_skip = False
                flip_index_list_kari = [] 
            if direction_skip:
                continue
            index2 = self.check_squares[i]
            index3 = [(index[0] + index2[0]), (index[1] + index2[1])]
            if min(index3) < 0:
                continue
            if max(index3) > 7:
                continue
            sq = self.squares[index3[0]][index3[1]]
            if (sq.state == EMPTY) or ((sq.state == my_color) and (len(flip_index_list_kari) == 0)):
                opponent_stone = False
                direction_skip = True
                continue
            if sq.state == my_color:#相手の石を挟んでいる
                flip_index_list.extend(flip_index_list_kari)
                flip_index_list_kari = []
                opponent_stone = False
                direction_skip = True
                continue
            if sq.state == opponent_color:
                opponent_stone = True
                flip_index_list_kari.append(index3)
        return flip_index_list

    def is_gameover(self):
        if self.piece_sum() >= self.size[0] * self.size[1]:
            return True
        return False

    def piece_sum(self):
        pieces = 0
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.squares[y][x].state != EMPTY:
                    pieces += 1
        return pieces

    def piece_num(self):
        pieces = 0
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.squares[y][x].state == self.turn:
                    pieces += 1
        return pieces

    def opponent_piece_num(self):
        pieces = 0
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.squares[y][x].state != EMPTY and self.squares[y][x].state != self.turn:
                    pieces += 1
        return pieces

    def make_simple_feature(self):
        black = []
        white = []
        for y in range(self.size[1]):
            black_rank = []
            white_rank = []
            for x in range(self.size[0]):
                if self.squares[y][x].state == BLACK:
                    black_rank.append(1)
                    white_rank.append(0)
                elif self.squares[y][x].state == WHITE:
                    black_rank.append(0)
                    white_rank.append(1)
                else:
                    black_rank.append(0)
                    white_rank.append(0)
            black.append(black_rank)
            white.append(white_rank)
        if self.turn == BLACK:
            output = [black, white]
        else:
            output = [white, black]
        return output

if __name__ == '__main__':
    """
    ここにテストとかを書く
    """
    pass
