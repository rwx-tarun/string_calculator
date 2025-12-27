delimiters= ["\n",";","//"]

def add(numbers: str) -> int:
    # for empty string 
    if numbers == "":
        return 0
    # replace all delimiters from ","
    numbers = cleaned_data(numbers)
    # get the integer numbers list
    numbers = parse_numbers(numbers)
    # check negatives here 
    has_negatives = check_negatives(numbers)
    if has_negatives:
        raise ValueError(f"negative numbers not allowed")

    return sum(numbers)

def cleaned_data(numbers):
    # replace all delimeter with ","
    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ",")
    return numbers

def parse_numbers(numbers: str) -> list[int]:
    result = []

    for part in numbers.split(","):
        part = part.strip()
        if part == "":
            continue

        try:
            result.append(int(part))
        except ValueError:
            raise ValueError(f"Invalid number: {part}")

    return result


def check_negatives(numbers):
    for num in numbers:
        if int(num) < 0:
            return True
    return False
