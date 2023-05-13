def exchange_money(budget, exchange_rate):
    exchanged_value = budget / exchange_rate
    return exchanged_value

def get_change(budget, exchanging_value):
    remaining_budget = budget - exchanging_value
    return remaining_budget

def get_value_of_bills(denomination, number_of_bills):
    total_value_of_bills = denomination * number_of_bills
    return total_value_of_bills

def get_number_of_bills(budget, denomination):
    number_of_bills = budget // denomination
    return number_of_bills

def get_leftover_of_bills(budget, denomination):
    leftover_amount = budget % denomination
    return leftover_amount

def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_exchange_rate = exchange_rate + (spread / 100) * exchange_rate
    max_exchanged_value = budget / actual_exchange_rate
    max_exchanged_value = int(max_exchanged_value / denomination) * denomination
    return max_exchanged_value
