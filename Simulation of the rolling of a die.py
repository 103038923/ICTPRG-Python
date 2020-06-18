# Simulation code
sum = []
i = 1
min_number = 1
max_number = 6
ht = int(input("How many times do you want to roll the dice :"))
while i <= ht :
    import random
    num = int(random.randint(min_number,max_number))
    print("Rolling the dice")
    print("The number randomly generated is :",num)
    sel = str(input("Indicate whether you want this to be counted (y or n) "))
    if sel == 'y' :
        sum.append(num)
        print("the number",num,"is selected")
    i += 1
print("The sum of all number is",ht)
if sum == [] :
    print("None of the numbers were selected.")
else:
    print("The numbers selected are",sum)
