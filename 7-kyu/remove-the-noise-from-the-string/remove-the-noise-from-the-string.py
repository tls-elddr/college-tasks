def remove_noise(st):
    noise = "%$&/#·@|º\ª"
    result = ""
    
    for x in st:
        if x not in noise:
            result += x
    return result       
    pass