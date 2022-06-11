import json

books = []
library_contents = []


def open_library():
    global library_contents
    library = open('books_json', 'r')
    library_contents = json.load(library)
    library.close()


def write_to_library():
    global books
    library = open('books_json', 'w')
    json.dump((books + library_contents), library)
    library.close()
    books = []


MENU_PROMPT = '''\nEnter:
'a' to add a book to your library  
'r' to mark a book in your library as read
'd' to delete a book from your library
'q' to quit: '''


def add():

    name = input("Enter the name of the book: ")
    author = input("Enter the author's name: ")

    books.append({
        'name': name,
        'author': author,
        'read': False
    })


def read():
    book_in_library = False

    open_library()

    if not library_contents:
        print("There are no books in your library.")
    else:
        user_input = input("Search for a book name: ")

        for book in library_contents:
            if user_input.lower() == book['name'].lower():
                book_in_library = True

                book_read = input(
                    f"{user_input} is in your library! Have you finished reading {user_input}? Enter y/n: ")

                if book_read != 'y':
                    print("Keep reading!")

                else:
                    book['read'] = True
                break

        if not book_in_library:
            print(f'{user_input} is not in your library')


def delete(name):
    global library_contents
    library_contents = [book for book in library_contents if book['name'].lower() != name.lower()]


selection = input(MENU_PROMPT)
while selection != 'q':

    open_library()

    if selection == "a":
        add()

    elif selection == "r":
        read()

    elif selection == "d":
        delete(input("Enter the name of the book you would like to delete: "))

    else:
        print('Unknown command. Please try again.')

    write_to_library()
    selection = input(MENU_PROMPT)



