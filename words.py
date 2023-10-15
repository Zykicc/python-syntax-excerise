def print_upper_words(words):
  """ Print each word in the list uppercase"""

  for word in words:
    print(word.upper())



def print_upper_words2(words):
  """ Print only words that start with the letter 'e' or 'E' in it uppercased"""

  for word in words:
    if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, starting_letter):
  """ Prints each word uppercased if it starts with the letter given"""

  for word in words:
     for letter in starting_letter:
        if word.startswith(letter):
           print(word.upper())
                

