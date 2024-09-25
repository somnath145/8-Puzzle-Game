import random
def print_bord(bord):

    for row in bord:
        print(" ".join(str(tile) if tile != 0 else " " for tile in row))
    print()

def solved(goal_bord,board):
    if(goal_bord == board):
        return True

def find_blank(bord):
    for i in range (3):
        for j in range(3):
            if(bord[i][j]==0):
                return i,j

def move_bord(bord,choice):
    x,y = find_blank(bord)

    if(choice == 'u'):
        if(x<2):
            bord[x][y], bord[x+1][y] = bord[x+1][y], bord[x][y]

    elif(choice == 'd'):
        if(x>0):
            bord[x][y], bord[x-1][y] = bord[x-1][y], bord[x][y]

    elif(choice == 'l'):
        if(y<2):
            bord[x][y], bord[x][y+1] = bord[x][y+1], bord[x][y]

    elif(choice == 'r'):
        if(y>0):
            bord[x][y], bord[x][y-1] = bord[x][y-1], bord[x][y]

    else: print("Invalid Choice")

def suffle_bord(bord):
    for i in range(100):
        move_bord(bord,random.choice(['u','d','l','r']))

def main():

    print("Welcome to my PUZZLE game")

    goal_bord = [[1,2,3],
                 [4,5,6],
                 [7,8,0]]
    print("Goal Bord")
    print_bord(goal_bord)
    
    my_bord =  [[0,1,2],
                [3,4,5],
                [6,7,8]]
    suffle_bord(my_bord)
    
    
    while(True):
        print("Bord : ")
        print_bord(my_bord)

        if(solved(goal_bord,my_bord)==True):
            print("Well done...")
            break

        choice = input("Enter Choice : UP -> U , Down -> D , Left -> L , Right -> R : ").lower()
        move_bord(my_bord,choice)


if __name__ == "__main__":
    main()
