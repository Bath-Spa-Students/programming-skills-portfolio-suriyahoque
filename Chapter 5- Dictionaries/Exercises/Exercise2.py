# Create a glossary with programming words and their meanings
programming_glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A programming construct that repeats a set of instructions until a certain condition is met.',
    'list': 'An ordered collection of items that can be modified.',
    'conditional': 'A statement that performs different actions depending on whether a condition is true or false.'
}

# Print each word and its meaning with neat formatting
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")