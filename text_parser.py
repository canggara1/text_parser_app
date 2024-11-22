import re
import pandas as pd

def parse_text(input_text):
    # Split input into lines and initialize variables
    lines = input_text.strip().split("\n")
    data = []
    current_variant = ""

    # Process each line
    for line in lines:
        line = line.strip()
        # Match date with quantity (dd/mm/yyyy and quantity in parentheses)
        match = re.match(r"(\d{2}/\d{2}/\d{4})\((\d+)\)", line)
        if match:
            expired_date = match.group(1)  # Extract the expiration date
            quantity = int(match.group(2))  # Extract the quantity
            data.append([current_variant, expired_date, quantity])
        else:
            current_variant = line  # Update current variant

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["Variant", "Expired Date", "Quantity"])
    return df

if __name__ == "__main__":
    # Example input
    input_text = """
    jambu
    11/11/2024(5) 
    12/11/2024(9) 
    naga
    11/11/2024(3) 
    12/11/2024(6) 
    beet
    12/11/2024(6) 
    15/11/2024(10) 
    kristal
    10/11/2024(9) 
    14/11/2024(2) 
    mangga
    12/11/2024(4) 
    15/11/2024(14) 
    hijau
    11/11/2024(8) 
    12/11/2024(6) 
    15/11/2024(10) 
    ajw
    12/11/2024(2) 
    15/11/2024(15) 
    kunyah
    17/11/2024(11) 
    sereh
    15/11/2024(1)
    """
    # Parse the text
    df = parse_text(input_text)

    # Print the parsed DataFrame
    print("Parsed Data:")
    print(df)
