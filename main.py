from engine import build_deck, get_score, is_blackjack
from strategies.copycat import copycat_AI

def main():
    trial_count = int(input("Please enter the number of trials that you wish to have: "))
    total_player_wins = 0
    total_dealer_wins = 0
    total_ties = 0

    for i in range(trial_count):
        deck = build_deck()
        player_cards = [deck.pop(), deck.pop()]
        dealer_cards  = [deck.pop(), deck.pop()]

        player_bj = is_blackjack(player_cards)
        dealer_bj  = is_blackjack(dealer_cards)
        if player_bj and dealer_bj:
            total_ties += 1
            continue
        elif player_bj:
            total_player_wins += 1
            continue
        elif dealer_bj:
            total_dealer_wins += 1
            continue

        player_score = get_score(player_cards)
        while player_score < 21:
            if copycat_AI(player_score) == "H":
                player_cards.append(deck.pop())
                player_score = get_score(player_cards)
            else:
                break
        if player_score > 21:
            total_dealer_wins += 1
            continue

        dealer_score = get_score(dealer_cards)
        while dealer_score < 21:
            if copycat_AI(dealer_score) == "H":
                dealer_cards.append(deck.pop())
                dealer_score = get_score(dealer_cards)
            else:
                break
        if dealer_score > 21:
            total_player_wins += 1
            continue

        if player_score > dealer_score:
            total_player_wins += 1
        elif dealer_score > player_score:
            total_dealer_wins += 1
        else:
            total_ties += 1

    print(f"Trials:       {trial_count:,}")
    print(f"Player wins:  {total_player_wins:,} ({(total_player_wins/trial_count) * 100:.2f}%)")
    print(f"Dealer wins:  {total_dealer_wins:,} ({(total_dealer_wins/trial_count) * 100:.2f}%)")
    print(f"Ties:         {total_ties:,} ({(total_ties/trial_count) * 100:.2f}%)")

if __name__ == "__main__":
    main()
