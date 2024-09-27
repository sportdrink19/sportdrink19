class DynamicArray:

    def __init__(self, capacity: int):
        self.dynamicArray = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if(self.capacity == len(self.dynamicArray)):
            self.resize()
        self.dynamicArray.append(n)

    def popback(self) -> int:
        return self.dynamicArray.pop()
 
    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.dynamicArray)
        
    def getCapacity(self) -> int:
        return self.capacity
    

array = DynamicArray(4)
print(array)
array.pushback(1)
print(array)
array.set(0, 0)
array.pushback(2)
print(array)
print(array.get(0), array.get(1))
print(array.getCapacity())
array.popback()
print(array)