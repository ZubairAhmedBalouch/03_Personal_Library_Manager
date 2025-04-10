import json # Importing the JSON module for saving and loading data
import os # Importing the OS module for file operations

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []


library = []

#step 1: Show library menu

def show_menu():
    print("\n Welcome to your Personal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")


# Step 2: Add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }
    
    library.append(book)
    print(f"Book '{title}' successfully added to your library.✅")

#step 3: remove book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' successfully removed from your library.✅")
            return
    print(f"Book '{title}' not found in your library.❌")


# Step 4: Search for a book
def search_book():
    print("Search by: ")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice (1 or 2): ")

    keyword = input("Enter the title or author to search: ").lower()
    found_books = []

    for book in library:
        if choice == "1" and keyword in book["title"].lower():
            found_books.append(book)
        elif choice == "2" and keyword in book["author"].lower():
            found_books.append(book)

    if found_books:
        print("📚 Matching Books:")
        for book in found_books:
            status = "Read" if book["read"] else "Unread"
            print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')
    else:
        print("⚠️ No matching books found.")

#step 5: Display all books
def display_books():
    if not library:
        print("Your library is empty. 📚")
    else:
        print("📚 Your Library:")
        for book in library:
            status = "Read" if book.get("read", False) else "Unread"
            print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')

#step 6: Display statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book.get("read", False))
    unread_books = total_books - read_books

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")
    
 #step 7: Main program loop       
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        with open(data_file, 'w') as file:
            json.dump(library, file)
        print("Library data saved. Goodbye! 👋")
        break
    else:
        print("⚠️Invalid choice. Please try again.")

    