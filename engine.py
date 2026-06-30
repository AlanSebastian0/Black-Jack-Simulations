import random

shoe_count = 6
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['Hearts','Diamonds','Clubs','Spades']

def build_deck(): #builds a deck of list
    deck = [(v,s) for v in values for s in suits] * shoe_count
    random.shuffle(deck)
    return deck #return list of tuples

def is_blackjack(cards: list):
    return len(cards) == 2 and get_score(cards) == 21 #checks if its black jack for the beginning


def Dealer_AI(score: int) -> str: #the constant Dealer AI common amongst most casinos
    return "S" if score >= 17 else "H"

def get_score(cards: list):
    score = 0
    ace_count = 0
    for value, _ in cards:
        if value in ("K","Q","J","10"):
            score += 10
        elif value == "A":
            ace_count += 1
            score += 11
        else:
            score += int(value)
    while score > 21 and ace_count >= 1:
        score -= 10
        ace_count -= 1
    return score
def visible_card_score(card: str) -> int:
    if card == "A":
        return 11
    elif card in ["J","Q","K"]:
        return 10
    else:
        return int(card)
