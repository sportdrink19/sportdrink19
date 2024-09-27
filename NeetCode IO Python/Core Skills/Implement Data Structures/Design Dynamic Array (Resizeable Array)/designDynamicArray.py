class DynamicArray:

    def __init__(self, capacity: int):
        self.dynamicArray = []
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if(self.capacity == self.length):
            self.resize()
        self.dynamicArray.append(n)
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.dynamicArray.pop()
 
    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
    

# Unsure why len() was not working and needed a self managed length variable
# class DynamicArray:

#     dynamicArray = []
#     capacity = 0

#     def __init__(self, capacity: int):
#         if(capacity > 0):
#             self.capacity = capacity

#     def get(self, i: int) -> int:
#         return self.dynamicArray[i]

#     def set(self, i: int, n: int) -> None:
#         self.dynamicArray[i] = n

#     def pushback(self, n: int) -> None:
#         if(self.capacity == len(self.dynamicArray)):
#             self.resize()
            
#         self.dynamicArray.append(n)

#     def popback(self) -> int:
#         return self.dynamicArray.pop()
 
#     def resize(self) -> None:
#         self.capacity *= 2

#     def getSize(self) -> int:
#         return len(self.dynamicArray)
        
#     def getCapacity(self) -> int:
#         return self.capacity