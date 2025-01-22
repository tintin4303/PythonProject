#solution to reeborg's maze level

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_around()
    turn_left()


def jump():
    turn_left()
    while not right_is_clear():
        move()
    else:
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        else:
            turn_left()


while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif front_is_clear() and not right_is_clear():
        move()
    elif not front_is_clear() and right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
        if front_is_clear():
            move()