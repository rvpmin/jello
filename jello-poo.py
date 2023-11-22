#!/usr/bin/env python3
#BY rvpmin
#LICENSE GNU/GPL

class Jello:

    def __init__(self,water,flavor,grenetina,sugar,color,slides):
        self.water = water
        self.flavor = flavor
        self.grenetina = grenetina
        self.sugar = sugar
        self.color = color
        self.slides = slides


    def slide(self,flavor):
        if flavor in self.flavor:
            if self.slides > 0:
                self.slides = self.slides - 1
                return True
            else:
                return False

        else:
            return False


jello_lemon = Jello(1.0,'lemon',150.0,100.0,'green',10)
jello_strawberry = Jello(5.0,'strawberry',100.0,70.0,'red',5)
jello_grape = Jello(1.0,'grape',150.0,100.0,'purple',8)


for i in range(12):
    if jello_lemon.slide('lemon'): print('Thank you!!!')
    else: print(':c')
