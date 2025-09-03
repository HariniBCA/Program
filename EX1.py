def reverse_string(text):
    return text[::-1]
def count_words(text):
    words = text.split()
    return len(words)
print("Flow control,Functions and string manipulation:")
input_text = input("Enter a sentence:")
if  input_text.startswith ("Hello!"):
    print("Greeting: Hello!")
elif input_text.startswith ("Good bye!"):
    print("Parting: Good bye!")
else:
    print("Custom message:",input_text)
    reverse_text = reverse_string(input_text)
    print("Reversed text:",reverse_text)
    word_count = count_words(input_text)
    print("word_count:",word_count)
