import random

def problem_word(word):
    pw=random.sample(word,len(word)) 
    return "".join(pw)


def check_word(word,score):
    wc=problem_word(word)
    print("Arrange the letters to form a valid words: ")
    print(wc)
    user_word=input()
    print()

    if user_word.upper()==word:
        print("Correct Answer")
        score+=1
    else:
        print("False Answer")
        score-=1
    return score


def puzzle():
    score=0
    word_list=['FATHER','BREAK','COUNTRY','GREEN','AEROPLANE','ALOK']
    words=random.sample(word_list,len(word_list))

    for word in words:
        score=check_word(word,score)
    
    print("your score is : ",score)

puzzle()

    

