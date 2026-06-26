from engine import build_deck, get_score, is_blackjack #basics game mehanics needed 
#Total stratgies below
from strategies.copycat import copycat_AI
from strategies.stand_15 import stand_15
from strategies.stand_16 import stand_16
from strategies.stand_18 import stand_18
from strategies.stand_19 import stand_19

def run_simulation(strategy, trial_count):
    #win,los, tie counts
    total_player_wins = 0
    total_dealer_wins = 0
    total_ties = 0
    for i in range(trial_count):
        deck = build_deck() #builds the deck each 'round' fro 0 main compute
        #player and dealer cards dealt at start
        player_cards = [deck.pop(), deck.pop()]
        dealer_cards  = [deck.pop(), deck.pop()]
        player_bj = is_blackjack(player_cards) #check if natural black jack was formed
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
        player_score = get_score(player_cards) #returns the hand score
        while player_score < 21:
            if strategy(player_score) == "H": #wheter hit or stand is dependant on stratgey
                player_cards.append(deck.pop()) #card is added to the 'hand'
                player_score = get_score(player_cards) #new score calculated from scracth to catch 'soft' hands, eg Ace + 3 + Queen
            else:
                break
        if player_score > 21: #player busts
            total_dealer_wins += 1
            continue
        dealer_score = get_score(dealer_cards) #same logic for dealer
        while dealer_score < 21:
            if Dealer_AI(dealer_score) == "H": #dealer strategy is fixed as most casinos are
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
    return total_player_wins, total_dealer_wins, total_ties #return the wins,losses and ties for anaylsyes

def Dealer_AI(score: int) -> str: #the constant Dealer AI common amongst most casinos
    return "S" if score >= 17 else "H"

def main(): #main anyalysyes is here
    trial_count = int(input("Please enter the number of trials that you wish to have: "))
    strategies = [stand_15, stand_16, copycat_AI, stand_18, stand_19] #list of the current strategies available where the functions are objects
    #Print formatting to complete a table rathern than an excel table
    names      = ["Stand 15+", "Stand 16+", "Copycat (Stand 17+)", "Stand 18+", "Stand 19+"]
    print(f"\n{'Strategy':<22} {'Wins':>8} {'Losses':>8} {'Ties':>8} {'Win %':>8} {'Loss %':>8}")
    print("-" * 66) #line to seperate
    for strategy, name in zip(strategies, names): #tuple unpacing in zip
        w, l, t = run_simulation(strategy, trial_count)
        print(f"{name:<22} {w:>8,} {l:>8,} {t:>8,} {(w/trial_count)*100:>7.2f}% {(l/trial_count)*100:>7.2f}%")

if __name__ == "__main__":
    main()
