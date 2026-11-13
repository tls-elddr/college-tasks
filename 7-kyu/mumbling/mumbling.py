def accum(st):
    result = []
    count = 1
        
    for char in st:
        part = char.upper() + char.lower() * (count - 1)
        result.append(part)
        count +=1
    return "-".join(result)
    pass