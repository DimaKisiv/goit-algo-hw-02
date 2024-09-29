from collections import deque
import re

def palindrome_check(phrase: str) -> bool:
    phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase.lower())
    
    dq = deque(phrase)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


phrases = [
    "this phrase is not a palindrome",
    "Sit on a potato pan, Otis.",
    "Cigar? Toss it in a can. It is so tragic.",
    "Go hang a salami, I'm a lasagna hog.",
    "Taco cat.",
    "Nun.",
    "Mom.",
    "Madam in Eden, I'm Adam.",
    "Go deliver a dare vile dog.",
    "one more not a palindrome phrase"
]

for phrase in phrases:
    result = " є паліндромом" if palindrome_check(phrase) else " не є паліндромом"
    print(f"'{phrase}'{result}.")

