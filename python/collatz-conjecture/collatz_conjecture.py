def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    count = 0

    while(number>1):
        count += 1
        if(number%2==0):
            number = int(number/2)
            # print(f"number was even {number}")
        else:
            number = (3*number + 1)
            # print(f"number was odd {number}")
    return count




# steps(12)
