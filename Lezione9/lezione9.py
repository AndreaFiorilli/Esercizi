def anagram(s: str, t: str) -> bool:
    s1=s.lower()
    t1=t.lower()
    conta=0
    conta1=0
    for i in s1:
        conta1 += 1
        if i in t1:
            conta += 1
    
    if conta == conta1:
        return True
    else:
        return False
    