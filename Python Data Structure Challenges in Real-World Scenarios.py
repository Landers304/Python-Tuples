#Task 1:


def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    else:
        print("This book already exists in the library.")

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Test function
add_book(library, "To Kill a Mockingbird", "Harper Lee")
add_book(library, "1984", "George Orwell")  # Attempt to add duplicate book
add_book(library, "The Great Gatsby", "F. Scott Fitzgerald")

# Updated library
print("\nUpdated Library:")
for idx, book in enumerate(library, start=1):
    print(f"{idx}. {book[0]} by {book[1]}")
