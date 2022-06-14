import random
import os

list=['R','Y','B','O','G','W','V','P']
to_find=[]
for i in range(5):
    # create the solution to find
    to_find.append(list[random.randint(0,len(list)-1)])
    
def same_tab(tab1, tab2):
    # compare user input with response array
    for i in tab1:
        if tab1[i]!=tab2[i]:
            return False
    return True

def str_to_arr(string):
    # transform a string into an array
    temp=[]
    for i in range(5):
        temp.append(string[i])
    return temp
        
def tab_num(tab, num):
    # count the number of 'num' in an array
    temp=0
    for i in tab:
        if i==num:
            temp+=1
    return temp

while(same_tab):
    os.system('CLS')
    cpt=0
    print(to_find)
    print('R:red, Y:yellow, B:blue, O:orange, G:green, W:white, V:violet, P:pink')
    response=input('Entrez un suite de 5 couleurs:')
    tab=str_to_arr(response)
    tab_check=[0 for x in range(5)]
    same_color=0
    for i, val in enumerate(tab):
        if to_find[i]==val:
            tab_check[i]=1
        else:
            for j, val in enumerate(to_find):
                if tab_check[j]==1:
                    pass
                else:
                    if tab[i]==val:
                        if tab_check[j]==2:
                            pass
                        else:
                            tab_check[j]=2
                            same_color+=1
                            break
    
    cpt+=1
    print('Bonne couleur:',tab_num(tab_check,2))
    print('Bonne place',tab_num(tab_check,1))
    print("Nombre d'essai:", cpt)
    
    