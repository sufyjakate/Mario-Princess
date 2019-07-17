def PrincessPath(n, grid):
    
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
    
    # negative row difference implies UP
    # negative col difference implies LEFT
    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]

    final = ''.join([
        'UP\t' * abs(drows) if drows < 0 else 'DOWN\t' * drows,
        'LEFT\t' * abs(dcols) if dcols < 0 else 'RIGHT\t' * dcols])
    
    return final 



if __name__ == "__main__":
    n = int(input('Enter N'))
    grid = [input('grid').strip() for _ in range(n)]
    
    print(PrincessPath(n, grid))
    