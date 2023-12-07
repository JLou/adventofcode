from collections import Counter


with open("./inputs/07", 'r') as f:
    lines = f.read().splitlines()

# lines = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".splitlines()


FIVE_OF_A_KIND = 90_000_000
FOUR_OF_A_KIND = 80_000_000
FULL_HOUSE = 70_000_000
THREE_OF_A_KIND = 60_000_000
TWO_PAIRS = 50_000_000
ONE_PAIR = 40_000_000
HIGH_CARD = 0


def get_card_value(card: str):
    if card.isnumeric():
        return int(card)
    match (card):
        case 'T':
            return 10
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14


def get_card_value_part2(card: str):
    if card.isnumeric():
        return int(card)
    match (card):
        case 'T':
            return 10
        case 'J':
            return 1
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14


class Hand:
    def __init__(self, hand: str, bid: int):
        self.counter = Counter(hand)
        self.hand = hand
        self.bid = bid
        self.value = self.get_value()
        self.second_value = self.get_card_order_value()
        self.value_part2 = self.get_value_part2()
        self.second_value_part2 = self.get_card_order_value_part2()

    def get_value(self):
        counts = self.counter.most_common(5)
        if (counts[0][1] == 5):
            return FIVE_OF_A_KIND
        if (counts[0][1] == 4):
            return FOUR_OF_A_KIND
        if (counts[0][1] == 3 and counts[1][1] == 2):
            return FULL_HOUSE
        if (counts[0][1] == 3):
            return THREE_OF_A_KIND
        if (counts[0][1] == 2 and counts[1][1] == 2):
            return TWO_PAIRS
        if (counts[0][1] == 2):
            return ONE_PAIR
        return HIGH_CARD

    def get_value_part2(self):
        counts = list(
            filter(lambda x: x[0] != 'J', self.counter.most_common(5)))
        jokers = self.hand.count('J')
        if (jokers == 5):
            return FIVE_OF_A_KIND
        if (counts[0][1] + jokers == 5):
            return FIVE_OF_A_KIND
        if (counts[0][1] + jokers == 4):
            return FOUR_OF_A_KIND
        if (counts[0][1] + jokers == 3 and counts[1][1] == 2):
            return FULL_HOUSE
        if (counts[0][1] + jokers == 3):
            return THREE_OF_A_KIND
        if (counts[0][1] == 2 and counts[1][1] == 2):
            return TWO_PAIRS
        if (counts[0][1] + jokers == 2):
            return ONE_PAIR
        return HIGH_CARD

    def get_card_order_value(self):
        total = 0
        for c in self.hand:
            total *= 100
            total += get_card_value(c)
        return total

    def get_card_order_value_part2(self):
        total = 0
        for c in self.hand:
            total *= 100
            total += get_card_value_part2(c)
        return total

    def __repr__(self) -> str:
        return self.hand + " " + str(self.bid)


hands: list[Hand] = []
for hand, bid in [line.split(' ') for line in lines]:
    h = Hand(hand, int(bid))
    hands.append(h)

hands.sort(key=lambda x: (x.value, x.second_value))
print(sum(([(i+1)*h.bid for i, h in enumerate(hands)])))

hands.sort(key=lambda x: (x.value_part2, x.second_value_part2))
# for i in hands:
#     print(i.hand, (i.value, i.second_value))
print(sum(([(i+1)*h.bid for i, h in enumerate(hands)])))
