# DAY 7: https://adventofcode.com/2023/day/7
import functools

puzzle_input = open("input.txt").read().splitlines()
example_input = open("example.txt").read().splitlines()

ranks = {"Five_of_a_kind": 7, "Four_of_a_kind": 6, "Full_house": 5, "Three_of_a_kind": 4, "Two_Pair": 3, "Pair": 2, "High Card": 1}
card_ranks = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}

def full_house(cards):
    two_card = False
    three_card = False
    for card in cards:
        if cards.count(card) == 2:
            two_card = True
        elif cards.count(card) == 3:
            three_card = True
    if two_card and three_card:
        return True
    else:
        return False


def x_pair(cards, x):
    counter = 0
    list = []
    for card in cards:
        if cards.count(card) < 2 or card in list:
            continue
        else:
            counter += 1
            list.append(card)

    if counter == x:
        return True
    else:
        return False


def x_of_a_kind(cards, x):
    for card in cards:
        if cards.count(card) == x:
            return True
    return False


def get_rank(cards):
    if x_of_a_kind(cards, 5):
        return ranks["Five_of_a_kind"]
    elif x_of_a_kind(cards, 4):
        return ranks["Four_of_a_kind"]
    elif full_house(cards):
        return ranks["Full_house"]
    elif x_of_a_kind(cards, 3):
        return ranks["Three_of_a_kind"]
    elif x_pair(cards, 2):
        return ranks["Two_Pair"]
    elif x_pair(cards, 1):
        return ranks["Pair"]
    else:
        return ranks["High Card"]


def compare(x, y):

    cards_x = x.split(" ")[0]
    cards_y = y.split(" ")[0]

    x_rank = get_rank(cards_x)
    y_rank = get_rank(cards_y)

    if x_rank > y_rank:
        return 1
    elif x_rank == y_rank:
        for card_x, card_y in zip(cards_x, cards_y):
            if card_ranks[card_x] > card_ranks[card_y]:
                return 1
            elif card_ranks[card_y] > card_ranks[card_x]:
                return -1
    else:
        return -1


ranked = sorted(puzzle_input, key=functools.cmp_to_key(compare))
print(ranked)

sum = 0
for i in range(len(ranked)):
    bid = ranked[i].split(" ")
    sum += (int(bid[1]) * (i + 1))

print(f"Total sum = {sum}")
