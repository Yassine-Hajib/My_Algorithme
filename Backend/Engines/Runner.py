import time
from Backend.Engines.Registry import ALGORITHMS

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