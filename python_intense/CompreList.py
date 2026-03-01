pairs = [(x,y) for x in range(10) for y in range(5)]
print (pairs)
print()
increasing_pairs = [(x,y) for x in range (10) for y in range(x+1,10)]
print(increasing_pairs)