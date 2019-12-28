# Exercise4.6
def computepay(h,r):
    if h > 40:
        a = 40 * r + (h-40) * r * 1.5
    else:
        a = h * r
    return a

hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computepay(float(hrs),float(rate))
print(p)

# Exercise5.2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    if num == "done": 
        break 
    
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
        
    if largest == None:
        largest = num
        
    elif (largest != None) & (num > largest):
        largest = num
    
    if smallest == None:
        smallest = num
        
    elif (smallest != None) & (smallest > num):
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)