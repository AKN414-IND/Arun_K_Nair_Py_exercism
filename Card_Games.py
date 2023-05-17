def get_rounds(number):
    return [number,number+1,number+2];


def concatenate_rounds(rounds_1, rounds_2):

    return rounds_1+rounds_2;



def list_contains_round(rounds, number):
    if number in rounds:
        return True;
    else :
        return False;


def card_average(hand):
    return sum(hand)/len(hand);
    


def approx_average_is_average(hand):
    actual_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]

    return actual_average == first_last_average or actual_average == median;

def average_even_is_average_odd(hand):
    even_average = sum(hand[::2])/ len(hand[::2])
    odd_average = sum(hand[1::2])/ len(hand[1::2])

    return even_average == odd_average;


def maybe_double_last(hand):
    a=len(hand)
    if hand[a-1]==11:
        hand[a-1]*=2
    return hand;
