from tttlib import *

def main():

   T=genBoard()
   gameNotOver= True
   
   printBoard(T)
   
   while gameNotOver:
      
      #ask user for input
      moveX = input("X move? \n")
      userMove=int(moveX)
      
      #check valid move
      if userMove<-1 or userMove>9:
          print("Not in range")
      if T[userMove]!=0:
          print("Spot is taken")
      else:
         
         #set gameboard position to player's move (denoted by 1) if move is valid
          T[userMove] = 1
          
         #check if/how game has ended
          state = analyzeBoard(T)
          if state==1:
             print("You won!")
             gameNotOver=False
          elif state==3:
             print("Draw")
             gameNotOver = False
      printBoard(T)

      #computer's turn below
      if gameNotOver == True:
         if int(genOpenMove(T))== -1:
          return 1
         elif getWinningMove(T,2)!=-1:
            o=int(getWinningMove(T,2))
         elif genNonLoser(T,2)!=-1:
            o=int(genNonLoser(T,2))
         else:
            o = int(genRandomMove(T, 2))
            if o<-1 or o>9:
               print("Not in range")
               if T[o]!=0:
                  print("Spot is taken")
            
      #set gameboard position tocomputer's move (denoted by 2) if move is valid
         T[o] = 2
      
      #check if/how game has ended
         state = analyzeBoard(T)
         if state==2:
             print("O won")
             gameNotOver = False
         elif state==3:
             print("Draw")
             gameNotOver = False
         printBoard(T)
