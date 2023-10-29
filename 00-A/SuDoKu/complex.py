class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

 	def str(self):
 		return self.r + " + "+self.i+"i"


class Calculator:
    current = 0

    def add(self, amount):
        self.r = self.r + amount.r
        self.i = self.i + amount.i

    def get_current(self):
        return self.current


#print("justin")
comp = Complex()
comp.create(3,4)
#print(comp.str())