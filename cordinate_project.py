class cord:
    def __init__(self,x,y):
        self.cor_x=x
        self.cord_y=y
    def __str__(self):
        return "<{},{}>".format(self.cor_x,self.cord_y)
    
    def euclidean(self,other):
        return ((self.cor_x-other.cor_x)**2+(self.cord_y-other.cord_y)**2)**0.5


p1=cord(0,0)
p2=cord(10,10)

#print(p1.euclidean(p2))

class person:
    def __init__(self,input_name,input_country):
        self.name=input_name
        self.country=input_country
    
    def great(self):
        if self.country=='India':
            print(f'Namaste {self.name}')
        else:
            print('Welcome {}'.format(self.name))
p=person('Suhas','India')
p.great()
p.gender='Male'
#print(p.gender)



class bal:
    def __init__(self):
        self.__balance=1000

    def get_bal(self):
        return self.__balance

    def set_balance(self,new_val):
        if type(new_val)==int:
            self.__balance=new_val
        else:
            print('Please enter valid amount')

b=bal()
print(b.get_bal())
b.set_balance('heheh')
print(b.get_bal())