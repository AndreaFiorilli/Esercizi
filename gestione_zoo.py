#Andrea Fiorilli 
#13/05/2024



class Animal:

    def __init__(self, name:str, species:str, age:int, width:float, height:float, habitat:str) -> None:
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width= width
        self.preferred_habitat=habitat
        self.fence=None
        self.health=round(100*(1/age),3)

    def dim_animal(self) -> float:
        return self.height * self.width


class Fence:

    def __init__(self, area:float, temperature:float, habitat:str) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.animals[Animal]=[]

    def free_area(self) -> float:
        area: float = 0
        for a in self.animals:
            area1=area1+a.dim_animal()
        return self.area-area1

class Zookeeper:

    def __init__(self, name:str, surname:str, id:int) -> None:
        self.name=name
        self.surname=surname
        self.id=id

    def add_animal(animal: Animal, fence: Fence) -> None:
        if animal.dim_animal() > fence.free_area():
            return 0
        else:
            if animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
                animal.fence=fence

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal in fence.animals:
            fence.animals.remove(animal)

    def feed(self, animal: Animal) -> None:
        a: float = (animal.height*0.02) * (animal.width*0.02)
        b: float = animal.height * animal.width
        c: float = b + a
        if animal.fence.free_area()>=c:
            w: float = animal.width * 0.02
            h: float = animal.height * 0.02
            he: float = animal.health * 0.01
            animal.width=animal.width+w
            animal.height=animal.height+h
            animal.health=animal.health+he

    def clean(self, fence: Fence) -> float:
        if fence.free_area() == 0:

            return fence.area
        x = fence.area - fence.free_area()
        return x / fence.free_area()



class Zoo:

    def __init__(self, name: str, address: str) -> None:
        self.name=name
        self.address=address
        self.fences[Fence]=[]
        self.zoo_keepers[Zookeeper]=[]

    def describe_zoo(self) -> None:
        print("Guardians: \n")
        for a in self.zoo_keepers:
            print(f"ZooKeeper(name={a.name}, surname={a.surname}, id={a.id})\n")
        print("Fences: \n")
        for b in self.fences:
            print(f"Fence(area={b.area}, temperature={b.temperature}, habitat={b.habitat})\n")
            print("with animals:\n")
            for c in b.animals:
                print(f"Animal(name={c.name}, species={c.species}, age={c.age})\n")
            print("#" * 30)
            print("")