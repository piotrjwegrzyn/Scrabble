import sys
import random

#game_pool = list("aaaaaaaaaąbbcccćdddeeeeeeeęfgghhiiiiiiiijjkkklllłłmmmnnnnnńooooooóppprrrrsśtttuuwwwwyyyyzzzzzźż")
game_pool = list("nhucgźoróylwmłńoadpteidcezifpsgaoyićawiplozlżnzwreomakjhoitaarunmiłznśiazrąęekweyceentbyabkajid")
scores = {
    'a' : 1,
    'ą' : 1,
    'b' : 3,
    'c' : 2,
    'ć' : 6,
    'd' : 2,
    'e' : 1,
    'ę' : 5,
    'f' : 5,
    'g' : 3,
    'h' : 3,
    'i' : 1,
    'j' : 3,
    'k' : 2,
    'l' : 2,
    'ł' : 3,
    'm' : 2,
    'n' : 1,
    'ń' : 7,
    'o' : 1,
    'ó' : 5,
    'p' : 2,
    'r' : 1,
    's' : 1,
    'ś' : 5,
    't' : 2,
    'u' : 3,
    'w' : 1,
    'y' : 2,
    'z' : 1,
    'ź' : 9,
    'ż' : 5,
}

def isalpha_and_in_pool(pool, word):
    if not(word.isalpha()):
        print("Ya entered some weird stuff")
        return False

    move_score = 0
    player_pool_copy = pool.copy()
    for char in word:
        if (char in player_pool_copy):
            player_pool_copy.remove(char)
        else:
            print("character(s) not in your pool")
            return False
    return True 

def in_dictionary(word):
    f = open('slownik')
    for line in f:
        if (word == line.strip()):
            break
    else:
        print("Word not in dictionary")
        f.close()
        return False
    f.close()
    return True

def remove_from_pool(pool, word):
    for char in word:
        pool.remove(char)

def draw(how_many):
    if (len(game_pool) < how_many):
        print("AND THAT IS THE END")
        sys.exit()
    draw_pool = []
    for i in range(how_many):
        draw_pool.append(game_pool.pop(random.randint(0, len(game_pool)-1)))
    return draw_pool

def count_score(word):
    move_score = 0
    for char in word:
        move_score += scores[char]
    return move_score


player_score = 0
player_pool = draw(7)

while True:
    print("------------------------")
    print("LETTERS LEFT: {0}".format(len(game_pool)))
    print("YOUR SCORE IS: {0}".format(player_score))
    print(player_pool)
    print("You gotta choose:")
    print("1 -> make a move")
    print("2 -> draw some letters")
    print("3 -> exit")
    player_choice = int(input())

    if (player_choice == 1):
        word = input("enter word: ")
        if (isalpha_and_in_pool(player_pool, word)):
            if (in_dictionary(word)):
                temp_score = count_score(word)
                print("You scored -> {0} <- for entering word -> {1} <-".format(temp_score, word))
                player_score += temp_score
                remove_from_pool(player_pool, word)
                temp = draw(len(word))
                player_pool.extend(temp)

    elif (player_choice == 2):
        word = input("what letters ya wanna exchange: ")
        if (isalpha_and_in_pool(player_pool, word)):
                remove_from_pool(player_pool, word)
                temp = draw(len(word))
                player_pool.extend(temp)
                print("Here you go -> ", temp)
    elif (player_choice == 3):
        break
    else:
        print("smth went wrong")