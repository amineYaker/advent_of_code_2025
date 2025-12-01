MAX_NUMBER = 99
MIN_NUMBER = 0
INITIAL_VALUE = 50

result = 0
current_value = INITIAL_VALUE

with open("../resources/day1/input.txt", "r") as file:
    for line in file:
        command = line.strip()
        direction = command[0]
        offset = int(command[1:])
        if direction == "R":
            current_value += offset % (MAX_NUMBER + 1)
            current_value = current_value % (MAX_NUMBER + 1)
            if current_value == MIN_NUMBER:
                result += 1
        else:
            current_value -= offset
            while current_value < MIN_NUMBER:
                current_value += MAX_NUMBER + 1
            if current_value == MIN_NUMBER:
                result += 1

print(f"Final result: {result}")
