class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        default = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        to_change = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        
        #print(to_change[1])
        pos=[0,3,6]
        for x in pos:
            for y in pos: 
                to_change=dict(default)
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if board[i][j] == ".":
                            continue
                        elif to_change[int(board[i][j])] == 0:
                            to_change[int(board[i][j])]=1
                        else: 
                            print("false1")
                            return False
        
        for i in range(9):
            to_change=dict(default)
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif to_change[int(board[i][j])] == 0:
                    print("check")
                    to_change[int(board[i][j])]=1
                else: 
                    print("false2")
                    return False

            
        for i in range(9):
            to_change=dict(default)
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif to_change[int(board[j][i])] == 0:
                    to_change[int(board[j][i])]=1
                else: 
                    print("false3")
                    return False
    

        return True


