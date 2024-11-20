# Parsing and transforming the given text into a tabular format with columns "Variant", "Expired Date", and "Quantity"

# Input data
input_text = """
°kunyas
Exp 19/11/2024=5
Exp 25/11/2024=11
°mango coco
Exp 19/11/2024=2
°mn
Exp 18/11/2024=2
Exp 20/11/2024=5
°beet
Exp 21/11/2024=2
Exp 23/11/2024=6
°guava
Exp 20/11/2024=4
°jambu
Exp 21/11/2024=1
Exp 23/11/2024=10
°kjn
Exp 19/11/2024=2
Exp 20/11/2024=4
°nan
Exp 23/11/2024=11
°ajw
Exp 23/11/2024=16
°sereh
Exp 20/11/2024=3
°mvn
Exp 21/11/2024=1
Exp 23/11/2024=6
°hijau
Exp 23/11/2024=16
"""

import re
import pandas as pd

# Split input into lines and initialize variables
lines = input_text.strip().split("\n")
data = []
current_variant = ""

# Process each line
for line in lines:
    line = line.strip()
    if re.match(r"^\d{2}/\d{2}/\d{2}\(\d+\)$", line):  # Match date with quantity (e.g., 25/11/24(4))
        date, quantity = re.findall(r"(\d{2}/\d{2}/\d{2})\((\d+)\)", line)[0]
        data.append([current_variant, date, int(quantity)])
    else:
        current_variant = line  # Update current variant

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Variant", "Expired Date", "Quantity"])
df
