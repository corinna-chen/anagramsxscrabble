#imported pygame from Python
import pygame 
pygame.init()
#imported time from Python
import time
#imported threading from Python 
import threading 
#imported random from Python
import random 
#imports english dictionary from Python
import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()

def game_countdown():
    global countdown_time 
    countdown_time = 30 

    for i in range(countdown_time):
        countdown_time = countdown_time - 1
        time.sleep(1)  

def results_countdown():
    global result_time 
    result_time = 10 

    for i in range(countdown_time):
        result_time = result_time - 1
        time.sleep(1)  

#generates a random word
def generate_word():
    global word_length
    global number
    total_words = len(word_list)
    b = int(total_words)
    number = random.randint(0,b)
    word_length = len(word_list[number])

#to pick the length of the word
def word_set_length(length):
    generate_word()
    #checks that the word is the length we want
    while(int(word_length) != int(length)):
        generate_word()
        if(int(word_length) == int(length)):
            #print("Word:" + " " + str(word_list[number]))
            break
        else:
            continue

#scrambles word
#word_list[number] <-- this is our word each time
def scramble_word(word):
    global scrambled_word
    scrambled_word = ''.join(random.sample(word, len(word)))
    scrambled_word = scrambled_word.lower()

# prints out items from the data abstraction vertically
def print_data_abstraction(x,y, start_y,data_abstraction): 
    for word in data_abstraction: 
        #ensures word prints on the screen
        if x < 0 and y > 500: 
            y = start_y
            x = 10
        elif y > 500: 
            y = start_y
            x += 300 
        elif x < 0:
            x = 10
        else:
            y += 40

        text = font.render(word, 1, (255,0,0))
        screen.blit(text, (x, y))
        pygame.display.update() 


def playing_screen():
    global x_spot
    global y_spot
    screen.fill((213, 221, 236))
    pygame.display.update()
    
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render('words guessed!', 1, (255,0,0))
    screen.blit(text, (400, 10))
    text = font.render('letters:' + str(scrambled_word), 1, (255,0,0))
    screen.blit(text, (20,10))

    #procedural abstraction called here!
    print_data_abstraction(-580, 550, 120, guess_list)

    if countdown_time < 5:
        text = font.render('Get your last words in!', 1, (255,0,0))
        screen.blit(text, (90, 70))

    pygame.display.update()


global total_points
total_points = 0

global word_points 
word_points = 0

#key holds the word, value is the points the word earned
total_words = {

}

one_point = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r']
two_points = ['d', 'g']
three_points = ['b', 'c', 'm', 'p']
four_points = ['f', 'h', 'v', 'w', 'y']
five_points = ['k']
eight_points = ['j', 'x']
ten_points = ['q', 'z']
guess_list = []

screen_width = 1100
screen_height = 700
pygame.display.set_caption("anagrams x scrabble")
screen = pygame.display.set_mode((screen_width, screen_height))

word_set_length(6)
scramble_word(word_list[number])

screen.fill((213, 221, 236))
font = pygame.font.SysFont('comicsans', 50)
text = font.render('Welcome to anagramsxscrabble!', 1, (255,0,0))
screen.blit(text, (100,100))
text = font.render('Make words out of the given letters!', 1, (255,0,0))
screen.blit(text, (100,150))
text = font.render('tip: when you get stuck press 1 to resuffle the words!', 1, (255,0,0))
screen.blit(text, (100,200))
text = font.render('Do you understand how to play? (yes or no)', 1, (255,0,0))
screen.blit(text, (100,250))
pygame.display.update()

understand = input("do you understand how to play? ('yes' or 'no')")
while understand == 'no':
    text = font.render('Given the letters, makes words out of them', 1, (255,0,0))
    screen.blit(text, (100,300))
    text = font.render('For example, given the letters pyalre', 1, (255,0,0))
    screen.blit(text, (100,350))
    text = font.render('you can make words like player, play, lay, layer, etc.', 1, (255,0,0))
    screen.blit(text, (100,400))
    understand = input("do you understand how to play? ('yes' or 'no')")
    pygame.display.update()

correct = True
countdown_thread = threading.Thread(target = game_countdown)
countdown_thread.start()
playing_screen()

while countdown_time > 0:
    #pygame.time.delay(50)
    guess = input("word:" + " ")
    guess = guess.lower() 
    if guess in word_list:
        for letter in guess: 
            if letter in word_list[number]:
                if letter in one_point:
                    total_points += 1
                    word_points += 1
                elif letter in two_points: 
                    total_points += 2
                    word_points += 2
                elif letter in three_points:
                    total_points += 3
                    word_points += 3
                elif letter in four_points: 
                    total_points += 4
                    word_points += 4
                elif letter in five_points:
                    total_points += 5
                    word_points += 5
                elif letter in eight_points:
                    total_points += 8
                    word_points += 8
                elif letter in ten_points:
                    total_points += 10
                    word_points += 10
            else:
                correct = False
    
    if correct == False:
        total_points -= word_points
        word_points = 0

    if word_points > 0:
        #if word has already been guessed, it doesn't count it again
        if guess in total_words:
            total_points -= word_points
        #appends key (the correct guess) and its value to the data abstraction 
        total_words[guess] = word_points 
        word_points = 0

    x_guess = 20
    y_guess = 40
        
    if guess == '1': 
        scramble_word(word_list[number])
    else:
        font = pygame.font.SysFont('comicsans', 60)
        text = font.render(str(guess), 1, (255,0,0))
        screen.blit(text, (x_guess, y_guess))
        guess_list.append(guess)
    
    if guess != '1':
        y_guess += 60
    if y_guess >= 500: 
        x_guess += 300
        y_guess = 40
        y_guess += 20
    
    playing_screen()
    pygame.display.update()


screen.fill((51,255,252))
text = font.render('total:' + ' ' + str(total_points), 1, (255,0,0))
screen.blit(text, (10, 10))
pygame.display.update()
countdown_thread = threading.Thread(target = results_countdown)
countdown_thread.start()

while result_time > 0:
    font = pygame.font.SysFont('comicsans', 60)

    #when the game is over print the total words
    print_data_abstraction(10, 60, 60, total_words)

    
    x_spot = 200
    y_spot = 60
    for word in total_words:
        if x_spot < 0 and y_spot > 500: 
            y_spot = 60
            x_spot = 10
        elif y_spot > 500: 
            y_spot = 60
            x_spot += 300 
        elif x_spot < 0:
            x_spot = 10
        else:
            y_spot += 40

        text = font.render(str(total_words[word]), 1, (255,0,0))
        screen.blit(text, (x_spot, y_spot))
        pygame.display.update()


    