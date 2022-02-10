# HTE BLACKJACK CAPSTONE PROJECT
# IMPLEMENNTTING ALL CONCEPTS FROM THE 1ST 10 DAYS
import random


def deal_card():
    """"Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win, You have Blackjack"
    elif user_score > 21:
        return "You went over 21 , You lose"
    elif computer_score > 21:
        return "Opponent went over 21, You Win" 
    elif user_score > computer_score:
        return "You Win"
    else: 
        return "You lose"       
    
    
def play_game():
    user_card = []
    computer_card = []
    is_game_over = False


    for nums in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        

    def calculate_score(cards):
            """Returns the sum of the card in hand and changes the Ace to "1" after exceeding 21."""
            if sum(cards) == 21 and len(cards) == 2:
                return 0
            return sum(cards)
            if 11 in cards and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)        
            
    while not is_game_over:

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card} current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]} ")
                
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
            
            
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card) 
        


    print(f"Your final hand {user_card}, final score: {user_score}")
    print(f"Computer's final hand {computer_card}, final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    play_game()
    
        
        
        
# FINIRE