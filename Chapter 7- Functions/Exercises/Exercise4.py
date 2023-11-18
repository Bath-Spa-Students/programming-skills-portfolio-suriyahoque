def make_shirt(size="large", message="I love Python"):
    """Prints a sentence summarizing the size and message of a shirt."""
    print(f"Making a {size}-sized shirt with the message: '{message}'")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a custom-sized shirt with a different message
make_shirt(size="small", message="Programming is fun!")
