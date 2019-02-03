# find all numbers divisible by 7 but not a multiple of 5 between 1 and 3000
empty_list = []

# iterate through range of numbers
for i in range(1994,3001):
    if(i % 7 == 0) and (i % 5 != 0):
        empty_list.append(str(i))
    
print(",".join(empty_list))