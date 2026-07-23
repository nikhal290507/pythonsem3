"""Simple examples demonstrating measurement scales using pandas and statistics.

This script shows nominal, ordinal, and interval examples.
"""

import statistics
try:
    import pandas as pd
except Exception as e:
    raise SystemExit("pandas is required to run this script. Install with: pip install pandas") from e


def nominal_example():
    fruits = [
        "apple",
        "banana",
        "apple",
        "banana",
        "mango",
        "banana",
        "apple",
        "mango",
        "mango",
        "banana",
        "apple",
        "banana",
        "apple",
        "banana",
        "mango",
        "banana",
        "apple",
        "mango",
        "mango",
        "banana",
        "apple",
        "banana",
        "apple",
        "banana",
    ]
    s = pd.Series(fruits)
    print("Count of each category:")
    print(s.value_counts())
    modes = s.mode()
    if len(modes) > 0:
        print("Most common fruit (mode):", modes.iloc[0])


def ordinal_example():
    # customer satisfaction survey data (ordered categories)
    rating = ["good", "average", "excellent", "good", "excellent", "average", "good"]
    cat_type = pd.CategoricalDtype(categories=["poor", "average", "good", "excellent"], ordered=True)
    s = pd.Series(rating, dtype=cat_type)
    print("Ratings:", list(s))
    print("Is 'good' better than 'average'?", s.iloc[0] > s.iloc[1])
    print("Sorted ratings:", sorted(s))
    # median works for ordered categorical
    try:
        print("Median rating:", s.median())
    except Exception:
        # fallback to manual median
        sorted_vals = s.sort_values()
        print("Median rating:", sorted_vals.iloc[len(sorted_vals) // 2])


def interval_example():
    # temperature data in Celsius
    temperature = [20, 25, 30, 15, 10, 0, -5]
    print("Temperatures (Celsius):", temperature)
    print("Mean temperature:", statistics.mean(temperature))
    print("Difference between 30 C and 20 C:", 30 - 20, "degrees -> meaningful!")
    print("Is 30 C really 'twice as hot' as 15 C? No — Celsius is an interval scale.")


if __name__ == "__main__":
    nominal_example()
    print()
    ordinal_example()
    print()
    interval_example()