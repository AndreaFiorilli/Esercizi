class Animal:

    def __init__(self, name:str, species:str, age:int, width:float, height:float, habitat:str) -> None:
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=habitat
        self.health:float=round(100 * (1 / age))
        self.fence=Fence

    def area_a(self, feed = False) -> float:
        if feed:
            x = (self.height*0.02) * (self.width*0.02)
            y = self.height * self.width
            x = y - x
            return x
        return self.height * self.width


class Fence:

    def __init__(self, temperature, area, habitat) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []

    def free_area(self) -> float:
        area = 0
        for x in self.animals:
            area += x.area_a()
        return self.area - area

class Zookeeper:

    def __init__(self, name, surname, id) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: int = id

    def add_animal(animal: Animal, fence: Fence) -> None:
        if animal.area_a() > fence.free_area():
            print("NOT ENOUGHT SPACE IN THIS FENCE")   #gestire eccezione
            return 0
        else:
            if animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
                print("Animale aggiunto")
            else:
                print("Habitat non compatibile con l'animale")

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal in fence.animals:
            fence.animals.remove(animal)
        else:
            print("ANIMAL NOT IN THIS FENCE")

    def feed(self, animal: Animal, fence: Fence) -> None:
        if fence.free_area() >= animal.area_a(feed=True):
            x = animal.width * 0.02
            y = animal.height * 0.02
            z = animal.health * 0.01
            animal.width += x
            animal.height += y
            animal.health += z
        else:
            print("NOT ENOUGHT SPACE TO FEED THE ANIMAL")

    def clean(self, fence: Fence) -> float:
        if fence.free_area() == 0:
            return fence.area
        x = fence.area - fence.free_area()
        return x / fence.free_area()



class Zoo:

    def __init__(self, name: str, address: str) -> None:
        self.name: str = name
        self.address: str = address
        self.fences: list[Fence] = []
        self.zoo_keepers: list[Zookeeper] = []

    def describe_zoo(self) -> None:
        print("Guardians: \n")
        for x in self.zoo_keepers:
            print(f"Name: {x.name}\tSurname: {x.surname}\t ID: {x.id}")
        print("\n Fences \n")
        for x in self.fences:
            print(f"Fence: \n\thabitat: {x.habitat}\n\ttemperature: {x.temperature}\n\tarea: {x.area}\n with this animals:")
            for y in x.animals:
                print(f"{y.name}\t{y.species}\t{y.age}")
            print("#" * 30)


lion = Animal("Leo", "Lion", 5, 2.5, 1.5, "savannah")
tiger = Animal("Tigger", "Tiger", 4, 2.2, 1.4, "jungle")
elephant = Animal("Dumbo", "Elephant", 10, 3.5, 2.5, "savannah")

savannah_fence = Fence(25, 13, "savannah")
jungle_fence = Fence(30, 50, "jungle")

zookeeper = Zookeeper("John", "Doe", 123)

Zookeeper.add_animal(lion, savannah_fence)
Zookeeper.add_animal(tiger, savannah_fence)
Zookeeper.add_animal(elephant, savannah_fence)

zoo = Zoo("My Zoo", "123 Main Street")
zoo.fences.append(savannah_fence)
zoo.fences.append(jungle_fence)
zoo.zoo_keepers.append(zookeeper)
print(zoo.zoo_keepers[0].clean(zoo.fences[0]))
zoo.describe_zoo()
zoo.zoo_keepers[0].remove_animal(zoo.fences[0].animals[0], zoo.fences[1])
zoo.zoo_keepers[0].remove_animal(zoo.fences[0].animals[0], zoo.fences[0])
zoo.describe_zoo()