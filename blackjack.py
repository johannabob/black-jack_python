import random

#make the card deck and the card box of several card decks
card_deck = []
suits = "of hearts", "of spades", "of diamonds", "of clubs"
card_ranks = "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"
for i in suits:
    for x in card_ranks:
        card_deck.append(f"{x} {i}")
#print("card deck:", card_deck) #test print

#make the card shoe (=several card decks together)
amount_of_decks = 4
card_shoe = []
for y in range(0, amount_of_decks):
    card_shoe += card_deck
print("card_shoe:", card_shoe) #test print

#########################
# functions
########################

def suffle_the_cards(shoe):
    #suffles the cards
    return random.shuffle(shoe)

def money_to_account():
    #add money to account
    return int(input("how much money do you want to load to your game account? "))

##################################
# the game
##################################

#suffle the card shoe
suffled_cards = suffle_the_cards(card_shoe)

#suffle again when there is no more cards to play in the shoe

#amount_of_players = int(input("How many players? "))
# add this feature later, now only 1 player

###################
# money
###################
account = 0
account += money_to_account()

#luo pelitili
#lataa pelitilille rahaa

#aseta pelin panos
#pelaa
#päivitä pelitilin saldo
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
