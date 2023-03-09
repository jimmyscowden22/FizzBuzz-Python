#FizzBuzz Program to count from 1-100
#Replaces numbers divisible by 3 with "Fizz"
#Replaces numbers divisible by 5 with "Buzz"
#Replaces numbers divisble by 3 & 5 with "FizzBuzz"
#Prints all other numbers in range

#function to count from 1-100 and replace numbers with appropriate words
def fizzbuzz():
    #This will count from 1-100
    count = range(1,101)
    #Loop through the numbers
    for number in count:
        #if divisble by 3 and 5, print "FizzBuzz"
        if number%3==0 and number%5==0:
            print("FizzBuzz")
            continue
        #if divisible by 3, print "Fizz"
        if number%3==0:
            print("Fizz")
            continue
        #if divisible by 5, print "Buzz"
        if number%5==0:
            print("Buzz")
            continue
        #if not divisible by 3 or 5, print the number
        else:
            print(number)
            
#Don't forget to define main
def main():
    fizzbuzz()

#if __name__ == __main__, execute main()
if __name__ == "__main__":
    main()