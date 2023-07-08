tag: user.chess
-

short castle: "O-O\n"
long castle: "O-O-O"

<user.chess_move>: insert(chess_move)

# promotion
pawn {user.chess_file} eight {user.chess_piece}:
	insert("{chess_file}8={chess_piece}")

pawn {user.chess_file} <user.chess_capture> {user.chess_file} eight {user.chess_piece}:
	insert("{chess_file_1}x{chess_file_2}8={chess_piece}")
