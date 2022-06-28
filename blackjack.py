import random
import time

#make the card deck
card_deck = []
suits = "of hearts", "of spades", "of diamonds", "of clubs"
card_ranks = "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"
for i in suits:
    for x in card_ranks:
        card_deck.append(f"{x} {i}")

def make_shoe():
    #make the card shoe (=several card decks together)
    amount_of_decks = 4
    new_card_shoe = []
    for y in range(0, amount_of_decks):
        new_card_shoe += card_deck
    return new_card_shoe

card_shoe = make_shoe()
#########################
# functions
########################

def suffle_the_cards(shoe):
    #suffles the cards
    return random.shuffle(shoe)

def ask_money_to_account():
    #adds money to account
    ok = False
    while ok == False:
        try:
            money = int(input("how many euros do you want to add to your game account? "))
            if money > 0:
                ok = True
            else:
                print("please give a positive number")
        except:
            print("please give a positive integer")
    return money

def ask_for_bet(money_in_account):
    ok = False
    while ok == False:
        try:
            bet = int(input("Place your bet. "))
            if bet > 0 and bet <= money_in_account:
                ok = True
            elif bet > 0 and bet > money_in_account:
                print(f"You only have {money_in_account} euros to play.")
            else:
                print("please give a positive number")
        except:
            print("please give a positive integer")
    return bet

def deal_one_more():
    #deal one more card
    try:
        return card_shoe.pop(0)
    except:
        make_shoe()
        return card_shoe.pop(0)

def sum_the_cards(list_of_cards):
    sum = 0
    number_of_aces = 0
    for i in list_of_cards:
        if "Jack" in i or "Queen" in i or "King" in i:
            sum += 10
        elif "Ace" in i:
            number_of_aces += 1
            sum += 11
            #add the logic of ace being either 1 or 11
        else:
            sum += int(i[0])
    return sum

##################################
# the start
##################################

#suffle the card shoe
suffled_cards = suffle_the_cards(card_shoe)

#suffle again when there is no more cards to play in the shoe

#amount_of_players = int(input("How many players? "))
# add this feature later, now only 1 player

###################
# money to playing account
###################
account = 0
account += ask_money_to_account()

print("money in account", account) #test print

##################
# the game
#################

while want_to_continue == True:
    #check if account is empty
    if account == 0:
        print("You don't have any money in your playing account. Let's add some.")
        account += ask_money_to_account()
    #place the bet
    bet = ask_for_bet(account)
    account -= bet

    #deal the first cards
    dealers_cards = []
    players_cards = []

    players_cards.append(deal_one_more())
    players_cards.append(deal_one_more())
    dealers_cards.append(deal_one_more())
    dealers_cards.append(deal_one_more())
    print(f"Players cards {players_cards}")
    print(f"Dealers first card {dealers_cards[0]}")

    #players game:
    while True:
        one_more = input("Do you want another card? y/n ")
        if one_more.lower() == "y":
            players_cards.append(deal_one_more())
            print(f"Players cards {players_cards}")
            players_sum = sum_the_cards(players_cards)
            print(f"the sum of players cards is now {players_sum}")
            if players_sum > 21:
                print("The sum of your cards is over 21. You loose.")
                #add money logic
                break
        elif one_more.lower() == "n":
            break

    print(f"Dealers cards are {dealers_cards[0]}")

    #dealers game:
    if players_sum <= 21:
        dealers_sum = sum_the_cards(dealers_cards)
        while True:
            if dealers_sum > players_sum and dealers_sum >= 17 and dealers_sum <= 21:
                print(f"The dealer won with the sum on {dealers_sum}") 
                #add money logic
                break
            elif dealers_sum < players_sum and dealers_sum >= 17 and dealers_sum <= 21:
                print(f"The dealer looses with the sum on {dealers_sum}") 
                #add money logic
                break
            elif dealers_sum < 17:
                dealers_cards.append(deal_one_more())
                print(f"Dealers cards {dealers_cards}")
                dealers_sum = sum_the_cards(dealers_cards)
                print(f"the sum of dealers cards is now {dealers_sum}")
            elif dealers_sum > 21:
                print("The sum of dealers cards is over 21. You win.")
                #add money logic
                break


    #after the game, ask if you want to play again
    again = input("Do you want to play again? y/n")
    if again.lower() == "y":
        want_to_continue = True
    elif again.lower() == "n":
        want_to_continue = False
        print("Thanks for playing! Bye!")
        time.sleep(5) #sleep for 5 seconds before ending the program
        


#pelin lopuksi kysy pelataanko uudestaan.

# ässä on arvoltaan joko yksi tai yksitoista, 
# kaikki kuvakortit kymmenen ja 
# muut kortit nimellisarvonsa verran.

#jaa kortit:
# vuorotellen jakajalle ja pelaajalle/pelaajille
# pelaajalle yht 2 korttia, kuvapuoli ylöspäin. jakajalle yht 2 korttia, toinen nurinpäin

# pelaajalle kortteja, kunnes ei halua enää lisää
# tai korttien summa on yli kaksikymmentäyksi.

# jakajan toinen kortti oikeinpäin
# Tämän jälkeen jakaja ottaa itselleen kortteja, 
# kunnes hänen kätensä on 17 tai enemmän. 
# Jos käden arvo on seitsemäntoista tai enemmän, jakaja ei saa ottaa enempää kortteja. 

# Pelin voittaa se, jolla korttien yhteislukema on suurempi, mutta max 21
# 
# Kahdella ensimmäisellä kortilla saatu pistemäärä kaksikymmentäyksi on nimeltään blackjack, 
# ja se voittaa useammalla kuin kahdella kortilla saadun 21 pisteen summan. 
# Jos pelaajalla ja jakajalla on yhteislukema sama, pelaaja häviää, 
# paitsi jos kyseessä on tasapeli kahdessakymmenessäyhdessä tai blackjackissä (niin sanottu stand off). 
# Jos yhteislukema on suurempi kuin kaksikymmentäyksi, sen summan saanut häviää.
# 
# Paremmille käsille maksetaan alkuperäisen panoksen suuruinen voitto, 
# huonommat kädet menettävät panoksensa. 
# Tasapelitilanteessa pelaaja saa pitää panoksensa. 
# Blackjackin saaneelle pelaajalle maksetaan panos puolitoistakertaisena 
# ellei myös jakajalla ole blackjackia.

# Pistevoitolla pelaajan pelipanos voittaa 1:1. Blackjack voittaa 3:2.
