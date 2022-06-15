import random
import os

list=['R','Y','B','O','G','W','V','P']
to_find=[]
for i in range(5):
    # create the solution to find
    to_find.append(list[random.randint(0,len(list)-1)])
    
def str_to_arr(string):
    # transform a string into an array
    temp=[]
    x=len(string)-1
    for i in range(5):
        if i<=x:
            temp.append(string[i])
        else:
            temp.append('-')
    return temp
        
def tab_num(tab, num):
    # count the number of 'num' in an array
    temp=0
    for i in tab:
        if i==num:
            temp+=1
    return temp
cpt=0
tab_check=[]
tab_input=[]
while(tab_num(tab_check,1)<5):
    print('R:red, Y:yellow, B:blue, O:orange, G:green, W:white, V:violet, P:pink')
    response= (input('Entrez un suite de 5 couleurs:')).upper()
    tab_input.append(' | '+' | '.join(str(response[:5])))
    os.system('CLS')
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
    tab_input[cpt]+=(' | => bonne couleur: '+str(tab_num(tab_check,2))+' - bonne place: '+str(tab_num(tab_check,1)))
    cpt+=1
    
    print('Donnée(s) précédente(s):')
    print('-----------------------')
    for i in tab_input:
        print(i)
    print('-----------------------')
    print("Nombre d'essai:", cpt)
print('BRAVO')
    
    