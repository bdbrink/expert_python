class Aggregator:
    def __init__(self) -> None:
        self.all_aggregated = []
        self.las_aggregated = None
        
    def aggregate(self, value):
        self.las_aggregated = value
        self.all_aggregated.append(value)
        
a1 = Aggregator()
a2 = Aggregator()

print(a1.aggregate("a1-1"))
print(a1.aggregate("a1-2"))
print(a2.aggregate("a2-1"))

print(a1.all_aggregated)
print(a2.all_aggregated)