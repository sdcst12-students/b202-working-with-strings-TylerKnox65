#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"

def createDeck():
  global ranks, suits
  clubs = [(i + "C") for i in ranks]
  diamonds = [(i + "D") for i in ranks]
  hearts = [(i + "H") for i in ranks]
  spades = [(i + "S") for i in ranks]
  all = [clubs, diamonds, hearts, spades]
  all = [i for i in (clubs + diamonds + hearts + spades)]



  return all

def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1


if __name__ == "__main__":
  main()
