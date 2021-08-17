import random

# generating a 4*4 matrix
# with all entries as 0, denoting the empty position

def start_game(): 
    mat = []
    for i in range(4) :
        mat.append([0] * 4)
    return mat

# adding random new 2 at the empty position

def add_new_2(mat) :    
    r = random.randint(0, 3)      # generating random row number
    c = random.randint(0, 3)      # generating random column number
    while (mat[r][c] != 0) :          # keep generating random value if the position is not empty
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2
    
def reverse(mat) :
    new_mat = []
    for i in range(4) :
        new_mat.append([])
        for j in range(4) :
            new_mat[i].append(mat[i][4 - j - 1])
            
    return new_mat

def transpose(mat) :
    new_mat = []
    for i in range(4) :
        new_mat.append([])
        for j in range(4) :
            new_mat[i].append(mat[j][i])
    return new_mat
    
    
def merge(mat) :
    changed = False
    for i in range(4) :
        for j in range(3) :
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0 :
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True
    return mat, changed

def compress(mat) :
    changed = False
    # new matrix with all entries as 0 
    new_mat = []
    for i in range(4) :
        new_mat.append([0]*4)
        
    for i in range(4) :
        pos = 0
        for j in range(4) :
            if mat[i][j] != 0 :
                new_mat[i][pos] = mat[i][j]
                # if position is changing then the change is happening
                if j != pos :
                    changed = True
                pos +=  1
    return new_mat, changed

def move_up(grid):
    '''
    # perform TRANSPOSE-COMPRESS-MERGE-COMPRESS-TRANSPOSE
    
    reversed_grid = reverse(grid)
    new_grid = compress(grid)
    new_grid = mrege(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid
    '''
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid, changed

def move_down(grid):
    '''
    # perform REVERSE-COMPRESS-MERGE-COMPRESS-REVERSE
    
    transposed_grid = transpose(grid)
    reversed_grid = reverse(grid)
    new_grid = compress(grid)
    new_grid = mrege(new_grid)
    new_grid = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid
    '''
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid, changed

def move_right(grid):
    '''
    # perform REVERSE-COMPRESS-MERGE-COMPRESS-REVERSE
    
    reversed_grid = reverse(grid)
    new_grid = compress(grid)
    new_grid = mrege(new_grid)
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid
    '''
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid, changed

def move_left(grid):
    '''
    # perform COMPRESS MERGE COMPRESS
    
    new_grid = compress(grid)
    new_grid = mrege(new_grid)
    new_grid = compress(new_grid)
    return new_grid
    
    '''
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    return new_grid, changed               

    
def get_current_state(mat) :
    # anywhere 2048 is present
    for i in range(4) :
        for j in range(4) :
            if (mat[i][j] == 2048) :
                return "WON"
    
    # anywhere 0 is present
    for i in range(4) :
        for j in range(4) :
            if(mat[i][j]) == 0 :
                return "GAME NOT OVER"
            
    # Every row and column except last row and last column
    # still in the game if anywhere consecutive numbers are same - in the range of 3
    for i in range(3) :
        for j in range(3) :
            if(mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]):
                return "GAME NOT OVER"
    
    # last row
    # 3rd row
    for j in range(3) :
        if mat[3][j] == mat[3][j + 1] :
            return "GAME NOTE OVER"
             
    # last column
    # 3rd column
    for i in range(3) :
        if mat[i][3] == mat[i + 1][3] :
            return "GAME NOT OVER"
        
    return "LOST"