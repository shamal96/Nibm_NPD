import sys

total = 0
count = 0
print("\t\t\t--------BILL---------\n\n")
print('Enter your price list or press "ENTER KEY" to quit\n\n\n')
price= input("Enter your item price : ")

while price:
    count +=1
    no=price
    f=open("bill.txt", 'a+')
    f.write("\n")
    f.write(str(price))
    f.close()
    try:
        no= float(price)
        total += float(price)
        errorflag= False

    except ValueError:
        error = sys.exc_info()[1]
        print ("invalid input")
        print (error)
        errorflag=True

    if  errorflag:
        print("You entered invalid value, Plese try again!")

    price= input("Enter your item price: ")
    
if total>=5000:
    total=total-total*0.15
elif total>=3000:
    total=total-total*0.12
elif total>=1000:
    total=total-total*0.5

f=open("bill.txt", 'a+')
f.write("\n")
f.write(str(price))
f.write("\n")
f.close()

print("Total  is {0}. ".format(total))
