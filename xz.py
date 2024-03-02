class Животное:
    def __init__(self, имя):
        self.имя = имя

    def звук(self):
        pass
class Собака(Животное):
    def звук(self):
        return f"{self.имя} лает: Гав-гав!"
class Кошка(Животное):
    def звук(self):
        return f"{self.имя} мурлычет: Мур-мур!"
class СобакоКошка(Собака, Кошка):
    def __init__(self, имя):
     super().__init__(имя)
    def звук(self):
        return f"{self.имя} гавкает и мурлычет: Гав-мур!"
собако_кошка1 = СобакоКошка("Nİxad")
print(собако_кошка1.звук())
