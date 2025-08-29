class Mom:
    def cook(self):
        print("Indian")

class Daughter(Mom):
    def cook(self):
        print("Chinese")

m = Mom()
d = Daughter()

m.cook()
d.cook()