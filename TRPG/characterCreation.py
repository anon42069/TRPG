
import assets
class Player():
    pass
Player = assets.Player()
# name
print('Traveler, what is thy name?')
Player.name = str(input())
# race array to verify the race is available
raceArr = ['dwarf','elf','human','catfolk','dragonkin','ratfolk','orc','woodfolk']
# choose race

def choiceMenu():
    print('In these lands, there are many folk with different strength and weaknesses')
    print('Dwarf of the stone')
    print('Elve of the magus')
    print('Human of the capital')
    print('Catfolk of the songs')
    print('Dragonkin of the lore')
    print('Ratfolk of the swamp')
    print('Orc of the south')
    print('Woodfolk of the forests')
choiceMenu()
def raceChanger(race):
    Player.race = race
def genderChoice(a):
    if a.lower() == 'sword':
        Player.isMale = True
    if a.lower() == 'shaft':
        Player.isMale = False
    else:
        print('please make a valid selection')
        
        

choice = input()
if choice.lower() in raceArr:
    raceChanger(choice)
else:
    print('please make a valid selection')
    choiceMenu()

# choose gender
print('what genitalia were you born with?')
print('sword\nor\nshaft\n')
genderChoice(input())
# choose class
# create backstory








def main():
    pass