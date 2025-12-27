def add(numbers: str) -> int:
    if numbers == "":
        return 0

    nums = numbers.split(",")
    return sum(int(n) for n in nums)
