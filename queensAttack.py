import os

def main():
    def readText():
        try:
            if os.stat('archivo.txt').st_atime > 0:
                file = open('archivo.txt', 'r')
                list_lines = file.readlines()
                file.close()
                fulfill = validator(list_lines)
                if fulfill['cumple']:
                    varFormat(fulfill['lista'])
                else:
                    print(fulfill['error_message'])
            else:
                print('The file is empty')
        except Exception as e:
            print('can not read the file, pleace check it '+str(e))

    def validator (list_lines):
        validator = True
        list_validator = []
        error_message = ''
        if len(list_lines) >= 2:
            for index, linea in enumerate(list_lines):
                line = linea.split()
                if len(line) == 2:
                    if int(line[0]) < 0 or int(line[1]) < 0:
                        error_message = 'the numbers should not be negative'
                        validator = False
                        break
                    else:
                        if index == 0:
                            matrizT = int(line[0])
                            if int(line[1]) != len(list_lines) - 2:
                                error_message = 'the number of obstacles does not match'
                                validator = False
                                break
                        if matrizT < int(line[0]) or matrizT < int(line[1]):
                            error_message = 'The position'+line[0]+', '+line[1]+' it is not found inside the matrix'
                            validator = False
                            break
                else:
                    error_message = 'Must enter positions'
                    validator = False
                    break
                list_validator.append(line)
        else:
            validator = False
            error_message = 'You must enter more data'

        return {'validator': validator, 'error_message': error_message, 'list': list_validator}

    def varFormat(lista):
        obst = {}
        queenP =[]
        for idxRow, row in enumerate(lista):
            obstl = []
            if idxRow == 0:
                lenM = int(row[0])
            elif idxRow == 1:
                queenP.append(int(row[0]))
                queenP.append(int(row[1]))
            else:
                obstl.append(int(row[0]))
                obstl.append(int(row[1]))
                obst[idxRow-2] = obstl
        fillMatriz(lenM, queenP, obst)

    def fillMatriz(lenM, queenP, obst):
        board = crearMatriz(lenM)
        putObstacules(board, obst)
        solve(lenM, queenP, board)

    def crearMatriz(n):
        chessboard = []
        for i in range(n):
            chessboard.append([0] * n)
        return chessboard

    def putObstacules(board, obst):
        for i in obst:
            board[obst[i][0] - 1][obst[i][1] - 1] = 2

    def print_board(board):
        for i in board:
            pass
            print(i)

    def solve(lenM, queenP, board):
        x = queenP[0]-1
        y = queenP[1]-1
        board[x][y] = 1
        find_way(board, lenM, x, y)
        print_board(board)

    def find_way(board, lenM, x, y):
        rx = lx = srx = slx = irx = ilx = x
        ry = ly = sry = sly = iry = ily = y

        count = 0
        if lenM > rx:
            while countWay(board, lenM, rx-1, y):
                rx = rx-1
                count = count+1
            while countWay(board, lenM, lx+1, y):
                lx = lx+1
                count = count+1
            while countWay(board, lenM, x, ry-1):
                ry = ry-1
                count = count+1
            while countWay(board, lenM, x, ly+1):
                ly = ly+1
                count = count+1
            while countWay(board, lenM, srx+1, sry+1):
                srx = srx+1
                sry = sry + 1
                count = count+1
            while countWay(board, lenM, slx-1, sly-1):
                slx = slx - 1
                sly = sly - 1
                count = count+1
            while countWay(board, lenM, irx+1, iry-1):
                irx = irx + 1
                iry = iry - 1
                count = count+1
            while countWay(board, lenM, ilx-1, ily+1):
                ilx = ilx - 1
                ily = ily + 1
                count = count+1

        print(count)

    def countWay(board, lenM, x, y):
        if x < 0 or y < 0 or x > lenM-1 or y > lenM-1:
            return False
        if board[x][y] == 0:
            return True
        else:
            return False

    readText()
main()