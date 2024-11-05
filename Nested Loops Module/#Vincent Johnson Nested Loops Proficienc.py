#Vincent Johnson Nested Loops Proficiency Test
import random
al = []
board = ["_", "|", "_", "|", "_"]
board2 = ["_", "|", "_", "|", "_"]
board3 = ["_", "|", "_", "|", "_"]
divider = ["---------------------"]
wins = 0
wins2 = 0
    
def main(board, board2, board3, wins, divider, wins2, al):
    if wins >= 1:
        print("You won!")
        return
    if wins2 >= 1:
        print("Computer won!")
        return
    while wins2 == 0:
        while wins == 0:
            if wins >= 1:
                print("You won!")
                break
            if wins2 >= 1:
                print("Computer won!")
                break
            print("\n\nPosition naming: 1 top left, 3 top right, 7 bottom right, 9 bottom left, 5 in the middle.\n")
            print(f"{board}\n{divider}\n{board2}\n{divider}\n{board3}\n Here is your board^^^")
            placing = int(input("What place do you want to put an X?\n"))
            al.append(placing)
            if placing <= 0:
                print("That isn't a correct placing")
            elif placing <= 3:
                if placing == 1:
                    board[0] = "X"
                elif placing == 2:
                    board[2] = "X"
                elif placing == 3:
                    board[4] = "X"
            elif placing <= 6:
                if placing == 4:
                    board2[0] = "X"
                elif placing == 5:
                    board2[2] = "X"
                elif placing == 6:
                    board2[4] = "X"
            elif placing <= 9:
                if placing == 7:
                    board3[0] = "X"
                elif placing == 8:
                    board3[2] = "X"
                elif placing == 9:
                    board3[4] = "X"
            elif placing > 9:
                print("That isn't a correct placing")
            print(f"{board}\n{divider}\n{board2}\n{divider}\n{board3}\n Here is your board^^^")
            if board.count("X") >= 3:
                wins +=1
            if board2.count("X") >= 3:
                wins +=1
            if board3.count("X") >= 3:
                wins +=1
            if board[0].count("X") > 0:
                if board2[0].count("X") > 0:
                    if board3[0].count("X") > 0:
                        wins +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
                elif board2[2].count("X") > 0:
                    if board3[4].count("X") > 0:
                        wins +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
            elif board[2].count("X") > 0:
                if board2[2].count("X") > 0:
                    if board3[2].count("X") > 0:
                        wins +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
            elif board[4].count("X") > 0:
                if board2[4].count("X") > 0:
                    if board3[4].count("X") > 0:
                        wins +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
                elif board2[2].count("X") > 0:
                    if board3[0].count("X") > 0:
                        wins +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
            else:
                pass
            rndm = random.randint(1,9)
            while rndm == placing:
                rndm = random.randint(1,9)
            if al.count(str(rndm)) >= 1:
                rndm = random.randint(1,9)
            if rndm <= 3:
                if rndm == 1:
                    board[0] = "O"
                elif rndm == 2:
                    board[2] = "O"
                elif rndm == 3:
                    board[4] = "O"
            elif rndm <= 6:
                if rndm == 4:
                    board3[0] = "O"
                elif rndm == 5:
                    board2[2] = "O"
                elif rndm == 6:
                    board2[4] = "O"
            elif rndm <= 9:
                if rndm == 7:
                    board3[0] = "O"
                elif rndm == 8:
                    board3[2] = "O"
                elif rndm == 9:
                    board3[4] = "O"


            if board.count("O") >= 3:
                wins2 +=1
            if board2.count("O") >= 3:
                wins2 +=1
            if board3.count("O") >= 3:
                wins2 +=1
            if board[0].count("O") > 0:
                if board2[0].count("O") > 0:
                    if board3[0].count("O") > 0:
                        wins2 +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
                elif board2[2].count("O") > 0:
                    if board3[4].count("O") > 0:
                        wins2 +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
            elif board[2].count("O") > 0:
                if board2[2].count("O") > 0:
                    if board3[2].count("O") > 0:
                        wins2 +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
            elif board[4].count("O") > 0:
                if board2[4].count("O") > 0:
                    if board3[4].count("O") > 0:
                        wins2 +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
                elif board2[2].count("O") > 0:
                    if board3[0].count("O") > 0:
                        wins2 +=1
                        main(board, board2, board3, wins, divider, wins2, al)
                        break
            else:
                pass
        break
main(board, board2, board3, wins, divider, wins2, al)