def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    if (card_one == 'A' or card_two == 'A'): 
        return 1
    elif (value_of_card(card_one) + value_of_card(card_two) <= 10):
        return 11 
    else :
        return 1
        



def is_blackjack(card_one, card_two):
    if card_one == 'A' and card_two in ['10', 'J', 'Q', 'K']:
        return True
    elif card_two == 'A' and card_one in ['10', 'J', 'Q', 'K']:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    if card_one =='Q' and card_two =='K':
        return True 
    elif card_one =='K' and card_two =='Q':
        return True 
    elif card_one == card_two:
        return True 
    else :
        return False 
    
    


def can_double_down(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)
    return total_value in [9, 10, 11]
