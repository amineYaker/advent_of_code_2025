MAX_NUMBER = 99
MIN_NUMBER = 0
INITIAL_VALUE = 50

result = 0
current_value = INITIAL_VALUE


def read_command(line):
    command = line.strip()
    direction = command[0]
    offset = int(command[1:])
    return direction, offset


def turn(direction, current_value, offset, result):
    start_from_zero = current_value == MIN_NUMBER
    if direction == "R":
        if (offset + current_value) <= MAX_NUMBER:
            current_value += offset
        elif offset > MAX_NUMBER:
            while offset > MAX_NUMBER:
                # Full wrap around
                offset -= MAX_NUMBER + 1
                result += 1

            # we need to re-evaluate the turn with the remaining offset
            current_value, result = turn(direction, current_value, offset, result)
        else:  # offset + current_value > MAX_NUMBER
            current_value += offset - (MAX_NUMBER + 1)
            result += 1
    else:
        if (current_value - offset) > MIN_NUMBER:
            current_value -= offset
        elif (current_value - offset) == MIN_NUMBER:
            current_value = MIN_NUMBER
            result += 1
        elif offset > MAX_NUMBER:
            while offset > MAX_NUMBER:
                # Full wrap around
                offset -= MAX_NUMBER + 1
                result += 1
            # we need to re-evaluate the turn with the remaining offset
            current_value, result = turn(direction, current_value, offset, result)
        else:  # current_value - offset < MIN_NUMBER
            current_value = current_value - offset + (MAX_NUMBER + 1)
            if not start_from_zero:
                result += 1
    return current_value, result


i = 0
with open("../../resources/day1/input.txt", "r") as file:
    for line in file:
        i += 1
        print(f"--- Command {i} ---")
        direction, offset = read_command(line)
        print(f"Direction: {direction}, Offset: {offset}")
        current_value, result = turn(direction, current_value, offset, result)
        print(f"Current value: {current_value}, Result: {result}")

print(f"Final result: {result}")
