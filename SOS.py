'''
    Author: Adham Khaled
    Date: 2022/ 02/ 23
    Version: 1.0
'''


# takes input from the user and makes sure it's correct
def user_input():

    player = input().replace(" ", "")

    # if the input isn't a number it prints an error message and takes another input and recurses
    if not player.isdigit():

        print("wrong input please try again")
        return user_input()

    # if the number is less than 1 or bigger than 16 then it recurses because the number is out of bounds
    if int(player) < 1 or int(player) > 16:

        print("this number is out of range please choose a valid number from 1 to 16")
        return user_input()

    # if the input is less than 10 it puts a space before the input and checks if it's a valid number
    # if it's not valid then it recurses
    if int(player) < 10:

        player = " " + player

        if player in table:

            return player

        else:

            print("this number has already been played please try another valid number")
            return user_input()

    # checks if the number is valid if it's not it recurses
    else:

        if player in table:

            return player

        else:

            print("this number has already been played please try another valid number")
            return user_input()


# takes the user's input and puts it in the table
# then checks if the user got SOS then it increases the score of the player
# then returns true so that he can play the next turn
def play(player_1, table):

    player = user_input()
    print("please enter S or O")
    choice = input()
    loop = False

    # while the input is wrong it takes new input
    while choice != "s" and choice != "o" and choice != "S" and choice != "O":

        print("please choose a valid input (either s or o)")
        choice = input()

    choice = choice.upper()
    # puts either an S or an O in the game table depending on the user's choice
    # notice that for every 3 indexes we have a letter ex:| S| O| S|
    table = table.replace(player, " " + choice)
    player = (int(player.replace(" ", "")))
    player = player * 3 - 1
    player += int((((player + 1) / 3) - 1) / 4) * 2

    # if the player played S then there's 8 possibilities
    # if we represent them on an x and y axis we will have the following
    # (x, 0), (0, y), (x, y), (x, -y), (-x, 0), (0, -y), (-x, -y), (-x, y)
    if choice == "S":

        if player + 6 < len(table):

            if table[player + 3] == "O" and table[player + 6] == "S":
                player_1 += 1
                loop = True

        if player - 6 >= 0:

            if table[player - 3] == "O" and table[player - 6] == "S":
                player_1 += 1
                loop = True

        if player + 28 < len(table):

            if table[player + 14] == "O" and table[player + 28] == "S":
                player_1 += 1
                loop = True

        if player - 28 >= 0:

            if table[player - 14] == "O" and table[player - 28] == "S":
                player_1 += 1
                loop = True

        if player + 34 < len(table):

            if table[player + 17] == "O" and table[player + 34] == "S":
                player_1 += 1
                loop = True

        if player - 34 >= 0:

            if table[player - 17] == "O" and table[player - 34] == "S":
                player_1 += 1
                loop = True

        if player + 22 < len(table):

            if table[player + 11] == "O" and table[player + 22] == "S":
                player_1 += 1
                loop = True

        if player - 22 >= 0:

            if table[player - 11] == "O" and table[player - 22] == "S":
                player_1 += 1
                loop = True

    # if the player chooses an O then we have 4 possibilities in all of them we will have an S on each side of the O
    # if we are going to represent them on a Y and X axis we will have the following
    # ((x, 0), (-x, 0)), ((0, y), (0, -y)), ((x, y), (-x, -y)), ((-x, y), (x, -y))
    else:

        if player - 3 >= 0 and player + 3 < len(table):

            if table[player - 3] == "S" and table[player + 3] == "S":
                player_1 += 1
                loop = True

        if player - 14 >= 0 and player + 14 < len(table):

            if table[player + 14] == "S" and table[player - 14] == "S":
                player_1 += 1
                loop = True

        if player - 17 >= 0 and player + 17 < len(table):

            if table[player + 17] == "S" and table[player - 17] == "S":
                player_1 += 1
                loop = True

        if player - 11 >= 0 and player + 11 < len(table):

            if table[player + 11] == "S" and table[player - 11] == "S":
                player_1 += 1
                loop = True

    return loop, table, player_1


# checks which player has a bigger score and then asks if the players want to play again
# if they want to play again it returns True to the game loop if they don't it returns False
def print_winner(player_1, player_2):

    if player_1 > player_2:

        print("player 1 wins")

    elif player_1 < player_2:

        print("player 2 wins")

    else:

        print("\tDraw")

    print("type 1 if you want to play again and 0 if you want to quit")
    player = input().replace(" ", "")

    # the loop keeps going asking for a new input until the user enters a valid number
    while player != "1" and player != "0":

        print("invalid number please try again")
        print("type 1 if you want to play again and 0 if you want to quit")
        player = input().replace(" ", "")

    if player == "1":

        return True

    else:

        return False


# the game table that gets printed numbers less than 10 have a space before them
# to make them 2 spaces long and the table would look good
table = "| 1| 2| 3| 4|\n| 5| 6| 7| 8|\n| 9|10|11|12|\n|13|14|15|16|\n"
# player 1 and player 2's score and a counter to count turns and check when the game ends
player_1 = 0
player_2 = 0
counter = 0
game = True

# game loop
while game:

    # a loop for the first player because if gets SOS he will play again if not the loop breaks
    loop = True
    while loop:

        #   if counter = 16 that means that there is no more available plays and the loop breaks
        if counter == 16:

            break

        # prints the table and takes input from the user
        counter += 1
        print(table)
        print("player one's turn")
        loop, table, player_1 = play(player_1, table)

    if counter == 16:

        game = print_winner(player_1, player_2)
        # it resets every variable to it's original value
        # if the user wants to play again the game variable will be True and the loop will end
        table = "| 1| 2| 3| 4|\n| 5| 6| 7| 8|\n| 9|10|11|12|\n|13|14|15|16|\n"
        player_1 = 0
        player_2 = 0
        counter = 0
        continue

    loop = True
    while loop:

        if counter == 16:

            break

        counter += 1
        print(table)
        print("player two's turn")
        loop, table, player_2 = play(player_2, table)

    if counter == 16:

        game = print_winner(player_1, player_2)
        table = "| 1| 2| 3| 4|\n| 5| 6| 7| 8|\n| 9|10|11|12|\n|13|14|15|16|\n"
        player_1 = 0
        player_2 = 0
        counter = 0
        continue
