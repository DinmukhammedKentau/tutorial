def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage:
input_sentence = "We are ready"
output_sentence = reverse_words(input_sentence)
print(output_sentence)  # Output: "ready are We"
