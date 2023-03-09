def fizzbuzz():
    x = range(1,101)
    for i in x:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
            continue
        if i%3==0:
            print("Fizz")
            continue
        if i%5==0:
            print("Buzz")
            continue
        else:
            print(i)

def main():
    fizzbuzz()

if __name__ == "__main__":
    main()