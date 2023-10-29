
with open(r"day-26 list compre\f1.txt") as f:
    f1_data = f.readlines()
    
with open(r"day-26 list compre\f2.txt") as f:
    f2_data = f.readlines()
    
# print(f1_data, f2_data)
result = [int(num) for num in f1_data if num in f2_data]

print(result)