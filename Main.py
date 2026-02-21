from Backend.Engines.Runner import run_algorithm

def main():
    print("Sum", run_algorithm("sum", 4))
    print("\n_________\n")
    print("Factorial Recursive:", run_algorithm("factorial_recursive", 5))
    print("\n_________\n")
    print("Factorial Iterative:", run_algorithm("factorial_iterative", 5))


if __name__ == "__main__":
    main()
# It prevents code from executing automatically when imported.