class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn

    def printDetail(self):
        print(f"Name is: {self.name}")
        print(f"USN is {self.usn}")


s1 = Student("Ashank", 123)
s2 = Student("Abhishek", 345)
s1.printDetail()
s2.printDetail()
