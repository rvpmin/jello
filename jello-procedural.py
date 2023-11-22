#!/usr/bin/env python3
#BY rvpmin
#LICENSE GNU/GPL

#variables globales
size_lemon = 10
size_strawberry = 5 


def slide(flavor):
    global size_lemon
    global size_strawberry
    
    if 'lemon' in flavor:
        if size_lemon > 0:
            size_lemon = size_lemon - 1
            return True
        else:
            return False

        
    elif 'strawberry' in flavor:
        if size_strawberry > 0:
            size_strawberry = size_strawberry - 1
            return True
        else:
            return False

    
lemon_water = 1.0 #Lt
lemon_flavor = 'lemon'
lemon_grenetina = 15.0 #gr
lemon_sugar = 100.0 #gr
lemon_color = 'green'

strawberry_water = 1.0 #Lt
strawberry_flavor = 'lemon'
strawberry_grenetina = 15.0 #gr
strawberry_sugar = 100.0 #gr
strawberry_color = 'red'

for i in range(12):
    if slide('strawberry'):
        print(i,'Thank you!!!')
    else:
        print(i,':(')
