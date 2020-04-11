import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        take_cards = self.deck.pop()
        return take_cards


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card[1]]

    def adjust_for_ace(self):
        if self.cards[0][1] == "Ace" or self.cards[1][1] == "Ace":
            if self.value < 11:
                values["Ace"] = 11
            elif self.value > 10:
                values["Ace"] = 1


class Chips:
    def __init__(self):
        self.total = 300
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet

    def push(self):
        self.total = self.total


def take_bet(C):
    C.bet = int(input("enter your bet please : "))
    if C.total == 0 and C.bet > C.total:
        raise Exception("You got 0 money left, you lost")
    while C.bet > C.total or C.bet < 0 or not (isinstance(C.bet, int)):
        C.bet = int(input("enter your bet please : "))


def hit(D, hand):
    hand.add_cards(D.deal())
    hand.adjust_for_ace()


def hit_or_stand(D, hand):
    while True:
        hit_stand = input("do you want to hit or stand ?  ").lower()
        if hit_stand == "hit" or hit_stand == "h":
            hit(D, hand)
        else:
            print("PLAYER stand, DEALER is playing")
            return False
        return True


def show_some(player_hand, dealer_hand):
    print("PLAYER cards : ")
    print(player_hand.cards)
    print("DEALER cards : ")
    print(dealer_hand.cards[0])


def show_all(player_hand, dealer_hand):
    print("PLAYER cards : ")
    print(player_hand.cards)
    print("DEALER cards : ")
    print(dealer_hand.cards)


def player_busts(C, player_hand, dealer_hand):
    C.lose_bet()
    print(" Player BUST ")


def player_wins(C, player_hand, dealer_hand):
    C.win_bet()
    print(" Player WIN ")


def dealer_busts(C, player_hand, dealer_hand):
    C.win_bet()
    print(" Dealer BUST ")


def dealer_wins(C, player_hand, dealer_hand):
    C.lose_bet()
    print(" Dealer WIN ")


def push(C, player_hand, dealer_hand):
    print("PUSH")
    C.push()


def play_again():
    return input("do you want to play another hand ? ").lower().startswith("y")


def main():
    win = 0
    lose = 0
    tie = 0
    print("******WELCOME TO BLACKJACK GAME!******")
    print(
        "INSTRUCTION: 1)Bet should be lower than your total money or equal to it (300 is the current)"
    )
    print("2)Answer with y/n OR yes/no when you want to play another hand")
    print("3)answer with  H/S OR hit/stand  to hit or stand")
    C = Chips()
    while True:
        D = Deck()
        D.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_cards(D.deal())
        player_hand.add_cards(D.deal())
        dealer_hand.add_cards(D.deal())
        dealer_hand.add_cards(D.deal())
        take_bet(C)
        show_some(player_hand, dealer_hand)
        while hit_or_stand(D, player_hand):
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                show_all(player_hand, dealer_hand)
                player_busts(C, player_hand, dealer_hand)
                lose = lose + 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
                break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(D, dealer_hand)
            show_all(player_hand, dealer_hand)
            if dealer_hand.value > 21:
                dealer_busts(C, player_hand, dealer_hand)
                win = win + 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
            elif dealer_hand.value > player_hand.value:
                dealer_wins(C, player_hand, dealer_hand)
                lose = lose + 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
            elif dealer_hand.value < player_hand.value:
                player_wins(C, player_hand, dealer_hand)
                win = win + 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie =  {tie}")
            else:
                push(C, player_hand, dealer_hand)
                tie = tie + 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie =  {tie}")

        print(f"Your Total money ={C.total}")
        if play_again():
            continue
        else:
            print("Thanks for playing")
            print(
                f"Number of Wins  =  {win},Number of Loses =  {lose}, Number of Tie  =  {tie}"
            )
            break


main()
