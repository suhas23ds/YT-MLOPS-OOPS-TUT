#initiate with the class
class employee:
    #Special method/magic method/dunder method --constructor
    def __init__(self):
        print('Started executing attributes/data')
        self.id=123
        self.salary=50000
        self.designation='Developer'
        print('Finished executing attributes/data')
    
    def travel(self,destination):
        print('This travel function was called manually')
        print(f'employee is travelling to {destination}')
#creating object of the class
sam=employee()
print(sam.id)

sam.travel('New York')
print(type(sam))