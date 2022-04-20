a = int(input("Enter a number : "))
def prime(a):
    for i in range (2,a) :
        if a % i == 0 :
            return "This is not prime number"
    return "Prime number"
print(prime(a))
