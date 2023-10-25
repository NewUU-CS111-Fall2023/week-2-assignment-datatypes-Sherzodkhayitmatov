def string_matching(sentence, word):
  """Returns a boolean value indicating whether the word matches any part of the sentence, and the index of the matching substring if it exists.

  Args:
    sentence: A string.
    word: A string.

  Returns:
    A boolean value indicating whether the word matches any part of the sentence.
    The index of the matching substring if it exists, or -1 otherwise.
  """

  if word in sentence:
    return True, sentence.index(word)
  else:
    return False, -1



sentence = input("Enter a sentence: ")
word = input("Enter a word: ")


match_found, match_index = string_matching(sentence, word)

if match_found:
  print(f"The word '{word}' matches the sentence at index {match_index}.")
else:
  print("No match found.")
