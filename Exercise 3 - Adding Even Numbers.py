#Write your code below this row 👇

total = 0
for even_number in range(2, 101, 2):
    #print(even_number)
    total += even_number # it is going to be += NOT '=+'  
print(total) # indentation matters here 

# OR Can you do it this way [either one gives same OUTPUT]

total1 = 0 
for even_number in range(1,101):
    if even_number % 2 == 0:
        total1 +=even_number
print(total1)
