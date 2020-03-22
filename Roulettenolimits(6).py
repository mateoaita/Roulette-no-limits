import random
import matplotlib
import matplotlib.pyplot as plt

class Bettor(object):
    def __init__(self, wealth,bet,choice,rollnumber,turn,acumulatedwealth):
        self.wealth = wealth
        self.bet = bet
        self.choice = choice
        self.rollnumber = rollnumber
        self.turn =turn
        self.acumulatedwealth = acumulatedwealth
Bettor.wealth=0
Bettor.rollnumber=[]
Bettor.turn=0
Bettor.acumulatedwealth=[]
def Parameters():
    if Bettor.wealth==0:
        Bettor.wealth=input("starting wealth is:")
    else:
        print('Your current wealth is :'+ str(Bettor.wealth))
    Bettor.wealth=int(Bettor.wealth)
    Bettor.bet=input("How much do u wanna bet?:")
    Bettor.bet = int(Bettor.bet)

    while not Bettor.bet  in range(0,Bettor.wealth):
        Bettor.bet = input("Choose within your restriction:")
        Bettor.bet = int(Bettor.bet)

    Bettor.choice= input("choose number, type O for Odd or E for Even:")
    Bettor.choice=Bettor.choice.upper()

    while Bettor.choice not in 'O E'.split():
        print("Choose between the given options")
        Bettor.choice = input("choose color type R for red or B for black:")

    if Bettor.choice=='E':
        Bettor.choice='2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36'.split()
    else:
        Bettor.choice='1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35'.split()
def Roll():
    Bettor.turn+=1
    roll=random.randint(1,37)
    roll=str(roll)
    print('the number is '+roll)
    if roll in Bettor.choice:
        print('You won '+str(Bettor.bet*2)+' Dollars')
        Bettor.wealth+=Bettor.bet
        print('Remaining wealth = '+str(Bettor.wealth))
    else:
        print('You lost ' + str(Bettor.bet) + ' Dollars')
        Bettor.wealth-=Bettor.bet
        print('Remaining wealth = '+str(Bettor.wealth))
    Bettor.rollnumber.append(Bettor.turn)
    Bettor.acumulatedwealth.append(Bettor.wealth)
    PlayAgain()

def PlayAgain():
    pa = input("Wanna play again?, type yes if you do:")
    if pa== 'yes':
        Parameters()
        Roll()
    else:
        print(Bettor.rollnumber)
        print(Bettor.acumulatedwealth)
        plt.plot(Bettor.rollnumber, Bettor.acumulatedwealth)
        plt.ylabel('Accumulated Wealth')
        plt.xlabel('Turns')
        plt.show()
Parameters()
Roll()