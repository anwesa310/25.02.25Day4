def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def menu():
    while True:
        print("\nSelect an operation:")
        print("1. Fibonacci Sequence")
        print("2. Factorial")
        print("3. Prime Check")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            n = int(input("Enter the position for Fibonacci sequence: "))
            print(f"Fibonacci number at position {n}: {fibonacci(n)}")
        elif choice == '2':
            n = int(input("Enter the number for factorial: "))
            print(f"Factorial of {n}: {factorial(n)}")
        elif choice == '3':
            n = int(input("Enter the number to check for prime: "))
            print(f"Is {n} a prime number? {is_prime(n)}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    menu()
