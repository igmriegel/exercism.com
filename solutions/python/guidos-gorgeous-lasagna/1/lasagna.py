EXPECTED_BAKE_TIME = 40

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(minutes_in_oven):
    """Returns the remaining bake time"""
    return EXPECTED_BAKE_TIME - minutes_in_oven

def preparation_time_in_minutes(n_layers):
    """Returns the ammount of time expected to bake a lasagna with n layers"""
    return n_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns the elapsed cooking time"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
