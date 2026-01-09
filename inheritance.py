#simple class

class parent:
    def __init__(self):
        self.name='Suhas'
        self.relaion='Father'

class child(parent):
    # def __init__(self):
    #     self.childname='shaunak'
    pass

d=parent()
c=child()
print(c.name)
