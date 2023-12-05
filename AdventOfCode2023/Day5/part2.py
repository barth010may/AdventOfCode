# DAY 5: https://adventofcode.com/2023/day/5
import re

puzzle_input = open('input.txt').read().splitlines()

example_input = open('example.txt').read().splitlines()

# Parse the seeds into pairs of tuples
intermediate_seeds = re.findall("[\d]+ [\d]+", puzzle_input[0])
seeds = []
for seed in intermediate_seeds:
    seeds.append(tuple(seed.split(" ")))

def get_tuple(example_input, i):
    x_to_y = []
    for j in range(i + 1, len(example_input)):
        if example_input[j] == '':
            break
        x_tuple = example_input[j].split(' ')
        x_to_y.append(tuple(x_tuple))
    return x_to_y

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
for i in range(2, len(puzzle_input)):
    if puzzle_input[i] == 'seed-to-soil map:':
        seed_to_soil = get_tuple(puzzle_input, i)
    elif puzzle_input[i] == 'soil-to-fertilizer map:':
        soil_to_fertilizer = get_tuple(puzzle_input, i)
    elif puzzle_input[i] == 'fertilizer-to-water map:':
        fertilizer_to_water = get_tuple(puzzle_input, i)
    elif puzzle_input[i] == 'water-to-light map:':
        water_to_light = get_tuple(puzzle_input, i)
    elif puzzle_input[i] == 'light-to-temperature map:':
        light_to_temperature = get_tuple(puzzle_input, i)
    elif puzzle_input[i] == 'temperature-to-humidity map:':
        temperature_to_humidity = get_tuple(puzzle_input, i)
    elif puzzle_input[i] == 'humidity-to-location map:':
        humidity_to_location = get_tuple(puzzle_input, i)

# tuple = (destination range start, source range start, range length)
# Find the lowest 'location' value out of the given 'seeds'

def get_destination(map, source):
    destination = None
    for tuple in map:
        # potential issue: range ends with goes from i to j-1, which could cut of the last number in a range
        r = range(int(tuple[1]), int(tuple[1]) + int(tuple[2]))
        if source in r:
            dif = source - int(tuple[1])
            destination = int(tuple[0]) + dif
    destination = source if destination is None else destination
    #print(destination)
    return destination

# Just give this shit some large number xD
lowest_location = 100000000000

# Run through each seed and find its location and compare it with the current lowest
# So this is bruteforcy as fuck, and will literally takes Ages to computer
for seed in seeds:
    r = range(int(seed[0]), int(seed[0]) + int(seed[1]))
    for seed_copy in r:
        print(f"seed = {seed_copy}")
        seed_copy = int(seed_copy)
        soil = get_destination(seed_to_soil, seed_copy)
        fertilizer = get_destination(soil_to_fertilizer, soil)
        water = get_destination(fertilizer_to_water, fertilizer)
        light = get_destination(water_to_light, water)
        temperature = get_destination(light_to_temperature, light)
        humidity = get_destination(temperature_to_humidity, temperature)
        location = get_destination(humidity_to_location, humidity)
        print(f"location = {location}")
        lowest_location = location if location < lowest_location else lowest_location

print(f"Lowest location = {lowest_location}")


# Solution for Day 5 part 2, copied from https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py
# Unfortunately i couldn't find a better method than brute forcing the whole thing, which takes fucking years to compute :(
'''
inputs, *blocks = open("input.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])
'''
