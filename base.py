def sum(a, b, c):
    return a + b + c


def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i] == 1:
            board.append("X")
        elif zState[i] == 1:
            board.append("O")
        else:
            board.append(str(i))

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def checkwin(xState, zState):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X Wins the match!")
            return 1

        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O Wins the match!")
            return 0

    return -1


if __name__ == "__main__":

    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]

    turn = 1
    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("X's chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's chance")
            value = int(input("Please enter a value: "))
            zState[value] = 1

        cwin = checkwin(xState, zState)

        if cwin != -1:
            printBoard(xState, zState)
            print("Match Over")
            break

        if(xState.count(0)+zState.count(0)==9):
                print("It's a tie")
                break

        turn = 1 - turn