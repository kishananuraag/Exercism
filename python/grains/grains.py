def square(number):
    if number < 1 or number >64:
        raise ValueError("square must be between 1 and 64")
    square_one = 1
    grains_on_the_number = 1
    while(square_one  < number):
        grains_on_the_number = 2 * grains_on_the_number
        square_one += 1
    return grains_on_the_number

def total():
    square_one = 1
    grains_on_the_number = 1
    total_grains_on_chessboard = 1
    while(square_one  < 64):
        grains_on_the_number = 2 * grains_on_the_number
        square_one += 1
        total_grains_on_chessboard = total_grains_on_chessboard + grains_on_the_number
    return total_grains_on_chessboard

