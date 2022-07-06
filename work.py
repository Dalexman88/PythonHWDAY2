#Question 1.
num = 0
cubed = 1
while cubed < 999:
    num += 1
    cubed = num ** 3
    print("number: ", num, "cubed: ", cubed)

    #Question2
num = 2
prime = [2, ]
for num in range(2, 100):
    for i in range(2, num - 1):
        if num % i == 0:
            num += 1
        else:
            prime.append(num)
            break
print(prime)  

#Question3
age = int(input("How old are you? " ))

if age < 18:
    print("you are a kid")
elif 18 < age < 65: 
    print("you are an adult")
else:
    print("you are a senior citizen")

    #question4 
    #"""I will need more time on this one"""