'''
Created on 20 janv. 2018

@author: Lionel
'''

def affich():
    title = 'Days of the Week\n'

    new_path = 'D:/new_days.txt'
    new_days = open(new_path,'w')
    
    new_days.write(title)
    print(title)
    
    new_days.close()