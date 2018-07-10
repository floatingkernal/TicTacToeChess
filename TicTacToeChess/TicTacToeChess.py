class Piece(object):
	"""docstring for Piece"""
	def __init__(self, Player):
		super(Piece, self).__init__()
		self.Player = Player
		self.x = None
		self.y = None

	def val_spot(self, x, y):
		if x >= 0 and x < 4 and y >= 0 and y < 4:
			return True
		else:
			return False

	def move(self,x,y, gameboard, val_moves):
		if (x,y) in val_moves:
			if self.x != None and self.y != None:
				gameboard.board[self.x][self.y] = None
			kill = gameboard.get_piece(x,y)
			if kill != None:
				gameboard.kill_piece(kill)
			self.x = x
			self.y = y
			gameboard.set_piece(self, x, y)
			return True
		else:
			return False
		
class Rook(Piece):
	"""docstring for Rook"""

	def potential_place(self,gameboard): #return {(x,y)}
		# if piece not on board, place pice anywhere st no other piece is there
		if (self.x == None or self.y == None):
			return gameboard.get_empty_spots()
		# else if turn > 3, move piece based on its rule
		elif gameboard.turn > gameboard.min_turn:
			res = set()
			moves_set = [[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
			for i in range(1, 4):
				for move in moves_set:
					if move[2] == 0:
						new_x = self.x+i*move[0]
						new_y = self.y+i*move[1]
						if self.val_spot(new_x, new_y):
							p = gameboard.get_piece(new_x, new_y)
							if p == None:
								res.add((new_x, new_y))
							elif p.Player != self.Player:
								res.add((new_x, new_y))
								move[2] = 1
							elif p.Player == self.Player:
								move[2] = 1
			return res
		else:
			return set()

	def __str__(self):
		return "P-{} Rook".format(self.Player)

class Knight(Piece):
	"""docstring for Knight"""
	p_moves = [(1,2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]

	def potential_place(self,gameboard): #return {(x,y)}
		# if piece not on board, place pice anywhere st no other piece is there
		if (self.x == None or self.y == None):
			return gameboard.get_empty_spots()
		# else if turn > 3, move piece based on its rule
		elif gameboard.turn > gameboard.min_turn:
			res = set()
			for m in self.p_moves:
				new_x = m[0] + self.x
				new_y = m[1] + self.y
				if self.val_spot(new_x, new_y):
					piece = gameboard.get_piece(new_x, new_y)
					if piece != None:
						if piece.Player != self.Player:
							res.add((new_x, new_y))
					else:
						res.add((new_x,new_y))
			return res
		else:
			return set()

	def __str__(self):
		return "P-{} Knight".format(self.Player)

class Biship(Piece):
	"""docstring for Biship"""

	def potential_place(self,gameboard): #return {(x,y)}
		# if piece not on board, place pice anywhere st no other piece is there
		if (self.x == None or self.y == None):
			return gameboard.get_empty_spots()
		# else if turn > 3, move piece based on its rule
		elif gameboard.turn > gameboard.min_turn:
			res = set()
			moves_set = [[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0]]
			for i in range(1, 4):
				for move in moves_set:
					if move[2] == 0:
						new_x = self.x+i*move[0]
						new_y = self.y+i*move[1]
						if self.val_spot(new_x, new_y):
							p = gameboard.get_piece(new_x, new_y)
							if p == None:
								res.add((new_x, new_y))
							elif p.Player != self.Player:
								res.add((new_x, new_y))
								move[2] = 1
							elif p.Player == self.Player:
								move[2] = 1
			return res
		else:
			return set()

	def __str__(self):
		return "P-{} Biship".format(self.Player)

class Pawn(Piece):
	"""docstring for Pawn"""
	def __init__(self, Player):
		super(Pawn, self).__init__(Player)
		self.direction = Player - 1
		
	def move(self,x,y, gameboard, val_moves):
		if (x, y) in val_moves: 
			if x == 0:
				self.direction = 0
			elif x == 3:
				self.direction = 1
		return super(Pawn, self).move(x, y, gameboard, val_moves)

	def potential_place(self,gameboard): #return {(x,y)}
		# if piece not on board, place pice anywhere st no other piece is there
		if (self.x == None or self.y == None):
			return gameboard.get_empty_spots()
		# else if turn > 3, move piece based on its rule
		elif gameboard.turn > gameboard.min_turn:
			res = set()
			if self.direction == 0:
				# move fwd
				if self.val_spot(self.x+1, self.y):
					p = gameboard.get_piece(self.x+1, self.y)
					if p == None:
						res.add((self.x+1, self.y))
				if self.val_spot(self.x+1, self.y+1):
					p = gameboard.get_piece(self.x+1, self.y+1)
					if p != None and p.Player != self.Player:
						res.add((self.x+1, self.y+1))
				if self.val_spot(self.x+1, self.y-1):
					p = gameboard.get_piece(self.x+1, self.y-1)
					if p != None and p.Player != self.Player:
						res.add((self.x+1, self.y-1))
			else:
				# move bwd
				if self.val_spot(self.x-1, self.y):
					p = gameboard.get_piece(self.x-1, self.y)
					if p == None:
						res.add((self.x-1, self.y))
				if self.val_spot(self.x-1, self.y+1):
					p = gameboard.get_piece(self.x-1, self.y+1)
					if p != None and p.Player != self.Player:
						res.add((self.x-1, self.y+1))
				if self.val_spot(self.x-1, self.y-1):
					p = gameboard.get_piece(self.x-1, self.y-1)
					if p != None and p.Player != self.Player:
						res.add((self.x-1, self.y-1))
			return res

		else:
			return set()

	def __str__(self):
		return "P-{} Pawn".format(self.Player)

class GameBoard(object):
	"""docstring for GameBoard"""
	min_turn = 2*2 -1
	board = [[None,None,None,None],
			 [None,None,None,None],
			 [None,None,None,None],
			 [None,None,None,None]]
	turn = 0
	cur_player = 1 # player 1 or player 2
	piece_set = [[Biship(1), Knight(1), Pawn(1), Rook(1)],
				 [Biship(2), Knight(2), Pawn(2), Rook(2)]]
	val_piece = ["B","K","P","R"]

	def __init__(self):
		super(GameBoard, self).__init__()

	def get_piece(self, x, y):
		return self.board[x][y]
	def set_piece(self, piece, x, y):
		self.board[x][y] = piece

	def get_empty_spots(self):
		res = set()
		for x in range(len(self.board)):
			for y in range(len(self.board[x])):
				if self.board[x][y] == None:
					res.add((x,y))
		return res

	def get_filled_spots(self):
		res = set()
		for x in range(len(self.board)):
			for y in range(len(self.board[x])):
				if self.board[x][y] != None:
					res.add((x,y))
		return res

	def kill_piece(self, piece):
		self.board[piece.x][piece.y] = None
		piece.x = None
		piece.y = None

	def check_win(self):
		res = False
		win_con = [ {(0,0),(0,1),(0,2),(0,3)},
					{(1,0),(1,1),(1,2),(1,3)},
					{(2,0),(2,1),(2,2),(2,3)},
					{(3,0),(3,1),(3,2),(3,3)},
					{(0,0),(1,0),(2,0),(3,0)},
					{(0,1),(1,1),(2,1),(3,1)},
					{(0,2),(1,2),(2,2),(3,2)},
					{(0,3),(1,3),(2,3),(3,3)},
					{(0,0),(1,1),(2,2),(3,3)},
					{(0,3),(1,2),(2,1),(3,0)}]
		filled_spots = self.get_filled_spots()
		
		for con in win_con:
			m_win = all(spot in filled_spots for spot in con)		
			if m_win:
				pieces = []
				for spot in con:
					p = self.get_piece(spot[0], spot[1])
					pieces.append(p)
				player = pieces[0].Player
				res = all(p.Player == player for p in pieces)
		return res

	def print_play_turn(self):
		
		# select a piece
		select_piece = input("Pick one piece: B (Biship), K (Knight), P (Pawn), R (Rook)\n")
		if select_piece.upper() in self.val_piece:
			piece = self.piece_set[self.cur_player - 1][self.val_piece.index(select_piece.upper())]
			print("Here are valid moves for this piece:")
			val_spots = piece.potential_place(self)
			print(val_spots)
			in_spot = input("Select x, y pair from this set:\n")
			spot = in_spot.split();
			if len(spot) == 2:
				x = int(spot[0])
				y = int(spot[1])
				if (x, y) in val_spots:
					#move piece
					if piece.move(x, y, self, val_spots):
						print("Piece Moved Successfully\n")
						# change player
						if self.cur_player == 1:
							self.cur_player = 2
						elif self.cur_player == 2:
							self.cur_player = 1
						self.turn += 1

					else:
						print("Piece could not be moved")
				else: 
					print("{0} is not a valid spot".format(in_spot))



		else:
			print("{0} is not a Valid Piece".format(select_piece))

		# move piece
		# change player

	def __str__(self):
		max_len = 11
		half_len_empty_str = " " * (max_len//2)
		pieces = []
		for i in range(4):
			for j in range(4):
				piece = self.get_piece(i,j)
				str_piece = str(piece) + " " * (max_len-len(str(piece)))
				pieces.append(str_piece)
		grid_row1 = "|0|{0}|{1}|{2}|{3}|".format(pieces[0],pieces[1],pieces[2],pieces[3])
		grid_row2 = "|1|{0}|{1}|{2}|{3}|".format(pieces[4],pieces[5],pieces[6],pieces[7])
		grid_row3 = "|2|{0}|{1}|{2}|{3}|".format(pieces[8],pieces[9],pieces[10],pieces[11])
		grid_row4 = "|3|{0}|{1}|{2}|{3}|".format(pieces[12],pieces[13],pieces[14],pieces[15])
		grid_row0 = "| |{0}|{1}|{2}|{3}|".format(half_len_empty_str + "0"+ half_len_empty_str,
												half_len_empty_str + "1"+ half_len_empty_str,
												half_len_empty_str + "2"+ half_len_empty_str,
												half_len_empty_str + "3"+ half_len_empty_str)
		grid_row5 = "+-+{0}+{0}+{0}+{0}+".format("-"*max_len)
		res = "Current Player: {6} Turn: {7}, Pieces move after turn {8}\n{5}\n{0}\n{5}\n{1}\n{5}\n{2}\n{5}\n{3}\n{5}\n{4}\n{5}\n".format(
			grid_row0, grid_row1, grid_row2, grid_row3, grid_row4, grid_row5, self.cur_player, self.turn, self.min_turn)
		return res
		


def clear():
	print("\n"*100)
	pass

def main():
	clear()
	game = GameBoard()
	while not game.check_win():
		print(game)
		game.print_play_turn()
	print(game)
	print("Game Over, Player {} wins!".format("1" if game.cur_player != 1 else "2"))

if __name__ == '__main__':
	main()