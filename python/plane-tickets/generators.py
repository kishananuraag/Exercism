"""Functions to automate Conda airlines ticketing system."""

import itertools

def generate_seat_letters(number):
    
    '''
    index = 0
    seat_letters = ['A','B','C','D']
    for seats in range(number):
        yield seat_letters[index]
        if index < 3:
            index += 1
        else : 
            index = 0
    '''
    seat_letters = itertools.cycle('ABCD')
    for seats in range(number):
        yield next(seat_letters)

def generate_seats(number):
    seat = generate_seat_letters(number)
    rows = (number for number in itertools.count(1) if number !=13 for i in range(4))
    for rows,seat in zip(rows,seat):
        yield str(rows) + seat

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_no in seat_numbers:
        yield seat_no+flight_id+('0'*(12-len(seat_no)-len(flight_id)))
