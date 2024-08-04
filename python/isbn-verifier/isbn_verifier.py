def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn)!=10: return False
    nums = list(isbn)
    if nums[-1] == "X": nums[-1] = "10"
    if not all([num.isdigit() for num in nums]): return False
    return sum([int(x)*y for x,y in zip(nums,range(10,0,-1))]) %11 == 0