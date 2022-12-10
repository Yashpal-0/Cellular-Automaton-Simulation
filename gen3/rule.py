# #to print the array
def print_array():
    for i in range(dimensions[1]):
        for j in range(dimensions[0]):
            print(array[i][j], end="")
        print()


#to change the array elements
def change(i, j):
    if array[i][j] == "O":
        array[i][j] = "X"
    else:
        array[i][j] = "O"

#open file and read the dimensions of array and the number of rules
f = open("config.txt", "r")
dimensions = f.readline().split()
#convert the dimensions to integers
dimensions = [int(i) for i in dimensions]
#initialize the array of size m*n
array = [[ "O" for i in range(dimensions[0])] for j in range(dimensions[1])]
#initialize the rules array
rules = []
#read the rules from the file
for line in f:
    rules.append(line.split())
#convert rules to integers
rules = [[int(i) for i in rule] for rule in rules]
#close the file
f.close()
#change array at the rules
for rule in rules:
    change(dimensions[1]-rule[1], rule[0]-1)
#input the no of interations
iteration = int(input("Enter the no of iterations: "))
if(iteration==-1):
    exit()
#change o to X and X to O
for i in range(iteration):
    for j in range (dimensions[0]):
        for k in range(dimensions[1]):
            change(k,j)

print_array()

#save array elements to file
f = open("output.txt", "w")
for i in range(dimensions[1]):
    for j in range(dimensions[0]):
        f.write(array[i][j])
    f.write("\n")
f.close()