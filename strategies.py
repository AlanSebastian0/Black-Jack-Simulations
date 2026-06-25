import random
#test edit
def main():
    shoe_count = 6 #standard Casions have 6 shoes
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] #values
    suits = ['Hearts','Diamonds','Clubs','Spades'] #suits
    trial_count = int(input("Please enter the number of trials that you wish to have: "))
    total_player_wins = 0
    total_dealer_wins = 0
    total_ties = 0
    for i in range(trial_count):
        deck = [(v,s) for v in values for s in suits] * shoe_count
        random.shuffle(deck) #generate a new deck each round

        player_cards = [deck.pop(), deck.pop()]
        dealer_cards = [deck.pop(), deck.pop()]

        #Black Jack test to see if anyone won in the first 'deal'
        player_bj = is_blackjack(player_cards)
        dealer_bj = is_blackjack(dealer_cards)
        if player_bj and dealer_bj:
            total_ties += 1
            continue
        elif player_bj:
            total_player_wins += 1
            continue
        elif dealer_bj:
            total_dealer_wins += 1
            continue

        #this is the players turn
        player_score = get_score(player_cards)
        while player_score < 21:
            if copycat_AI(player_score) == "H":
                player_cards.append(deck.pop())
                player_score = get_score(player_cards)
            else:
                break

        if player_score > 21:  #check if player bust
            total_dealer_wins += 1
            continue #new round player lost

        #dealer's turn
        dealer_score = get_score(dealer_cards)
        while dealer_score < 21:
            if copycat_AI(dealer_score) == "H":
                dealer_cards.append(deck.pop())
                dealer_score = get_score(dealer_cards)
            else:
                break

        if dealer_score > 21:  #dealer bust
            total_player_wins += 1
            continue #new round player win

        #when both stood, compare scores
        if player_score > dealer_score:
            total_player_wins += 1
        elif dealer_score > player_score:
            total_dealer_wins += 1
        else:
            total_ties += 1

    print(f"Trials:       {trial_count:,}") #outputs to observe win rate
    print(f"Player wins:  {total_player_wins:,} ({(total_player_wins/trial_count) * 100:.2f}%)")
    print(f"Dealer wins:  {total_dealer_wins:,} ({(total_dealer_wins/trial_count) * 100:.2f}%)")
    print(f"Ties:         {total_ties:,} ({(total_ties/trial_count) * 100:.2f}%)")

def is_blackjack(cards: list) -> bool:
    return len(cards) == 2 and get_score(cards) == 21 #check to see if there was a 'natural' black jack

def get_score(cards: list) -> int:
    score = 0
    ace_count = 0 #number of aces in the deck to determine any 'soft' numbers
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

def copycat_AI(score: int) -> str:
    if score >= 17:
        return "S"
    else:
        return "H"

if __name__ == "__main__":
    main()
