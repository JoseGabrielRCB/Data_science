class humano :
    def __init__(self,count = 0):
        self.count = count
    def __repr__(self):
        return f"CountingCliker(count={self.count})"


Cobia1 = humano(12)
print(Cobia1)