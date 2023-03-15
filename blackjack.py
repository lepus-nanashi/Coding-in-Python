import random
import blackjack_art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_card(who_cards, times):
    if times > 0:
        new_card = random.choice(cards)
        who_cards.append(new_card)
    if times > 1:
        new_card = random.choice(cards)
        who_cards.append(new_card)

def sum_score(who_cards):
    final_sum = sum(who_cards)
    if final_sum == 21 and len(who_cards) == 2:
        final_sum = 0
    if 11 in who_cards and sum(who_cards) > 21:
        who_cards.remove(11)
        who_cards.append(1)
        final_sum = sum(who_cards)
    return final_sum

def compare_scores(user_score, comp_score):
    if user_score == 0 and comp_score != 0:
        return "You got a blackjack. You win!"
    if comp_score == 0 and user_score != 0:
        return "Computer has a blackjack. You lose..."
    if user_score == comp_score:
        return "It's a draw . . ."
    if user_score > 21:
        return "You went over. You lose..."
    if comp_score > 21:
        return "Computer went over. You win!"
    if user_score > comp_score:
        return "You win!"
    else:
        return "You lose..."
    
def start_round():
    if input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
        play_blackjack()
    else:
        import os
        from time import sleep
        print ("Very well, see you soon!")
        sleep(2)
        os.system("cls")
        

def play_blackjack():
        print (blackjack_art.logo)

        user_cards = []
        comp_cards = []

        add_card(user_cards, 2)
        user_score = sum_score(user_cards)
        print (f"Your cards: {user_cards}, current score: {user_score}.")

        add_card(comp_cards, 2)
        comp_score = sum_score(comp_cards)
        print (f"Computer's first card: {comp_cards[0]}")

        game_over = False       
        while not game_over:
            user_choice = input("Type 'y' to get another card, type 'n' to pass:  ")
            if user_choice == "y":
                add_card(user_cards, 1)
                user_score = sum(user_cards)
                print(f"Your hand: {user_cards}, current score: {user_score}")
            if comp_score < 21:
                add_card(comp_cards, 1)
                comp_score = sum(comp_cards)
            if user_choice == "n":
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
                results = compare_scores(user_score, comp_score)
                print(results)
                start_round()
                game_over = True


start_round()

    
