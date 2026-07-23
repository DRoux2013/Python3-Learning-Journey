print('How many cats are in your domicile?')
numCats = input()
try:
    if int(numCats) >= 4:
        print ('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except:
    print('You did not enter a number fool!')