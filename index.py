import random
from art import logo

print(logo)

# Create a deal_card() function that uses the List below to return a random card.
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Create a function called calculate_score() that takes a List of cards as input and returns the sum of all the cards in the List as the score.
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function called compare() and pass in the user_score and computer_score:





# If none of the above, then the player with the highest score wins
def compare(usuario_score, computadora_score):
    # If the computer and user both have the same score, then it's a draw.
    if usuario_score == computadora_score:
        return "It's a Draw 🙃."
    # If the computer has a blackjack (0), then the user loses.
    elif computadora_score == 0:
        return "Lose... Computer has Blackjack 😭"
    # If the user has a blackjack (0), then the user wins.
    elif usuario_score == 0:
        return "Win with a BLACKJACK 😎!!!"
    # If the user_score is over 21, then the user loses.
    elif usuario_score > 21:
        return "You went over. You lose... 😭"
    # If the computer_score is over 21, then the computer loses.
    elif computadora_score > 21:
        return "Computer went over. You win 😁!"
    # If the user score is higher than the computer, user wins.
    elif usuario_score > computadora_score:
        return "You win 😁!"
    # Last case, if the computer score is higher than the users, user lose.
    else:
        return "You lose... 😭"
    
# This function is made for the player typing 'yes' on the question about playing another round
def play_game():
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    # This is for having any value in the computer_score variable so we don't have an error when we arrive to the while loop were is allocated.
    computer_score = -1
    # The same for the users variable.
    user_score = -1
    # If the user_score is equal to 0, or the computer_score is equal to 0, or the user_score is greater than 21, then in this case we're going to tell the game to end.
    is_game_over = False

    # This is for running the loop twice
    #Every single time this loop runs, we're going to get a new card by calling deal_card().
    for _ in range(2):
        # Now the next thing we're going to do is we're going to add this new_card to the user_cards.
        user_cards.append(deal_card())
        # Now want to do the same thing for the computer_cards.
        computer_cards.append(deal_card())

    # The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    # This will while loop will give us a card until we type "no"
    # The while loop is responsible for dealing with when the user wants to keep drawing cards,
    while not is_game_over:
        # Call the function calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        # And this is the place where I want to call it, because it's only after I've dealt the user and the computer some cards can I actually calculate their scores.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # print statements here so that I can see what the user's cards are, and what the user's score is.
        print(f"Your cards: {user_cards}, current score → {user_score}")
        # So in here, we're going to insert the computer's cards, and we're only going to pick out the first item. So the one at index 0.
        print(f"Computer's first card: [{computer_cards[0]}]. current computer's score → {computer_score}")


        # Now that we've called calculate_score(), we also want to make sure that if the computer, or the user has a blackjack, or if the user scores over 21, then we have to end the game.
        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        # Over here in the if statement, we can add an else, because if the game hasn't ended, as in they haven't gone over 21 or nobody's got a blackjack, then we're going to ask the user if they want to get another card.
        else:
            user_should_deal = input("Type 'yes' to get another card, type 'no' to pass: \n").lower()
            if user_should_deal == "yes":
                user_cards.append(deal_card())
            # If they didn't type 'y', then that means they don't want another card. Well then in this case, the game has again ended.
            else:
                is_game_over = True
    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    # We can represent this logic using a while loop, while the computer_score is not equal to 0, and the computer_score is less than 17, then in this case we want to keep drawing cards.
    while computer_score != 0 and computer_score < 17:
        # We're going to take the computer's cards, and we're going to use the append to add a card by dealing
        computer_cards.append(deal_card())
        # And then we're going to recalculate the computer_score so that it updates,  and this while loop is evaluated on the latest score.
        computer_score = calculate_score(computer_cards)

    # Give the user a little bit more information, like revealing the final deck
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    # And now we can call that compare() function and pass in the user_score and also the computer_score.
    print(compare(user_score, computer_score))

# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play another round? Type 'yes or 'no': \n") == "yes":
    # we don't want to clutter up our screen with all the previous games, so before we call play_game() we also want to clear the console.
    # print("\n" * 50)
    play_game()