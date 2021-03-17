print("   ***** HCF and LCM calculator *****")
print("")
num1, num2 = [int(num1) for num1 in input("Enter any two number of your choices : ").split()]
print("")
#HCF
hcf=1
loop=0
n=2
if num1 < num2:
   loop=num1//2
   loop=loop+1
else:
    loop=num2//2
    loop=loop+1
   


while n != loop:
      if ((num1 % n == 0) and (num2 % n == 0)):
            hcf = n
            n = n + 1
      else:
             n = n + 1 

#LCM
lcm= (num1 * num2)/hcf

print("What you want to calculate..?")
print("1. Calculate HCF ")
print("2. Calculate LCM ")
print("3. Calculate Both HCF and LCM")
print("")
choice= int(input("Enter your Choice : "))
print("")
if choice==1:
    print("HCF of ",num1," and ",num2," = ",hcf)  #hcf print
    print("")
elif choice==2:
     print("LCM of ",num1," and ",num2," = ",lcm)  #lcm print
     print("")
elif choice==3:
    print("HCF of ",num1," and ",num2," = ",hcf)  #hcf print
    print("LCM of ",num1," and ",num2," = ",lcm)  #lcm print
    print("")
else:
    print("Opss! you entered wrong choice..!!")
    print("")




