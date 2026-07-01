import random
from itertools import islice
from engine import build_deck, get_score, is_blackjack, Dealer_AI,visible_card_score


def create_dna() -> dict:
    action = ["H","S"] #right now the dna can only include isntructions to either hit stand, no double or split
    dna = {}
    for player_score in range(4,21):
        for dealer_cards in range(2,12): #only visible cards can be 2 to ace(11)
            dna[(player_score,dealer_cards)] = random.choice(action)
    return dna #creates random genetics, the dna is basically a big 170 large table of choices hit or stand depending on the players card and dealers card, good genetics are promoted in natural selection through the 'breeding' of winning strategies, and mutations to introduce new genetic codde

def dna_win_rate(dna: dict ,trials: int) -> int:
    total_player_wins = 0
    for i in range(trials):
        player_bust = False
        deck = build_deck() #new deck each round so no card counting
        player_cards = [deck.pop(),deck.pop()]
        dealer_cards = [deck.pop(),deck.pop()]  
        if is_blackjack(player_cards) and not is_blackjack(dealer_cards): #check for 'natural' black Jack
            total_player_wins += 1
            continue
        elif is_blackjack(dealer_cards):
            continue
        player_score = get_score(player_cards)
        dealer_score = visible_card_score(dealer_cards[0][0]) #special card score as get score returns score for both cards while in real life the player can only see the first card
        result = dna[(player_score,dealer_score)] #the actual decision given by the dna for the player
        while (player_score < 21 and result == "H"): #loop uuntil stand or busted
            player_cards.append(deck.pop()) #simulate a hit
            player_score = get_score(player_cards)
            if player_score == 21:
                break #exit when won
            elif player_score > 21:
                player_bust = True
                break #exit when busted
            result = dna[(player_score,dealer_score)] #record the new action given by the dna
        if player_bust:
            continue #next round player has bust
        #When player decides to stand it is now dealers turn
        dealer_score = get_score(dealer_cards)
        while dealer_score < 17:
            dealer_cards.append(deck.pop())
            dealer_score = get_score(dealer_cards)
        if dealer_score > 21:
            total_player_wins += 1
            continue
        elif dealer_score == 21:
            continue
        elif dealer_score < player_score:
            total_player_wins += 1
    return total_player_wins

def main():
    population = 100
    trials = 1000
    generation = 10
    cutoff = 20 #the cut off is 20% only the top 20% are able to bread
    win_rates = []
    new_dna = []
    selection = []
    dna = [create_dna() for i in range(population)] #create a list of the DNA, the amount is given by the population
    win_rates = []
    best_win_rate = 0.00
    best_dna = {}
    while generation != 0:
        win_rates.clear()
        for i in range(population):
            win_rates.append((dna_win_rate(dna[i],trials),i))
        win_rates.sort()
        win_rates.reverse()
        print(f"Best win_rate of {abs(generation-10)}: {win_rates[0][0]/trials:.2f}")
        if (win_rates[0][0] / trials) * 100 > best_win_rate: #record the best win rate so far and the coressponding strategy
            best_win_rate = (win_rates[0][0] / trials) * 100
            best_dna = dict(dna[win_rates[0][1]]) #stores the best dna so far making sure it is a copy by using dict() win_rates also stores the index that is how the best dna is picked
        selection.clear()
        selection = win_rates[:cutoff] #first top 20 are chosen
        new_dna.clear()
        for i in range(cutoff):
            new_dna.append(dna[selection[i][1]]) #new dna now conains the new top 20
        pop_need = population - cutoff #the population needed to replace the perctanage that was not chosen
        while pop_need != 0:
            parent1_index = random.randint(0,cutoff-1) #picks random 2 parents
            parent2_index = random.randint(0,cutoff-1)
            child = crossover(new_dna[parent1_index], new_dna[parent2_index])
            mutation(child, mutation_rate=1) #mutation rate is 1%
            new_dna.append(child) #child is a now a new gene
            pop_need -= 1
        dna.clear()
        dna = list(new_dna) #repeat the cycle 
        print(f"Current generation is {abs(generation-10)}")
        generation -= 1
    print(f"The best win rate is {best_win_rate:.2f}")
    print(f"The winning dna was {best_dna}")

def crossover(parent1: dict, parent2: dict)  -> dict:
    crossover_point = random.randint(1,169) #dna has 170 genes, 169 beccause inclusive and list is 0 index based, randomly select the point to swap parents dna
    first_half_dna = dict(islice(parent1.items(),0,crossover_point)) #create a dictionary dna from 0 to crossover_point
    second_half_dna = dict(islice(parent2.items(),crossover_point,None)) #start at crossover_point to end which is None to make second half od the dna
    dna_child = first_half_dna | second_half_dna #union that megers to the 'half' dictionaries to form complete new dna that iis a mesh of the parents
    return dna_child

def mutation(dna: dict,mutation_rate: int):
    for cards,action in dna.items():
        if random.randint(1,100) <= mutation_rate:
            if dna[cards] == "H":
                dna[cards] = "S"
            else:
                dna[cards] = "H"

if __name__ == "__main__":
    main()



