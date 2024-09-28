import os
clear = lambda: os.system('clear')
clear()

b = [[9,0,0,0,5,0,0,0,4],
     [0,3,5,0,0,2,0,0,7],
     [8,0,0,0,0,0,3,0,0],
     [0,0,9,0,0,0,0,0,0],
     [0,0,0,0,0,8,0,4,0],
     [0,5,7,0,4,0,6,0,0],
     [0,0,0,1,0,0,0,0,2],
     [0,6,4,0,8,0,7,0,0],
     [3,0,0,0,0,0,0,0,0],
     ]

f = [[9,0,0,0,5,0,0,0,4],
     [0,3,5,0,0,2,0,0,7],
     [8,0,0,0,0,0,3,0,0],
     [0,0,9,0,0,0,0,0,0],
     [0,0,0,0,0,8,0,4,0],
     [0,5,7,0,4,0,6,0,0],
     [0,0,0,1,0,0,0,0,2],
     [0,6,4,0,8,0,7,0,0],
     [3,0,0,0,0,0,0,0,0],
     ]

def prGreen(skk): print("\033[92m{}\033[00m" .format(skk),end="")
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk),end="")

def pt():
    clear()
    for x in range(9):
        for y in range(9):
            if b[x][y] != 0:
                prCyan(b[x][y])
            else:
                if f[x][y] != 0:
                    prGreen(f[x][y])
                else:
                    print(".",end="")
            if y == 2 or y == 5:
                p = 0
                #print("|",end="")
        print()
        if x == 2 or x == 5:
            p= 0
            #
            # print("---+---+---")


def check_rules():
    for j in range(9):
        r = [i for i in f[j] if i != 0]
        if len(r) != len(set(r)):
            return False
    for j in range(9):
        r = [i for i in [f[y][j] for y in range(9)] if i != 0]
        if len(r) != len(set(r)):
            return False
    for j in [0,3,6]:
        for k in [0,3,6]:
            r = [f[j+0][k+0],f[j+0][k+1],f[j+0][k+2],
                f[j+1][k+0],f[j+1][k+1],f[j+1][k+2],
                f[j+2][k+0],f[j+2][k+1],f[j+2][k+2],]
            r = [i for i in r if i != 0]
            if len(r) != len(set(r)):
                return False

    return True

pt()
input()

def bf(i):
    if i == 9*9:
        pt()
        quit()
    if f[i//9][i%9] != 0:
        bf(i+1)
    for v in range(1,10):
        f[i//9][i%9] = v
        pt()
        if check_rules():
            #pt()
            bf(i+1)
        f[i//9][i%9] = 0
        
        
    
bf(0)