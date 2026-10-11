def name():
    n = input("Enter your name: ")
    return n

def say_name(n):
    print('Your name is {}.'.format(n))
    
def say_the_name():
    n = name()
    say_name(n)
    
say_the_name()