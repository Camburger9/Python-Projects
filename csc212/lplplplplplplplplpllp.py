class Atom():
        
    def __init__(self, symbol, atomic, mass, isotope=12):

        self.symbol = symbol
        self.atomic = atomic
        self.mass = mass
        self.isotope = isotope
        
    def neutrons(self):
        number = self.isotope - self.atomic
        print("%s has %d neutrons" % (self.symbol, number))
        return number

    def grams_to_moles(self, grams):
        moles = grams / self.mass
        print("%.1f g is %.1f moles of %s" % (grams, moles, self.symbol))
        return moles
if __name__ == "__main__":
    
        oxygen = Atom()
        oxygen.symbol = 'O'
        oxygen.atomic = 8
        oxygen.mass = 15.999
        oxygen.isotope = 16
        carbon = Atom()
        carbon.symbol = 'C'
        carbon.mass = 12.001
        oxygen.neutrons()
        oxygen.grams_to_moles(24)
        carbon.grams_to_moles(24)
        hydrogen = Atom()
        hydrogen.symbol = 'H'
        hydrogen.atomic = 1
        hydrogen.neutrons = 0
        hydrogen.atomic = 1
        hydrogen.mass = 1
        hydrogen.isotope()
__main__()
                                
