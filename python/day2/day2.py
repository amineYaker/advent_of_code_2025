def read_ranges_from_file(file_path):
    ranges = []
    with open(file_path, "r") as file:
        for line in file:
            for range in line.strip().split(","):
                start, end = map(int, range.strip().split("-"))
                ranges.append((start, end))
    return ranges


def find_invalid_ids(ids_range):
    invalid_ids = []
    start = ids_range[0]
    end = ids_range[1]
    print(f"Finding invalid IDs between {start} and {end}")
    for id in range(start, end + 1):
        if is_invalid_v2(id):
            invalid_ids.append(id)
    return invalid_ids


def is_invalid_v1(id):
    if get_number_digits(id) % 2 == 1:
        return False
    else:
        stringified_id = str(id)
        half_length = len(stringified_id) // 2
        first_half = stringified_id[:half_length]
        second_half = stringified_id[half_length:]
        for i in range(half_length):
            if first_half[i] != second_half[i]:
                return False
        return True


def is_invalid_v2(id):
    for i in range(1, get_number_digits(id) // 2 + 1):
        if i == 1 or get_number_digits(id) % i == 0:
            if not check_validity(i, id):
                return True
    return False


def check_validity(pattern_size, id):
    strigified_id = str(id)
    parts = []

    number_of_parts = len(strigified_id) // pattern_size
    for i in range(number_of_parts):
        part = strigified_id[i * pattern_size : (i + 1) * pattern_size]
        parts.append(part)

    first_part = parts[0]
    for part in parts[1:]:
        if part != first_part:
            return True
    return False


def get_number_digits(id):
    i = 0
    while id > 0:
        id //= 10
        i += 1
    return i


def count_digits_occurences(id):
    digit_count = {}
    while id > 0:
        digit = id % 10
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
        id //= 10
    return digit_count


if __name__ == "__main__":
    ranges = read_ranges_from_file("../../resources/day2/input.txt")

    list_of_invalid_ids = []
    for id_range in ranges:
        invalid_ids = find_invalid_ids(id_range)
        for invalid_id in invalid_ids:
            list_of_invalid_ids.append(invalid_id)

    print(f"Sum invalid IDs: {sum(list_of_invalid_ids)}")
