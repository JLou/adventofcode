from collections import defaultdict, deque
import queue
import re

with open("./inputs/05", 'r') as f:
    lines = f.read().split('\n\n')

# lines = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".split('\n\n')


def constant_factory(value):
    return lambda: value


def parse(block: str):
    return [list(map(int, l.split(" "))) for l in block.splitlines()[1:]]


def get_mapping(mapping: list[list[int]], key: int):
    for destination_start, source_start, length in mapping:
        if key >= source_start and key <= source_start + length:
            return destination_start + (key - source_start)
    return key


seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

seeds = list(map(int, re.findall(r'\d+', lines[0])))

maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
        light_to_temperature, temperature_to_humidity, humidity_to_location]

for curr_map, data in zip(maps, lines[1:]):
    curr_map += parse(data)


res = float('inf')


# for seed in seeds:
#     location = get_mapping(humidity_to_location, get_mapping(temperature_to_humidity, get_mapping(light_to_temperature, get_mapping(
#         water_to_light, get_mapping(fertilizer_to_water, get_mapping(soil_to_fertilizer, get_mapping(seed_to_soil, seed)))))))
#     res = min(location, res)

# print(res)

def get_seed_ranges(seeds):
    return [[s, s+range] for s, range in zip(seeds[::2], seeds[1::2])]


def get_mapping2(source_start, destination_start, source):
    return destination_start + (source - source_start)


def get_range_mapping(ranges, mapping):
    new_ranges = []
    for s, e in ranges:
        current_ranges = deque()
        current_ranges.append([s, e])
        while len(current_ranges) > 0:
            start, end = current_ranges.popleft()
            has_changed = False
            for destination_start, source_start, length in mapping:
                source_end = source_start + length
                if start < source_start and end > source_end:
                    new_ranges.append([
                        get_mapping2(
                            source_start, destination_start, source_start),
                        get_mapping2(source_start, destination_start, source_end)])
                    current_ranges.append([start, source_start - 1])
                    current_ranges.append([source_end + 1, end])
                    has_changed = True
                elif start >= source_start and end <= source_end:
                    new_ranges.append([
                        get_mapping2(source_start, destination_start, start),
                        get_mapping2(source_start, destination_start, end)])
                    has_changed = True
                elif source_start >= start and source_start < end:
                    new_ranges.append([
                        get_mapping2(
                            source_start, destination_start, source_start),
                        get_mapping2(source_start, destination_start, min(end, source_end))])
                    current_ranges.append([start, source_start - 1])
                    has_changed = True
                elif start >= source_start and start < source_end:
                    new_ranges.append([
                        get_mapping2(source_start, destination_start, start),
                        get_mapping2(source_start, destination_start, min(end, source_end))])
                    current_ranges.append([source_end + 1, end])
                    has_changed = True

                if has_changed:
                    break
            if not has_changed:
                new_ranges.append([start, end])
    return new_ranges


ranges = get_seed_ranges(seeds)
for mapping in maps:
    ranges = get_range_mapping(ranges, mapping)

print(min([start for start, end in ranges]))


# new_ranges = []
# for s, range in zip(seeds[::2], seeds[1::2]):
#     e = s + range
#     current_ranges = deque()
#     current_ranges.append([s, e])
#     while len(current_ranges) > 0:
#         start, end = current_ranges.popleft()
#         has_changed = False
#         for destination_start, source_start, length in seed_to_soil:
#             source_end = source_start + length
#             if start < source_start and end > source_end:
#                 new_ranges.append([get_mapping(seed_to_soil, source_start), get_mapping(
#                     seed_to_soil, source_end)])
#                 current_ranges.append([start, source_start - 1])
#                 current_ranges.append([source_end + 1, end])
#                 has_changed = True
#             elif start >= source_start and end <= source_end:
#                 new_ranges.append([get_mapping(seed_to_soil, start), get_mapping(
#                     seed_to_soil, end)])
#                 has_changed = True
#             elif source_start >= start and source_start < end:
#                 new_ranges.append([get_mapping(seed_to_soil, source_start), get_mapping(
#                     seed_to_soil, min(end, source_end))])
#                 current_ranges.append([start, source_start - 1])
#                 has_changed = True
#             elif start >= source_start and start < source_end:
#                 new_ranges.append([get_mapping(seed_to_soil, start), get_mapping(
#                     seed_to_soil, min(end, source_end))])
#                 current_ranges.append([source_end + 1, end])
#                 has_changed = True

#             if has_changed:
#                 break
#         if not has_changed:
#             new_ranges.append([start, end])
