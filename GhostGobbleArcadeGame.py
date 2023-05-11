def eat_ghost(has_power_pellet, touching_ghost):
    return has_power_pellet and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(has_power_pellet, touching_ghost):
    return not has_power_pellet and touching_ghost


def win(eaten_all_dots, has_power_pellet, touching_ghost):
    return eaten_all_dots and not lose(has_power_pellet, touching_ghost)
