from talon import Context, Module

ctx = Context()
mod = Module()

mod.list("chess_piece")
mod.list("chess_file", desc="A column of the chessboard")
mod.list("chess_rank", desc="A row of the chessboard")
mod.list("chess_check", desc="Type of check")

mod.tag("chess", desc="Enable commands to insert chess moves")

ctx.lists["self.chess_piece"] = {
    "king": "K",
    "queen": "Q",
    "rook": "R",
    "bishop": "B",
    "knight": "N",
    "pawn": "",
}

ctx.lists["self.chess_file"] = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "air": "a",
    "bat": "b",
    "cap": "c",
    "drum": "d",
    "each": "e",
    "fine": "f",
    "gust": "g",
    "harp": "h",
}

ctx.lists["self.chess_rank"] = {
    name: str(digit)
    for digit, name in enumerate(
        "one two three four five six seven eight".split(), start=1
    )
}

ctx.lists["self.chess_check"] = {
    "check": "+",
    "mate": "#",
}


@mod.capture(rule="take | takes")
def chess_capture(_) -> str:
    """Indicate the piece is capturing another piece."""
    return "x"


@mod.capture(rule="{self.chess_file} {self.chess_rank}")
def chess_square(m) -> str:
    """A square on the chessboard."""
    return "".join(m)


@mod.capture(rule="{self.chess_piece} [{self.chess_file}] [{self.chess_rank}]")
def chess_unambiguous_piece(m) -> str:
    """Name a piece to move in SAN, disambiguating if necessary."""
    return "".join(m)


@mod.capture(
    rule="(<self.chess_unambiguous_piece> | <self.chess_square>) [<self.chess_capture>] <self.chess_square> [{self.chess_check}]"
)
def chess_move(m) -> str:
    """A chess move in algebraic notation or UCI."""
    return "".join(m)
