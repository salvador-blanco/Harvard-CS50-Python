import random
import time

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

def main():
    random.seed(time.time())
    user_names  = get_user_names()
    loteria_deck = LoteriaDeck(cards)
    boards = create_boards(user_names, loteria_deck)
    winners = play_loteria(loteria_deck, boards)

    for board in boards:
        board.print_board()
        print()
    print()
    print("The winner is: {}".format(winners))
    print()
    print()
    print('Remmining cards: ')
    print(loteria_deck.cards)


def play_loteria(loteria_deck, boards):
    for card in range(len(loteria_deck)):
        card = loteria_deck.draw_card()
        for board in boards:
            board.check_card(card)
        winners = check_winner(boards)
        if winners:
            return winners

def check_winner(boards):
    winners_list = []
    for board in boards:
        if board.win:
            winners_list.append(board.user_name)
    if len(winners_list):
        return winners_list
    else:
        return False

def get_user_names() -> list:
    user_names = []
    while(True):
        print("Writte user name, input (q) in there are no more players")
        name = input("Name: ")
        print()
        if name == "q":
            break
        user_names.append(name)

    if len(user_names) > 0:
        return (user_names)
    else:
        raise ValueError("There must me at least one user")

def create_boards(user_names, loteria_deck):
    loteria_boards = []
    for user_name in user_names:
        loteria_boards.append(LoteriaBoard(user_name, loteria_deck))
        print()
    return loteria_boards


class LoteriaBoard():
    def __init__(self, user_name, loteria_deck, w=2, h=2):
        self.win = False
        self.user_name = user_name
        self.w = w
        self.h = h
        self.board = random.sample(loteria_deck.cards, k=self.w*self.h)
        self.board_binary = [False for _ in range(len(self.board))]
        self.max_card_name_lenght = max([len(card) for card in self.board]) + 3
        self.print_board()


    def print_board(self):
        print(self.user_name + ":")
        for i in range(self.h):
            row = self.board[i*self.w: (i+1)*self.w]
            row_binary = self.board_binary[i*self.w: (i+1)*self.w]

            row_formated = []
            for card, status in zip(row, row_binary):
                if status == True:
                    marker = "  "
                else:
                    marker = " 0"

                row_formated.append(f"{card}{marker}".ljust(self.max_card_name_lenght))

            print(row_formated)


    def check_card(self, card):
        if card in self.board:
            card_index = self.board.index(card)
            self.board_binary[card_index] = True
            print(f" Card {card} in {self.user_name}'s board")
            self.win = not False in self.board_binary

class LoteriaDeck():
    def __init__(self, cards):
        random.shuffle(cards)
        self.cards = cards

    def draw_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

if __name__ == "__main__":
    main()
