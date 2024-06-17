import pytest
import random
import time
from project import create_boards, play_loteria, check_winner
cards = [
    "El gallo", "El diablito", "La dama", "El catrín", "El paraguas",
    "La sirena", "La escalera", "La botella", "El barril", "El árbol",
    "El melón", "El valiente", "El gorrito", "La muerte", "La pera",
    "La bandera", "El bandolón", "El violoncello", "La garza", "El pájaro",
    "La mano", "La bota", "La luna", "El cotorro", "El borracho",
    "El negrito", "El corazón", "La sandía", "El tambor", "El camarón",
    "Las jaras", "El músico", "La araña", "El soldado", "La estrella",
    "El cazo", "El mundo", "El Apache", "El nopal", "El alacrán",
    "La rosa", "La calavera", "La campana", "El cantarito", "El venado",
    "El Sol", "La corona", "La chalupa", "El pino", "El pescado",
    "La palma", "La maceta", "El arpa", "La rana"
]

class LoteriaDeck():
    def __init__(self, cards):
        random.shuffle(cards)
        self.cards = cards

    def draw_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

random.seed(time.time())
user_names  = ["Chaba", "Diana", "Moy"]
loteria_deck = LoteriaDeck(cards)
boards = create_boards(user_names, loteria_deck)


def test_create_boards():
    assert len(boards) == 3
    assert boards[0].user_name == "Chaba"
    assert boards[1].user_name == "Diana"
    assert boards[2].user_name == "Moy"

def test_winner():
    assert check_winner(boards) == False
    boards[0].board_binary = [True, True, True, True]
    boards[0].win = True
    assert check_winner(boards) == ["Chaba"]

def test_play_loteria():
    random.seed(0)
    user_names  = ["Chaba", "Diana", "Moy"]
    loteria_deck = LoteriaDeck(cards)
    loteria_deck.cards = cards
    boards = create_boards(user_names, loteria_deck)
    boards[2].board = ["El gallo", "El diablito", "La dama", "El catrín"]
    assert play_loteria(loteria_deck, boards) == ["Moy"]
