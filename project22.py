import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing=True
class Card:
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
    def __str__(self):
        return self.ranks+"of"+self.suits

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        self.player=random.sample(self.deck,2)
        self.dealer=random.sample(self.deck,2)

        return self.player,self.dealer

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.extend(card)
        for i in range(0, len(card)):
            self.value += values[card[i][1]]

    def adjust_for_ace(self):
        if(self.cards[0][1]=="Ace" or self.cards[1][1]=="Ace"):
            if(self.value>10):
                values["Ace"]=1
            elif(self.value<11):
                values["Ace"]=11

class Chips(Deck,Hand):
    def __init__(self):
        self.total=100
        self.bet=0

    def win_bet(self):
        self.total=self.total+self.bet
    def lose_bet(self):
        self.total=self.total-self.bet

def take_bet(bet,total):
    while(bet>total or bet==0 or bet<0):
        bet = int(input("choose your bet: "))
    return bet
def hit(a, b):
     Card = a.deal()[0][0]
     Card = [Card]
     b.add_cards(Card)

def hit_or_stand(a, b):
        global playing
        answer = input(" Want to hit or stand : ").lower()
        if answer == "hit":
            hit(a, b)
        else:
            playing=False

def show_some(player_cards, dealer_cards):
    print(f" ----->\n PLAYER CARDS : {player_cards}")

    print(f" DEALER CARDS : {[dealer_cards[1]]} \n ----->\n")


def show_all(player_cards, dealer_cards):
    print(f" ------>\n PLAYER_CARDS : {player_cards}")

    print(f" DEALER_CARDS : {dealer_cards} \n ----->\n")

def player_busts(b,c):
    if b.value > 21:
        c.lose_bet()
        return True


def player_wins(b, d, c):
    if (b.value == 21):
        c.win_bet()
        return True

    elif (b.value > d.value and b.value < 21):
        c.win_bet()
        return True


def dealer_busts(d, b,c):
    if (d.value > 21):
        if (b.value < 21):
            c.win_bet()
        return True


def dealer_wins(b, d, c):
    if (d.value == 21):
         c.lose_bet()
         return True

    elif (d.value > b.value and d.value < 21):
        c.lose_bet()
        return True

def push(b,d):
    if(b.value==d.value):
        print("Push")


def play_again():
    return input("do you want to play another hand ? ").lower().startswith("y")

def main():
    a=Deck()
    c=Chips()
    while True:
        print("Welcome to BlackJack game.")
        a.shuffle()
        player, dealer = a.deal()
        b = Hand() #player hand
        b.add_cards(player)
        print("\n Total money -> ", c.total)

        bet = int(input(" Enter bet amount : "))  # Prompt for bet amount

        c.bet = take_bet(bet, c.total)  # New bet amount

        print(c.total)
        show_some(player, dealer)
        global playing
        while playing:
            hit_or_stand(a, b)
            show_some(b.cards, dealer)
            if(player_busts(b,c)==True):
                print(" player bust ")
                break
        playing=True
        d=Hand() #dealer hand
        d.add_cards(dealer)
        while d.value<17:
             hit(a, d)
             if(dealer_busts(d,b,c)==True):
                print("dealer bust")
                break

        show_all(b.cards,d.cards)
        push(b,d) #when equals
        if(player_wins(b,d,c)==True):
            print("player win")
        elif (dealer_wins(b, d, c) == True):
            print("dealer win")
        print('\n -- Remaining : ', c.total)
        if(not(play_again())):
           break
        if(c.total==0):
            print("you lost all money...the end!")
            break

main()



