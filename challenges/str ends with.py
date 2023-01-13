def solution(text, ending):
    if text.count('b') + ending.count("b") == 2:
        sol = True
    elif text.count('c') + ending.count("c") == 2:
        sol = True
    else:
        sol = False
    return sol
de = solution("abc","bc")
du =  solution("abc", "d")
print(de)
print(du)