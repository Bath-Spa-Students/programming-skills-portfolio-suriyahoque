# Create a glossary with programming words and their meanings
programming_glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A programming construct that repeats a set of instructions until a certain condition is met.',
    'list': 'An ordered collection of items that can be modified.',
    'conditional': 'A statement that performs different actions depending on whether a condition is true or false.'
}

# Add five more Python terms to the glossary
programming_glossary['dictionary'] = 'A collection of key-value pairs.'
programming_glossary['module'] = 'A file containing Python definitions and statements.'
programming_glossary['class'] = 'A blueprint for creating objects in Python.'
programming_glossary['exception'] = 'An event that occurs during the execution of a program and disrupts the normal flow.'
programming_glossary['method'] = 'A function that belongs to an object.'

# Loop through the dictionary's keys and values to print them
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")