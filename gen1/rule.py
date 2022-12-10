#to print the array
def print_array():
    for i in range(dimensions[1]):
        for j in range(dimensions[0]):
            print(array[i][j], end="")
        print()


#to change the array elements
def change(i, j):
    if array[i][j] == "O":
        array[i][j] = "X"

#open file and read the dimensions of array
f = open("config.txt", "r")
dimensions = f.readline().split()
#convert the dimensions to integers
dimensions = [int(i) for i in dimensions]
#initialize the array of size m*n
array = [[ "O" for i in range(dimensions[0])] for j in range(dimensions[1])]
rules = []
for line in f:
    rules.append(line.split())
#convert rules to integers
rules = [[int(i) for i in rule] for rule in rules]
f.close()
for rule in rules:
    change(dimensions[1]-rule[1], rule[0]-1)
#input the no of interations
iteration = int(input("Enter the no of iterations: "))
if(iteration==-1):
    exit()
#find "X" and change it's right neighbout to "X" for each iteration
for i in range(iteration):
    for rule in rules:
        change(dimensions[1]-rule[1], rule[0]+i)
        
print_array()

#save array elements to file
f = open("output.txt", "w")
for i in range(dimensions[1]):
    for j in range(dimensions[0]):
        f.write(array[i][j])
    f.write("\n")
f.close()
