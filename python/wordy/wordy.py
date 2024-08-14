def answer(question):
    equation = question.replace("What is ","").replace("?","").replace("minus","-").replace("plus","+").replace("multiplied by", "*").replace("divided by","/").split(' ')

    equation.insert(0,"(")
    equation.insert(4,")")

    not_math_words = [item.isalpha() for item in equation if item not in ('What', 'is')]

    if any(not_math_words):
        raise ValueError("unknown operation")
    try:
        return eval(' '.join(equation))
    except:
        raise ValueError("syntax error")





