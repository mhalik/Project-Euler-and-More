# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 08:08:13 2014

@author: Max
"""

computer_choice=randint(1,6)

def game_choice(n):
    if n==1:
        return 'Rock'
    if n==2:
        return 'Paper'
    if n==3:
        return 'Scissors'
    if n==4:
        return 'Lizard'
    if n==5:
        return 'Spock'

computer_action=game_choice(computer_choice)

user_choice=input('What is your choice? ')
def game_choice_human(n):
    n=n.lower()
    if n[0]=='r':
        return 'Rock'
    if n[0]=='p':
        return 'Paper'
    if n[0]=='s' and n[1]=='c':
        return 'Scissors'
    if n[0]=='l':
        return 'Lizard'
    if n[0]=='s' and n[1]=='p':
        return 'Spock'
    else:
        return 'You spelled something very wrong! Try again!'
        
user_action=game_choice_human(user_choice)
if user_action=='You spelled something very wrong! Try again!':
    print(user_action)
def game_action(computer,human):
    if computer==human:
        return 'It is a tie! Play again soon!'
    if computer=='Paper' and human=='Scissors':
        return ['human','Scissors cut paper!']
    if computer=='Scissors' and human=='Rock':
        return ['human','Rock breaks scissors!']
    if computer=='Rock' and human=='Paper':
        return ['human','Paper covers rock!']
    if computer=='Lizard' and human=='Rock':
        return ['human','Rock crushes Lizard!']
    if computer=='Spock' and human=='Lizard':
        return['human','Lizard poisons Spock!']
    if computer=='Spock' and human=='Paper':
        return['human','Paper disproves Spock!']
    if computer=='Rock' and human=='Spock':
        return['human','Spock vaporizes Rock!']
    if computer=='Scissors' and human=='Spock':
        return['human','Spock smashes Scissors!']
    if computer=='Lizard' and human=='Scissors':
        return['human','Scissors decapitate Lizard!']
    if computer=='Paper' and human=='Lizard':
        return['human','Lizard eats paper!']
    
    
    if human=='Paper' and computer=='Scissors':
        return ['computer','Scissors cut paper!']
    if human=='Scissors' and computer=='Rock':
        return ['computer','Rock breaks scissors!']
    if human=='Rock' and computer=='Paper':
        return ['computer','Paper covers rock!']
    if human=='Lizard' and computer=='Rock':
        return ['computer','Rock crushes Lizard!']
    if human=='Spock' and computer=='Lizard':
        return['computer','Lizard poisons Spock!']
    if human=='Spock' and computer=='Paper':
        return['computer','Paper disproves Spock!']
    if human=='Rock' and computer=='Spock':
        return['computer','Spock vaporizes Rock!']
    if human=='Scissors' and computer=='Spock':
        return['computer','Spock smashes Scissors!']
    if human=='Lizard' and computer=='Scissors':
        return['computer','computer decapitate Lizard!']
    if human=='Paper' and human=='Lizard':
        return['computer','computer eats paper!']
        
result=game_action(computer_action,user_action)
winner=result[0]
story=result[1]
print('The winner is the %s! %s' % (winner,story) )
