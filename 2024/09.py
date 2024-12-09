def part2(input, disk_size):
    is_file = True
    files = []
    file_index = 0
    result = 0
    empty_spaces = [True] * disk_size
    cursor = 0

    for char in input:
        if is_file:
            files.append((file_index, cursor, int(char)))
            file_index += 1
            is_file = False
            for j in range(int(char)):
                empty_spaces[cursor+j] = False
        else:
            is_file = True
        cursor += int(char)

    for i in range(len(files) - 1, 0, -1):
        file_index, start, size = files[i]
        j = empty_spaces.index(True)
        while j <= start-size:
            if all(empty_spaces[j:j+size]):
                files[i] = (file_index, j, size)
                for k in range(size):
                    empty_spaces[j+k] = False
                break
            j += 1

    for file_index, start, size in files:
        for i in range(size):
            result += file_index * (start + i)
    return result


def solve(input):
    is_file = True
    disk = []
    file_index = 0
    s = 0

    for char in input:
        if is_file:
            disk = disk + [file_index] * int(char)
            file_index += 1
            is_file = False
        else:
            disk = disk + ["."] * int(char)
            is_file = True

    left, right = 0, len(disk) - 1
    while left < right:
        if disk[left] == ".":
            while disk[right] == ".":
                right -= 1
            if left >= right:
                break
            disk[left] = disk[right]
            disk[right] = "."
            right -= 1
        left += 1

    for i, char in enumerate(disk):
        if char == ".":
            break
        s += i * int(char)

    return s, part2(input, len(disk))


test_input = """2333133121414131402"""

assert solve(test_input) == (1928, 2858)


with open("./inputs/09", 'r') as f:
    lines = f.read()

part1, part2 = solve(lines)
print(f'Part 1: {part1}, Part 2: {part2}')
