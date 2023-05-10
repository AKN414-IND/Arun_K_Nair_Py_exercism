EXPECTED_BAKE_TIME = 40
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2
def preparation_time_in_minutes(number_of_layers):
    """return preparation time in minutes """
    return number_of_layers * PREPARATION_TIME_PER_LAYER
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """return elapsed time in minutes"""
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time
def bake_time_remaining(actual_minutes):
    """baking time in minutes """
    if actual_minutes < EXPECTED_BAKE_TIME:
        return EXPECTED_BAKE_TIME - actual_minutes
    else:
        return 0
