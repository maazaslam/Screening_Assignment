from sklearn import mixture


class Carnivore:
    species1 = ['Lion', 'Tiger', 'Human', 'Cheetah']
    def animals(self):
        print(Carnivore.species)

class Herbivore:
    species2 = ['Cow', 'Sheep', 'Human', 'Deer']
    def species(self):
        print(Herbivore.species)

class Omnivore(Herbivore, Carnivore):
    mixed_species = []
    def printSpecies(self):
        for species in Herbivore.species2:
            if species in Carnivore.species1:
                self.mixed_species.append(species)

        print("Animals that eat both plants and animals are: ", self.mixed_species)


omni = Omnivore()
omni.printSpecies()
