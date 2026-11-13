def find_short(s):
    words = s.split()
    shortest = len(words[0])
    
    for word in words:
        if len(word) < shortest:
            shortest = len(word)
            
    return shortest
​