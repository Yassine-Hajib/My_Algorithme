from Backend.Engines.Runner import run_algorithm 
from Backend.Engines.Runner import compare_algorithms

def main():
    print("Sum", run_algorithm("sum", 4))
    print("\n____________________\n")
    print(compare_algorithms("factorial_recursive","factorial_iterative", 5))
    print("\n___________________\n")
    print(run_algorithm("Fibonnaci_Recursive",5))
    print("\n_______________\n")
    print(run_algorithm("Fibonnaci_Iterative",5))

if __name__ == "__main__":
    main()
# It prevents code from executing automatically when imported 