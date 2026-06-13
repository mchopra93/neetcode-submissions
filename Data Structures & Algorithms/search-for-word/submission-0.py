class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        wordlen = len(word)
        ROWS = len(board)
        COLS = len(board[0])

        def traverse(board,i,j,curr_match=0):

            if curr_match == wordlen:
                    return True

            if i < 0 or i > len(board) -1:
                return False
            if j<0 or j > len(board[0])-1:
                return False
            
            if curr_match<wordlen and board[i][j] == word[curr_match]:
                curr_match+=1
                temp = board[i][j]
                board[i][j] = '#'
                 
                move1=traverse(board,i+1,j,curr_match)
                move2=traverse(board,i-1,j,curr_match)
                move3=traverse(board,i,j+1,curr_match)
                move4=traverse(board,i,j-1,curr_match)

                board[i][j] = temp
                return move1 or move2 or move3 or move4
            else:
                return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if traverse(board,r,c,0):
                    return True

        return False

        