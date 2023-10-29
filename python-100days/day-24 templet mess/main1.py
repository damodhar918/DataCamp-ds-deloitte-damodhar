# file = open(r'day-24\file.txt', 'r')
# content = file.read()
# file.close()
# print(content)

#TODO: write file

with open(r'day-24\file.txt', 'w') as file:
    file.write("Hello World\n")

# TODO: append file
with open(r'day-24\file.txt', 'a') as file:
    file.write("Hello World!")


# TODO: read file
with open(r'day-24\file.txt', 'r') as file:
    content = file.read()
    
    
print(content)
