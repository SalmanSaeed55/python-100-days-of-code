import random


def deal(deck, player, dealer, player_choice=None):
    """Deals cards based on user choices. If player wants to `hit`, it adds cards to their hand. If they want to
    `stand`, it skips their turn.
    Dealer only has cards added to their hand if their total is less than 17

    :param deck: The deck of cards to draw from
    :param player: The players hand
    :param dealer: The dealer's hand
    :param player_choice: The player choice if they want to `hit` or `stand`
    :return: the player and dealer hands, and a boolean indicating if the game has ended
    """
    end = False
    if player and dealer:
        if sum(dealer) < 17:
            dealer.append(random.choice(deck))

        if player_choice == "h":
            picked_card = random.choice(deck)
            if picked_card + sum(player) > 21 and picked_card == 11:
                player.append(1)
            else:
                player.append(picked_card)
        elif player_choice == "s":
            if sum(dealer) >= 17:
                end = True
            else:
                end = False
    else:
        for i in range(2):
            player.append(random.choice(deck))
            dealer.append(random.choice(deck))

    return player, dealer, end


def show_dealer_hand(dealer_cards):
    """Displays the dealer hand, hiding the most recent card dealt to them

    :param dealer_cards: The dealer's hand
    :return: The cards that can be displayed to the player
    """
    cards_to_show = []
    for i in range(0, len(dealer_cards) - 1):
        cards_to_show.append(dealer_cards[i])
    return cards_to_show


def check_hands(player_deck, dealer_deck):
    """Checks teh sums of both player and dealer hands

    :param player_deck: the player hand
    :param dealer_deck: the dealer hand
    :return: the total sums of each hand
    """
    player_sum = sum(player_deck)
    dealer_sum = sum(dealer_deck)

    return player_sum, dealer_sum


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_continue = None
game_end = False

print("Welcome to Blackjack!")
input("Press enter to continue...")

while True:
    deal_cards = deal(CARDS, player_hand, dealer_hand, player_continue)
    player_hand = deal_cards[0]
    dealer_hand = deal_cards[1]

    print(f"\nYour hand: {player_hand} \t Current Score: {sum(player_hand)} \t Number of Cards: {len(player_hand)}")
    print(f"Dealer's hand: {show_dealer_hand(dealer_hand)} \t Number of Cards: {len(dealer_hand)}")

    hands_total = check_hands(player_hand, dealer_hand)

    if not deal_cards[2]:
        if hands_total[0] > 21:
            print("You are Bust! Dealer Wins")
            game_end = True
        elif hands_total[1] > 21:
            print("Dealer is Bust! You Win")
            game_end = True
        else:
            player_continue = input("Do you want to hit or stand? (h/s): ").lower()
    elif deal_cards[2]:
        player_sum = hands_total[0]
        dealer_sum = hands_total[1]

        if dealer_sum > 21 >= player_sum:
            print("You Win")
            game_end = True
        elif player_sum > 21 >= dealer_sum:
            print("Dealer Wins")
            game_end = True
        elif player_sum > 21 and dealer_sum > 21:
            print("Dealer Wins")
            game_end = True
        elif 17 <= dealer_sum <= 21 and player_sum <= 21:
            player_diff = 21 - player_sum
            dealer_diff = 21 - dealer_sum
            if player_diff < dealer_diff:
                print("You Win")
                game_end = True
            elif player_diff == dealer_diff:
                print("Draw")
                game_end = True
            else:
                print("Dealer Wins")
                game_end = True
        else:
            if player_sum > dealer_sum:
                print("You Win")
            elif player_sum == dealer_sum:
                print("Draw")
            else:
                print("Dealer Wins")
            game_end = True

    if game_end:
        print(f"\nYour final hand: {player_hand} \t Final Score: {sum(player_hand)}")
        print(f"Dealer's final hand: {dealer_hand} \t Final Score: {sum(dealer_hand)}")
        restart = input("Do you want to play again? (y/n): ").lower()

        if restart != "y":
            print("Thank you for playing!")
            break
        else:
            player_hand = []
            dealer_hand = []
            player_continue = None
            game_end = False
