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