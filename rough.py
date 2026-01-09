# from opps_project1 import chatbook

# obj=chatbook()

# class rfg:
#     def __init__(self):
#         self.__name='suhas'
#         self.age=32
    
#     def get_name(self):
#         return self.__name
    
#     def set_name(self,value):
#         self.__name=value
# obj=rfg()
# print(obj._rfg__name)

class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f'{self.name} says Woof Woof')

ad=animal('doggo')
ad.speak()