import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]




if __name__ == '__main__':

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value + len(suit_values) + suit_values[card.suit]

    deck = FrenchDeck()
    # print(len(deck))
    #
    # print(Card("Q", "hearts") in deck)
    # print(Card("7", "beasts") in deck)

    suit_values = dict(spdes=3, diamonds=3, clubs=0, hearts=2)
    # print(suit_values)
    for item in deck:
        print(item)

    # for card in sorted(deck, key=spades_high):
    #     print(card)


