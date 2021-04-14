from random import randint

class Soodur():
    tervis = 100

    def voitlus(self, vaenlane):
        while vaenlane.tervis > 0 and self.tervis > 0:
            rundaja = randint(1, 2)
            if rundaja == 1:
                print("Esimene sõdur lõi")
                vaenlane.tervis -= 20
                print("Teisel sõduril on alles", vaenlane.tervis, "elu")
                if vaenlane.tervis == 0:
                    print("Esimene sõdur Võitis!!!")
            elif rundaja == 2:
                print("Teine sõdur lõi")
                self.tervis -= 20
                print("Esimesel sõduril on alles", self.tervis, "elu")
                if self.tervis == 0:
                    print("Teine sõdur Võitis!!!")