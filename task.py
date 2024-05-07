class Chess:
    def __init__(self, name):
        self.name = name
    
    def price(self):
        pass

    def move(self):
        pass

class Piyada(Chess):
    def price(self):
        return f"{self.name} 1 xal"

    def move(self):
        return f"{self.name} 1 və ya 2 xana irəli hərəkət edir"

class At(Chess):
    def price(self):
        return f"{self.name} 3 xaldir"

    def move(self):
        return f"{self.name} L herfi səklində hərəkət edir"
    
class Fil(Chess):
    def price(self):
        return f"{self.name} 3 xaldir"

    def move(self):
        return f"{self.name} Çarpaz hərəkət edir"
    
class Top(Chess):
    def price(self):
        return f"{self.name} 5 xaldir"

    def move(self):
        return f"{self.name} Şaquli hərəkət edir"

class Vəzir(Chess):
    def price(self):
        return f"{self.name} 9 xal"

    def move(self):
        return f"{self.name} İstədiyi kimi hərəkət edir"
    
class Şah(Chess):
    def price(self):
        return f"{self.name}ın Xalı yoxdur"
    
    def move(self):
        return f"{self.name} 1 xana olmaqla istədiyi kimi hərəkət edir"



if __name__ == "__main__":
    Piyada_chess = Piyada("Piyada")
    At_chess = At("At")
    Fil_chess = Fil("At")
    Top_chess = Top("Top")
    Vəzir_chess = Vəzir("Vəzir")
    Şah_chess=Şah("Şah")

    print(Piyada_chess.price())
    print(Piyada_chess.move()) 

    print(At_chess.price())  
    print(At_chess.move())   

    print(Fil_chess.price())  
    print(Fil_chess.move())

    print(Top_chess.price())  
    print(Top_chess.move())    

    print(Vəzir_chess.price())  
    print(Vəzir_chess.move())

    print(Şah_chess.price())
    print(Şah_chess.move())