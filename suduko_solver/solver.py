
'''
Created on 25-Apr-2014

@author: rajavi07
'''

import pprint

sud_arr=[[0,2,0,0,3,0,0,4,0],[6,0,0,0,0,0,0,0,3],[0,0,4,0,0,0,5,0,0],[0,0,0,8,0,6,0,0,0],[8,0,0,0,1,0,0,0,6],[0,0,0,7,0,5,0,0,0],[0,0,7,0,0,0,6,0,0],[4,0,0,0,0,0,0,0,8],[0,3,0,0,4,0,0,2,0]]

#sud_arr=[[0,3,0,0,8,0,0,9,0],[5,0,0,4,0,3,0,0,8],[0,0,2,0,0,0,3,0,0],[0,1,0,9,0,6,0,5,0],[7,0,0,0,0,0,0,0,9],[0,9,0,2,0,1,0,4,0],[0,0,1,0,0,0,9,0,0],[6,0,0,3,0,4,0,0,1],[0,7,0,0,6,0,0,2,0]]

sud_arr=[[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]

XMAX=9
YMAX=9
ZMAX=10

it=0
depth=0

sud_3d_arr=[[[]]]
sud_stats_arr=[[]]



def init_3d_arr (__sud_3d_arr,__init_sud_arr):
    
    
    ##We will first initialize all the cells to zero
    for x in range (0, XMAX):
        __sud_3d_arr.append([])
        for y in range (0, YMAX):
            __sud_3d_arr[x].append([])
            for z in range (0, ZMAX):
                __sud_3d_arr[x][y].append(0)

    for x in range (0, XMAX):
        for y in range (0, YMAX):
            
            if (__init_sud_arr[x][y] !=0 ):
                __sud_3d_arr[x][y][0] = __init_sud_arr[x][y]
                
                for z in range (1, ZMAX):
                    __sud_3d_arr[x][y][z]=0
            else:
                for z in range (1, ZMAX):
                    __sud_3d_arr[x][y][z]=z
                    
    return (__sud_3d_arr)

def init_stats_arr (__sud_stats_arr):
    
    for x in range (0, XMAX):
        __sud_stats_arr.append([])
        for y in range (0, YMAX):
            __sud_stats_arr[x].append(0)       
            
    return (__sud_stats_arr)


def print_sud (sud_arr):
#     numrows = len(input)    # 3 rows in your example
#     numcols = len(input[0]) # 2 columns in your example

    ROWS=len(sud_arr)
    COLS=len(sud_arr[0])
    
    print("+===+===+===+===+===+===+===+===+===+") 
    for i in range(0, ROWS):
        print("! ",end="")
        for j in range (0, COLS):
            if ((j==2) or (j==5) or (j==8)):
                END=" ! "
            else:
                END=" | "
                
            if (sud_arr[i][j]==0):
                print (" ",end=END)
            else:
                print (sud_arr[i][j],end=END)
                
        print()
        
        if ((i==2) or (i == 5)):
            print("+===+===+===+===+===+===+===+===+===+") 
        else:
            print("+---+---+---+---+---+---+---+---+---+")
            

def print_stats_arr (__sud_stats_arr):
    
    ROWS=len(sud_arr)
    COLS=len(sud_arr[0])
    
    print("+===+===+===+===+===+===+===+===+===+") 
    for i in range(0, ROWS):
        print("! ",end="")
        for j in range (0, COLS):
            if ((j==2) or (j==5) or (j==8)):
                END=" ! "
            else:
                END=" | "
 
 
            print(__sud_stats_arr[i][j],end=END)
            
#             if (sud_arr[i][j]==0):
#                 print (" ",end=END)
#             else:
#                 print (sud_arr[i][j],end=END)
#                 
        print()
        
        if ((i==2) or (i == 5)):
            print("+===+===+===+===+===+===+===+===+===+") 
        else:
            print("+---+---+---+---+---+---+---+---+---+")
    
             
def print_sud_3d_arr (sud_3d_arr):
    
    temp_sud_arr=[[]]
    
    for x in range (0, 9):
        if (x != 0):
            temp_sud_arr.append([])
        for y in range (0, 9):
            temp_sud_arr[x].append(sud_3d_arr[x][y][0])
    
    print_sud(temp_sud_arr)
    

def get_stats (__sud_stats_arr,__sud_3d_arr):
    
    ##__sud_stats_arr is a 2d array
    __n_ele=0
    
    for x in range(0, XMAX):
        for y in range (0, YMAX):
            __opts=0
            if (__sud_3d_arr[x][y][0] != 0 ):
                __sud_stats_arr[x][y]=1
                __n_ele+=1
            else :
                for z in range (1, ZMAX):
                    if ( __sud_3d_arr[x][y][z] != 0):
                        __opts+=1
            __sud_stats_arr[x][y]=__opts

    return (__sud_stats_arr,__n_ele)

def get_x1_x2 (x):
    
    if ((x==0) or (x==1) or (x==2)):
        x1=0
        x2=2
    elif ((x==3) or (x==4) or (x==5)):
        x1=3
        x2=5
    elif ((x==6) or (x==7) or (x==8)):
        x1=6
        x2=8
    else:
        ##not reached
        x1=0
        x2=0
    
    return (x1,x2)


def remove_elements_based_on_solved_cells(__sud_3d_arr):
    
    
    for x in range (0, XMAX):
        for y in range ( 0, YMAX):
            if (__sud_3d_arr[x][y][0] !=0 ):
                ele=__sud_3d_arr[x][y][0]
                ##We will first remove in rows
                for i in range (0, XMAX):
                    __sud_3d_arr[i][y][ele]=0
                
                for j in range (0, YMAX):
                    __sud_3d_arr[x][j][ele]=0
            
                x1,x2=get_x1_x2(x)
                y1,y2=get_x1_x2(y)
                
                for i in range (x1, x2+1):
                    for j in range (y1, y2+1):
                        __sud_3d_arr[i][j][ele]=0
                
    return (__sud_3d_arr)

def place_singletons(__sud_3d_arr,__sud_stats_arr):
    
    n_ele=0
    ele=0
    __sud_stats_arr,n_ele=get_stats(__sud_stats_arr, __sud_3d_arr)
    
    for i in range (0, XMAX):
        for j in range (0, YMAX):
            if (__sud_stats_arr[i][j] == 1 ):
                ##We have a singletopn
                for k in range (1, ZMAX):
                    if (__sud_3d_arr[i][j][k] !=0 ):
                        ele=__sud_3d_arr[i][j][k]
                        
                __sud_3d_arr[i][j][0]=ele
                
                for k in range (1, ZMAX):
                    __sud_3d_arr[i][j][k]=0
                    
    return(__sud_3d_arr)
    

def simple_solution(__sud_3d_arr):
    ###
    
    for x in range (0, XMAX):
        for y in range (0, YMAX):
            if (__sud_3d_arr[x][y][0] == 0 ):
                for z in range (1, ZMAX):
                    if (__sud_3d_arr[x][y][z] != 0 ):
                        
                        __ele=__sud_3d_arr[x][y][z]
                        
                        inc=0
                        ##We will check colum first
                        for i in range (0, XMAX):
                            if ( i != x):
                                if (__sud_3d_arr[i][y][__ele] != 0):
                                    break
                                else:
                                    inc +=1
                        if ( inc == XMAX-1):
                            ##we have a solution!!!!!
                            __sud_3d_arr[x][y][0]=__ele
                            for k in range (1, ZMAX):
                                __sud_3d_arr[x][y][k]=0
                            return (__sud_3d_arr)
                        
                        ##check row
                        
                        inc=0
                        for j in range (0,YMAX):
                            if (j != y):
                                if (__sud_3d_arr[x][j][__ele] != 0 ):
                                    break
                                else:
                                    inc+=1
                                
                        if (inc == YMAX-1):
                            __sud_3d_arr[x][y][0]=__ele
                            
                            for k in range (1, ZMAX):
                                __sud_3d_arr[x][y][k]=0
                            
                            return(__sud_3d_arr)
                        
                        
                        ##check 3x3 cell
                        
                        inc=0
                        brk=0
                        x1,x2=get_x1_x2(x)
                        y1,y2=get_x1_x2(y)
                        
                        for x3 in range (x1, x2+1):
                            if (brk != 1 ):
                                for y3 in range (y1, y2+1):
                                    if ((x3 != x) and (y3 !=y)):
                                        if (__sud_3d_arr[x3][y3][__ele] != 0):
                                            brk=1
                                            break
                                        else:
                                            inc +=1
                                
                        if (inc == XMAX-1):
                            __sud_3d_arr[x][y][0]=__ele
                            
                            for k in range (1, ZMAX):
                                __sud_3d_arr[x][y][k]=0
                            
                            return(__sud_3d_arr)
                            
                                    
    return(__sud_3d_arr)     
                        


def solve_sudoko(__sud_3d_arr,__sud_stats_arr):
    
    old_n_s_ele=0
    n_s_ele=0
    ##Let's get status
    __sud_stats_arr,n_s_ele=get_stats(__sud_stats_arr, __sud_3d_arr)
    print("DEBUG: Initial solved Elements is " + str(n_s_ele))
    #old_n_s_ele=n_s_ele
    
    while (n_s_ele > old_n_s_ele):
        print("\n\n\n##################################")
        print_sud_3d_arr(sud_3d_arr)
        old_n_s_ele=n_s_ele
        __sud_3d_arr=simple_solution(__sud_3d_arr)
        __sud_stats_arr,n_s_ele=get_stats(__sud_stats_arr, __sud_3d_arr)
    
    print("DEBUG: Return Num of solved elements is " + str(n_s_ele))
    print("DEBUG: The retuen STATS matrix\n")
    print_stats_arr(__sud_stats_arr)
    #__sud_3d_arr=place_singletons(__sud_3d_arr, __sud_stats_arr)
    return(__sud_3d_arr)


def recursivesolver(__sud_3d_arr,__sud_stats_arr):
    ##Algorithm
    # 1. find the cell with lowest possibility, assigin a value to it (out of the possibilities)
    # 2. remove all the possbilities from adjecnt cells,
    # 3. check, if there is a singleton's (I.E cells with single soilutions), if so fill it
    # 4. check if there are any conflicts, if so return failure massage 
    # 6. check if the sudoku is solved, if so return the solution, if not continue
    # 7. call teh algo with the updated matrix
    
    #__sud_3d_arr=remove_elements_based_on_solved_cells(__sud_3d_arr)
    
    global it
    
    __sud_stats_arr,n_ele=get_stats(__sud_stats_arr, __sud_3d_arr)
    #__sud_3d_arr=place_singletons(__sud_3d_arr, __sud_stats_arr)
    
    it+=1
    
    print ("\ncurrent iteration is " + str(it) + "\n")
#     print_sud_3d_arr(__sud_3d_arr)
    
    if (n_ele == 81 ):
        ##sudoku is solved
        return(__sud_3d_arr,0)
    
    #Let's find the cell with lowese number of possibilities
    
    min_ele=9
    _xmin=0
    _ymin=0
    
    for i in range (0, XMAX):
        for j in range  (0, YMAX):
            if ( (__sud_stats_arr[i][j] < min_ele) and (__sud_stats_arr[i][j] != 0) ):
                min_ele=__sud_stats_arr[i][j]
                _xmin=i
                _ymin=j
    #print("Xmin is " + str(_xmin) + " and ymin is " + str(_ymin) + "\n")
    ##Let's get options for the _xmin,_ymin cell
    _opts=[]
    
    for i in range (1, ZMAX):
        if (__sud_3d_arr[_xmin][_ymin][i] != 0 ):
            _opts.append(__sud_3d_arr[_xmin][_ymin][i])
    
    #__sud_3d_arr_temp=list(__sud_3d_arr)
    
    for i in range (0, len(_opts)):
        ##we will assign the first option and then back track
        #Let's check if this element can be place here
        
        #__sud_3d_arr_temp=__sud_3d_arr ##creating a copy of the array
        __sud_3d_arr_temp=copy_3d_sud_arr(__sud_3d_arr)
        
        if (check_if_ele_can_place_cell(__sud_3d_arr, _opts[i], _xmin, _ymin) == 0 ):
            __sud_3d_arr_temp[_xmin][_ymin][0]=_opts[i]
            #print ("Setting " + str(_xmin) + ", " + str(_ymin) + " to " + str(_opts[i]) + "the oprions are" + str(_opts) + " \n")
            for k in range (1, ZMAX):
                __sud_3d_arr_temp[_xmin][_ymin][k]=0
            
            __sud_3d_arr_temp=remove_elements_based_on_solved_cells(__sud_3d_arr_temp)
            #
            __sud_3d_arr_temp=simple_solution(__sud_3d_arr_temp)
            #__sud_3d_arr_temp=solve_sudoko(__sud_3d_arr, __sud_stats_arr)
            
            __sud_3d_arr_temp_1,ret=recursivesolver(__sud_3d_arr_temp, __sud_stats_arr)
            
            if (ret != 0 ):
                ##the choice was wrong
                #print("The choice of xmin " + str(_xmin) + ", " + str(_ymin) + " to " + str(_opts[i]) + "was INCORRECT \n")
                pass
            else:
                print("The choice of xmin " + str(_xmin) + ", " + str(_ymin) + " to " + str(_opts[i]) + "was CORRECT \n")
                return(__sud_3d_arr_temp_1,0)
    
    return(__sud_3d_arr,1)
    

def copy_3d_sud_arr(__sud_3d_arr):
    
    #ret_3d_arr=[[[]]]
    ret_3d_arr=[[[]]]
    for i in range (0, XMAX):
        
        ret_3d_arr.append([])
            
        for j in range (0, YMAX):
            
            ret_3d_arr[i].append([])
            
            for k in range (0, ZMAX):
                ret_3d_arr[i][j].append(__sud_3d_arr[i][j][k])
                
    return (ret_3d_arr)
    
def check_if_ele_can_place_cell(__sud_3d_arr,__ele,_x,_y):
    
    #Let's check row's first
    for i in range (0, XMAX):
        if ( i != _x):
                if (__sud_3d_arr[i][_y][0] == __ele):
                    ##There is a conflict.. return 1==false
                    return(1)
    
    #Checking Column
    
    for j in range (0, YMAX):
        if (j != _y ):
            if (__sud_3d_arr[_x][j][0] == __ele):
                ##There is a conflict.. return 1==false
                return(1)
            
    ##Checking Cell
    x1,x2=get_x1_x2(_x)
    y1,y2=get_x1_x2(_y)
    
    for i in range (x1, x2+1):
        for j in range (y1, y2+1):
            if ((i != _x ) and (j != _y)):
                if (__sud_3d_arr[i][j][0] == __ele):
                    return(1)
    
    return(0)

##Initiliaze the sudoku
sud_3d_arr=init_3d_arr(sud_3d_arr,sud_arr)
sud_3d_arr=remove_elements_based_on_solved_cells(sud_3d_arr)

##Initialize the stats array
sud_stats_arr=init_stats_arr(sud_stats_arr)
#n_ele,sud_stats_arr=get_stats(sud_stats_arr, sud_3d_arr)
##Print Initial Sudoku

print("Initial Sudkou\n\n\n\n")
print_sud_3d_arr(sud_3d_arr)


##Print current Stats Array
# print("\n\n\n\ncurrent Stats Array\n")
# print_stats_arr(sud_stats_arr)


#sud_3d_arr=simple_solution(sud_3d_arr)

sud_3d_arr=solve_sudoko(sud_3d_arr,sud_stats_arr)
print("\n\n\n##################################")
print_sud_3d_arr(sud_3d_arr)

print("Recursive solver\n")

sud_3d_arr,ret=recursivesolver(sud_3d_arr, sud_stats_arr)

print("\n\n\n")
print_sud_3d_arr(sud_3d_arr)

