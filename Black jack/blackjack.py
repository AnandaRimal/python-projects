import random

print("Welcome to the Blackjack Project!")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_card = {"card1": random.choice(cards), "card2": random.choice(cards)}
computer_card = {"card1": random.choice(cards), "card2": random.choice(cards)}

print(f"User's cards: {user_card}")
print(f"Computer's cards: {computer_card}")


def calculate_score(cards):
    return sum(cards.values())


user2c = calculate_score(user_card)
computer2c = calculate_score(computer_card)

print(f"User's initial score: {user2c}")
print(f"Computer's initial score: {computer2c}")


def rules():
    global user2c, computer2c

    if user2c == 21 and computer2c == 21:
        print("It's a tie! Both have Blackjack!")
        return
    elif user2c == 21:
        print("User wins with Blackjack!")
        return
    elif computer2c == 21:
        print("Computer wins with Blackjack!")
        return

    add_card = input("Do you want to add a card? (yes/no): ").lower()
    if add_card == "yes":
        user_card["card3"] = random.choice(cards)
        user2c = calculate_score(user_card)
        print(f"User's new cards: {user_card}, total: {user2c}")

    if computer2c < 17:
        computer_card["card3"] = random.choice(cards)
        computer2c = calculate_score(computer_card)
        print(f"Computer's new cards: {computer_card}, total: {computer2c}")

    if user2c > 21 and computer2c > 21:
        print("Both busted! No winner.")
    elif user2c > 21:
        print("User busted! Computer wins.")
    elif computer2c > 21:
        print("Computer busted! User wins.")
    elif user2c > computer2c:
        print("User wins!")
    elif user2c < computer2c:
        print("Computer wins!")
    else:
        print("It's a tie!")


rules()
