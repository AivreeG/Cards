#!/bin/python
import sys

deck_type = sys.argv[-2]
num_shuffle = sys.argv[-1]

#deck_type = 0
#num_shuffle = 8
class Suit():
	def __init__(self, name, color, value):
			self.name = name
			self.color = color
			self.value = value          
	def getName(self):
			return self.name
	def getColor(self):
			return self.color
	def getValue(self):
			return self.value
	def members(self):
			return (self.name, self.color, self.value)

suits = {'s':Suit("Spades", "Black", 1),
				'd':Suit("Diamonds", "Red", 4),
				'c':Suit("Clubs", "Black", 3),
				'h':Suit("Hearts", "Red", 2)}
values = (("Ace",1), ('2',2), ('3',3), ('4',4), ('5',5), 
	('6',6), ('7',7), ('8',8), ('9',9), ('10',10), 
	("Jack",10), ("Queen",10), ("King",10))

class Card:
	STANDARD_BUILD = ('s+', 'h+', 'd-', 'c-')
	
	def __init__(self, suit="None", value=-1):
			self.suit = suit
			self.value = value
	def __str__(self):
			return "The " + self.getValue(0) + " of " + self.getSuit("name")
	def getSuit(self, attr=None):
			if attr:
				return getattr(self.suit, attr)
			else:
				return self.suit.members()
	def getValue(self, attr):
			return self.value[attr]

class Deck():
	def __init__(self, build=0):
				self.cards = []
				self.deck_type = (self.standard_build, self.pinochle_build)
				self.build = build
				self.deck_type[self.build]()
	def standard_build(self):
			print("Building Standard Deck")
			
			king_count = 0
			for s in suits:
				if king_count < 2:
						for v in values:
							if v[0] == "King":
									king_count += 1
							self.cards.append(Card(suits[s], v))
				else:
						for v in values[::-1]:
							self.cards.append(Card(suits[s], v))
	def pinochle_build(self):
			print("Building Pinochle Deck")
			order = Card.STANDARD_BUILD
			for s in order:
				for v in values[-5:] + values[:1]:
						self.cards.append(Card(suits[s], v))
						self.cards.append(Card(suits[s], v))
	def rebuild(self, build=0):
			self.cards = []
			self.build = build
			self.deck_type[build]()
	def shuffle(self, times=1):
			print("Shuffling Deck")
			for t in range(times):
				shuffled = []
				top_half = self.cards[:int(len(self.cards)/2)]
				bottom_half = self.cards[int(len(self.cards)/2):]
				
				top = True
				
				for i in range(len(self.cards)):
						if top:
							shuffled.insert(0, top_half.pop())
							top = not top
						else:
							shuffled.insert(0, bottom_half.pop())
							top = not top
			self.cards = shuffled
	def reorder(self, order=None):
			if not order:
				self.new_deck_order()
				return
			self.cards = []
			for s,d in order:
				self.cards += self.chunk(s,d)
	def chunk(self, suit, direction, start=None, end=None):
			chunk = []
			for v in values[start:end:int(direction+'1')]:
				chunk.append(Card(suits[suit], v))
			return chunk
	def new_deck_order(self):
								self.rebuild()
	def print(self):
			for c in self.cards:
				print(c)



deck = Deck(int(deck_type))
deck.print()
print("\n"*3)
deck.shuffle(int(num_shuffle))
deck.reorder(('c+','c+','c+','c+'))
deck.print()
