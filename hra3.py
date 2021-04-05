from random import randrange

dealer_cards = []
player_cards = []
print("Lukáš Lechovič BLACKJACK V2")
vek = int(input('Kolko máte rokov? '))
while True:
    if vek >= 18:
        print("Vitajte")
        break   
    print("Prepáčte hazardné hry sú od 18 rokov")

meno = input("Zadajte použivatelské meno: ")
while len(dealer_cards) !=2:
    dealer_cards.append(randrange(1,11))
    if len(dealer_cards) == 2:
        print("Dealer má X a", dealer_cards[1])

while len(player_cards) !=2:
    player_cards.append(randrange(1,11))
    if len(player_cards) == 2:
        print(meno, "má", player_cards, "=", sum(player_cards))

if sum(dealer_cards) == 21:
    print("Dealer má 21 a vyhráva!")
elif sum(dealer_cards) > 21:
    print("Dealer prehral", sum(dealer_cards))

while sum(player_cards) < 21:
    odpoved = str(input("Chceš hitnut alebo stat? "))
    if odpoved == "hit" or odpoved == "hitnut":
        player_cards.append(randrange(1,11))
        print("Teraz máš", str(sum(player_cards)), "z týchto kariet", player_cards)
    else:
        if sum(dealer_cards) < sum(player_cards):
            dealer_cards.append(randrange(1,11))
            print("Dealer si tahá ...")
        if sum(dealer_cards) < sum(player_cards):
            dealer_cards.append(randrange(1,11))
        if sum(dealer_cards) < sum(player_cards):
            dealer_cards.append(randrange(1,11))
            print("Dealer si tahá ...")
        print("Dealer má", str(sum(dealer_cards)), "z týchto kariet", dealer_cards)
        print("Máš", str(sum(player_cards)), "z týchto kariet", player_cards)
        if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) <= 21:
            print("Dealer vyhral!", dealer_cards, sum(dealer_cards))
        elif sum(player_cards) == sum(dealer_cards):
            print("Remíza tak to je extrem", sum(player_cards), "a", sum(dealer_cards))
        else:
            print(meno, "vyhral !", player_cards, sum(player_cards))
            
        break

if sum(player_cards) > 21:
    print("Prehral si! Dealer vyhral.")

elif sum(player_cards) == 21:
    print("Máš BLACKJACK!")