import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

start_balance = 100


def game_start(bl_1):
    print(f"Welcome to the game, you are given ${bl_1}")

    def continue_game(bl_c):
        if bl_c > 0:
            print(f"Your current balance is ${bl_c}")
            bet_amount = int(input("How much would you like to bet?\n$"))
            if bet_amount > bl_c:
                print("Bet amount is bigger than account balance")
                continue_game(bl_c)
                return
            bl_c -= bet_amount
            dealer_card = []
            player_card = []
            for i in range(0, 2):
                dealer_card.append(cards[random.randint(0, 11)])
                player_card.append(cards[random.randint(0, 11)])
            print(f"Dealer card is ({dealer_card[0]}, *) and your cards are {player_card[0], player_card[1]}\nYour card sum = {sum(player_card)}")
            if 10 in player_card and 11 in player_card:
                print("You win")
                bl_c += bet_amount*2
                continue_game(bl_c)
                return

            def add_player_card(card_adder):
                new_card = input("Do you want another card")
                if new_card == "n":
                    return
                elif new_card == "y":
                    card_adder.append(cards[random.randint(0, 11)])
                    print(player_card)
                    if sum(card_adder) > 21:
                        print("Busted!")
                        print(f"Your card {sum(player_card)} is over 21")
                        if bl_c < 1:
                            print("You are out of money!")
                        else:
                            continue_game(bl_c)
                    elif sum(card_adder) == 21:
                        return
                    elif sum(card_adder) < 21:
                        add_player_card(card_adder)
            add_player_card(card_adder=player_card)
            if bl_c < 1:
                return
            if 10 in dealer_card and 11 in dealer_card:
                print(dealer_card)
                print("Jackpot, dealer wins")

            def add_dealer(dealer_added, bal_update):
                if sum(dealer_added) < 17:
                    dealer_added.append(cards[random.randint(0, 11)])
                    if sum(dealer_added) > 21:
                        print(f"Dealer cards: {dealer_added} Sum: {sum(dealer_added)}")
                        print(f"Your cards{player_card} sum:{sum(player_card)}")
                        print("Bust, You win")
                        bal_update = bl_c
                        bal_update += bet_amount*2
                        continue_game(bal_update)

                    elif sum(dealer_added) > 18:
                        return
                    else:
                        add_dealer(dealer_added, bal_update)
            add_dealer(dealer_added=dealer_card, bal_update=bl_c)

            if sum(dealer_card) > sum(player_card):
                print(f"Dealer card is {dealer_card}, sum ={sum(dealer_card)}")
                print("You lose, better luck next time!")
                continue_game(bl_c)

            elif sum(player_card) > sum(dealer_card):
                print(f"Your card is {player_card} '{sum(player_card)}'")
                print(f"Dealer card is {dealer_card} '{sum(dealer_card)}'")
                print("You win")
                bl_c += bet_amount * 2
                continue_game(bl_c)

            elif sum(player_card) == sum(dealer_card):
                print(f"Dealer cards are {dealer_card} and your cards are {player_card}")
                print("Its a draw")
                bl_c += bet_amount
                continue_game(bl_c)
            else:
                print("There is an error in the code")
        else:
            print("You are out of money100")

    continue_game(bl_c=bl_1)


game_start(bl_1=start_balance)
# @saint_mathew1