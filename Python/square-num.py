def square_number(n: int) -> int:
    """Return the square of the given number."""
    return n ** 2

if __name__ == "__main__":
    try:
        x = int(input("Enter a number: "))
        result = square_number(x)
        print(f"The square of {x} is: {result}")
    except ValueError:
        print("❌ Please enter a valid integer.")
