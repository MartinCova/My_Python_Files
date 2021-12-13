
class Cmystere1():
    def __init__(self,p1,p2):
        self.att1 = p1
        self.att2 = p2
    def __str__(self):
        return("je veux des points")

    def anonyme1(self):
        self.att1 += 10 - self.att2
        return self.att1

    def anonyme2(self):
        print(self.att1,"/",self.att2)


class Cmystere2():
    def __init__(self):
        self.lst1 = []
        self.att1 = 0
    def anonyme1(self, DS1):
        if isinstance(DS1, Cmystere1):
            self.lst1.append(DS1)
    def anonyme2(self):
        for v in self.lst1:
            v.anonyme1()
        for v in self.lst1:
            print(v)
            v.anonyme2()


t1 = Cmystere1(10,20)
t2 = Cmystere1(10,20)
t1.anonyme1()
t1.anonyme1()
t3 = Cmystere2()
t3.anonyme1(t2)
t3.anonyme1(t1)

