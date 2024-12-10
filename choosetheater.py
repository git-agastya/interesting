'''
------------
SCREEN
------------
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

'''
import subprocess

theater = []

def buildTherater (size):
    for i in range(size):
        theater.append([0] * size)
    count = 0
    for i in range(size):
        for j in range(size):
            theater[i][j] = count
            count = count + 1

def printThreater():
    print("-----------------")
    print("     SCREEN")
    print("-----------------")
    size = len(theater)
    for i in range(size):
        for j in range(size):
            print(f"{theater[i][j] : ^3}", end=" ")
        print()
        
buildTherater(4)
printThreater()

def allotSeats():
    
    '''
    Ask the user seat number (1-16), update the theater matrix and print
    For a given seat number, how to caluclate row and column ?
    row = 8/4
    column = 8 % 4
    
    '''
    
    
    while True:
        print("Enter a seat number or type a number greater than 15 or less than 0 to get out not schedule a seat.")
        seat=int(input())
        if seat<0 or seat>15:
            break
        row=seat//4
        column=seat%4
        if theater[row][column] =="X":
            print("The seat is already taken so, choose a different seat before they are all gone.")
            return
        else:
            theater[row][column]="X"
        printThreater()
   
allotSeats() 



    
