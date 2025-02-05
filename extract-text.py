import re

def extract_to_values(file_path, output_path):
    # Regular expression to match the pattern TO-xxx (where xxx is digits)
    pattern = r"TO-\d+"
    
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Find all matches of the pattern
    matches = re.findall(pattern, content)
    
    # Write the matches to the output file
    with open(output_path, 'w') as output_file:
        for match in matches:
            output_file.write(match + '\n')

# Example usage
input_file = 'DIS-text.txt'  # Replace with your input file path
output_file = 'DIS-output.txt'    # Replace with your desired output file path
extract_to_values(input_file, output_file)

print(f"Extracted TO-xxx values have been written to {output_file}")
