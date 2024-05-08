def ransom(note: str, magazine: str) -> bool:
    conta=0
    a=""
    b=""
    for i in magazine:
        if i in note:
            a=a+i
        for j in a:
            if j in note:
                conta=conta+1
    if len(note)==conta:
        return True
    else:
        return False

print(ransom("a","b"))
print(ransom("aa", "ab"))
print(ransom("aa","aab"))
print(ransom("tu sei un figo", "bella per te stai zitto. figo di qua e di là"))
print(ransom("","ciao"))
print(ransom("tu sei un figo", "bella per te! ne vuoi stare zitto? figo di qua e di là... senza offesa"))