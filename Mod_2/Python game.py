#Game iedee
#je bent een persoon in een fantasy wereld je start in een cave met de keuze om of verder te exploren
#in de town ga je alleen maar dood
#uiteindelijk word je aangevallen of welke optie je ook hebt
#de eindbaas kan op 3 manieren worden gehandeld
#je kan wegrennen nadat je tegen hem hebt gepraat
#je kan gewoon niet naar hem toe
#je kan tegen hem vechten
#tegen hem vechten en niet naar hem heen gaan resulteerd in een win
#wegrennen na het praten resulteerd in een faal

name = input('Welcome lone traveller, what is your name? ')
print(f'{name}... Interesting name.')
choice1 = input('There is a cave behind you and a town infront of you. Do you explore the cave or do you go to the town? ')

if choice1 == 'cave':
    print('you chose to enter the cave')
    choice12 = input('you see a figure standing in the shadows do you approach it? ')
    if choice12 == 'yes':
        print('There is a man standing there. His eyes were glowing white and he is wearing a long black coat')
        choice13 = input('The man offers you a longsword it looks used and it glows blue with a red aura do you accept it? ')
        if choice13 == 'yes':
            print('You take the sword you feel powerful.')
            choice14 = input('You thank the man he nods and says you will go far. Do you go outside of the cave or do you wander further? ')
            if choice14 == 'wander further':
                print('You get jumped by 5 bandits')
                choice15 = input('Do you draw your sword and attack the bandits? ')
                if choice15 == 'yes':
                    print('An epic fight enduces and you end up killing the 5 bandits. Their souls enter your sword and the sword starts to glow brighter.')
                    print('You walk outside of the other end of the cave. It has been a while since you had seen the sun')
                    choice16 = input('You see a noble standing in the field do you approach him? ')
                    if choice16 == 'yes':
                        print('You approach the noble.')
                        print(f'Ah {name} I had been expecting you.')
                        print('How do you know my name?')
                        print('That does not matter we shall fight as fate has decided')
                        choice17 = input('do you fight the noble? ')
                        if choice17 == 'yes':
                            print('Ok, lets dance.')
                            print('You end up winning the fight and living a normal life afterwards')
                            raise NameError('you win')
                        else:
                            print('You try to make a run for it.')
                            print('You feel a hard sting in your chest.')
                            raise NameError('You died of a heart attack caused by the noble.')
                    else:
                        print('You made the right choice. The lives of those 5 men was enough bloodshed for today.')
                        print('Life goes on as normal.')
                        raise NameError('You win')
                else:
                    print('What are you? stupid?')
                    raise NameError('you died')
            else:
                print('You walk outside of the cave.')
                print('The man that gave you the sword stands there')
                print(f'Oh? {name} You are not worthy after all?')
                raise NameError('Your head violently pops. You died')
        else:
            print('You dont take the sword and decide to wander further into the cave resulting in you getting jumped by 5 bandits')
        raise NameError('You died.')
    else:
        print('You wandered further into the cave and got jumped by 5 bandits.')
    raise NameError('You died.')
else:
    print('you chose to go to the town')
    choice21 = input('You see a group of men standing in an alley and you see the local tavern where do you go? ')
    if choice21 == 'alley':
        print('You chose to go to the alley')
        print('You end up getting beat up by the men.')
    else:
        print('A few drunk men spot you.')
        print('They start getting mad')
        print('You end up getting into a fight')
        print('You lost the fight')
    raise NameError('You died.')