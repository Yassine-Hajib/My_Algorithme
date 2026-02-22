import time
from Backend.Engines.Registry import ALGORITHMS

def compare_algorithms(name1, name2, value) :
    if name1 not in ALGORITHMS or name2  not in ALGORITHMS :
        raise ValueError( "One Of The Algorithme not found")
    
    resultat_1=run_algorithm(name1,value)
    resultat_2=run_algorithm(name2,value)

    return {
        "input": value,
        "comparison": {
        name1: resultat_1,
        name2: resultat_2 
            }
            }


def run_algorithm(name, value):

    if name not in ALGORITHMS:
        raise ValueError(f"Algorithm '{name}' not found.")

    selected_fct = ALGORITHMS[name]
    
    start = time.perf_counter()

    output = selected_fct(value)

    if isinstance(output, tuple) and len(output) == 2:
        result, metrics = output
    else:
        result = output
        metrics = {
            "call_count": 1,
            "max_depth": 1
        }

    end = time.perf_counter()
    execution_time = end - start

    return {
        "algorithm": name,
        "input": value,
        "result": result,
        "execution_time": execution_time,
        "call_count": metrics["call_count"],
        "max_depth": metrics["max_depth"]
    }