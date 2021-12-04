#day four
import re

def textToArray(fname):
    '''
    just parse the input file and split into the input numbers and the boards
    '''
    boards = []

    with open(fname) as f:
        #first line is numbers called out
        input_nums = f.readline()

        for line in f:
            boards.append(line.strip())

    f.close()

    all_boards = []
    temp_board = []

    for line in boards:
        if line != '':
            temp_board.append(line)
        else:
            all_boards.append(temp_board)
            temp_board = []

    all_boards.append(temp_board)

    return input_nums, all_boards[1:]

def properBoard(board):
    '''
    convert each board list of strs -> list of lists
    '''
    cur_line = []
    final_board = []

    for line in board:
        cur_line = re.sub(' +', ' ', line)
        final_board.append(cur_line.split())
        
    return final_board

def createAllProperBoards(boards):
    '''
    list of boards
    '''
    all_boards = [properBoard(board) for board in boards]
    return all_boards

def checkNumberInBoard(board, num):
    '''
    check if number is in the board, and return its position 
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == num:
                return [i,j]

    return None

def findBoardScore(board):
    '''
    find total sum of board
    '''
    score = 0

    for line in board:
        score += sum([int(val) for val in line])

    return score

def findWinLoseBoard(inputs, boards):
    '''
    main fn - find the winning and losing boards
    '''
    board_count = len(boards)
    board_scores = [findBoardScore(board) for board in boards]
    meta_boards = [[[0]*5, [0]*5] for _ in range(board_count)] #keep track of how many numbers in each [row, col] have been filled

    first_board_score = 0
    last_board_score = 0

    for num in inputs:
        boards_in_running = []
        for i,board in enumerate(boards):
            #continue only for boards that have not been completed yet
            if not(5 in meta_boards[i][0]) and not(5 in meta_boards[i][1]): 
                boards_in_running.append(i)

                pos = checkNumberInBoard(board, num)
                if pos:
                    board_scores[i] -= int(num)
                    #print(board_scores, meta_boards[i])

                    meta_boards[i][0][pos[0]] += 1
                    meta_boards[i][1][pos[1]] += 1

                    #to check the first winning board (part 1)
                    if not first_board_score and (5 in meta_boards[i][0] or 5 in meta_boards[i][0]):
                        first_board_score = board_scores[i] * int(num)

        #to check the losing board / last board to win (part 2)
        if len(boards_in_running) == 1 and (5 in meta_boards[boards_in_running[0]][0] or 5 in meta_boards[boards_in_running[0]][1]):
            last_board_score = board_scores[boards_in_running[0]]*int(num)
            return first_board_score, last_board_score


#file = '/Users/mohana/Documents/mohana/code n shit/advent_of_code/sample.txt'
file = './data/day_four_input.txt'
ip, b = textToArray(file)

#reformat the input
boards = createAllProperBoards(b)
inputs = ip.strip().split(',')

print(findWinLoseBoard(inputs,boards))
