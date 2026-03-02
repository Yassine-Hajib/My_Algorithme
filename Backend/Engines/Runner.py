import time
from Backend.Engines.Registry import ALGORITHMS


def compare_algorithms(name1, name2, value):
    
    if name1 not in ALGORITHMS or name2 not in ALGORITHMS:
        raise ValueError("One of the algorithms was not found")
    result1 = run_algorithm(name1, value)
    result2 = run_algorithm(name2, value)

    
    time1 = result1["execution_time"]
    time2 = result2["execution_time"]

    
    if time1 < time2:
        winner = name1
    elif time2 < time1:
        winner = name2
    else:
      winner = name2

    time_difference = abs(time1 - time2)
    call_difference = abs(result1["call_count"] - result2["call_count"])
    depth_difference = abs(result1["max_depth"] - result2["max_depth"])

    return {
        "input": value,
        "comparison": {
            name1: result1,
            name2: result2
        },
        "analysis": {
            "winner_by_time": winner,
            "time_difference": time_difference,
            "call_difference": call_difference,
            "depth_difference": depth_difference
        }
    }


def run_algorithm(name, value):
    
    if name not in ALGORITHMS:
        raise ValueError(f"Algorithm '{name}' not found.")

    selected_fct = ALGORITHMS[name]
    start = time.perf_counter()
    output = selected_fct(value)
    end = time.perf_counter()

    execution_time = end - start

    if isinstance(output, tuple) and len(output) == 2:
        result, metrics = output
    else:
        result = output
        metrics = {
            "call_count": 1,
            "max_depth": 1
        }

    return {
        "algorithm": name,
        "input": value,
        "result": result,
        "execution_time": execution_time,
        "call_count": metrics["call_count"],
        "max_depth": metrics["max_depth"]
    }