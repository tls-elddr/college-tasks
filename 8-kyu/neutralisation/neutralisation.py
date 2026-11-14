def neutralise(s1, s2):
    result = ""
    
    for a, b in zip(s1, s2):
        if a == "+" and b == "+":
            result += "+"
        elif a == "-" and b == "-":
            result += "-"
        else:
            result += "0"
    
    return result
    pass