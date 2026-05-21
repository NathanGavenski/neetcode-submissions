from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transposed = list(zip(*board))
        squares = defaultdict(list)
        for row in range(len(board)):
            # check row and col
            numsb, numst = [], []
            for valueb, valuet in zip(board[row], transposed[row]):
                if valueb != ".":
                    value = int(valueb)
                    if value in numsb:
                        return False
                    numsb.append(value)

                if valuet != ".":
                    value = int(valuet)
                    if value in numst:
                        return False
                    numst.append(value)

            # check 3x3 grid
            for col in range(len(board[0])):
                value = board[row][col]
                if value != ".":
                    value = int(value)
                    if value in squares[(row // 3, col // 3)]:
                        return False
                    squares[(row // 3, col // 3)].append(value)
        return True
        