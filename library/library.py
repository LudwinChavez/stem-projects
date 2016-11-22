import json


def open_library(filename):
    # Create empty dictionaries just in case the library file is empty
    students = {}
    books = {}

    # Open the library file encoded in JSON and load it into the data object
    # We use the with keyword so we don't have to explicitly close the file
    # later.
    #
    # Alternatively you could use:
    #
    #  f = open(filename)
    #  data = json.load(f)
    #  f.close()
    #
    # and accomplish the same thing.

    with open(filename) as f:
        data = json.load(f)

    # If there are students or books in the library,
    # overwrite the empty dictionaries we created
    if data['students'] != {}:
        students = data['students']

    if data['books'] != {}:
        books = data['books']

    # Return the data we loaded from the file
    return students, books

    # NOTE: The function will return a tuple (students, books)
    # If you want either individually, you can use indexing as shown
    # below in the test section


def add_book(filename, isbn, title, author):
    # Here's a start
    data = open_library(filename)
    books = data[1]

    books[isbn] = {'author': author, 'title': title}  # Now how can we add books to the data?
    # In the space below, write code that adds the key isbn
    # and the value {'title':title, 'author':author}
    # to the books object.
    books
    # Finally, write code that writes the new data to the library
    # Do we need to return anything?
    pass


def remove_book(filename, isbn):
    data = open_library(filename)
    books = data[1]

    # How can we *remove* an item from a dictionary?
    # Write code to delete the book keyed by isbn in the space below

    # Now write code that saves the new version of the data to your library
    pass


def check_out(filename,book, isbn, s_id):
    data = open_library(filename)
    books = data[1]
    student_who_borrowed=s_id

    book="checked out"


    if book is data:
        if book:
            books="checked out"
            print("book has been checked out.")

    else:
        return "book is not found"
        print("book is not found")

    # Find a way to mark a book as checked out. Be sure to associate
    # the book with the student who borrowed it!


    # And again save the data here




def return_book(filename, isbn):
    data = open_library(filename)
    books = data[1]
    #Now ensure that the book is no longer checked out and save the changes
    # to the library.



def status(filename):
    data = open_library(filename)
    books = data[1]
    print(check_out)
    print({data:books})
    # Print out two lists - one of all books currently checked out,
    # and one of all available books.



# Main loop
while True:
    print('=' * 21)
    print('Library System')
    print('=' * 21)
    print('1. Add books to the library')
    print('2. Check out a book')
    print('3. Return a book')
    print('4. View library status')
    print('Q. Quit')
    m = input('Select an option from above or enter Q to quit. ')
    if m.upper() == 'Q':
        break

    # replace 'pass' with appropriate inputs and function calls.
    elif m == '1':
        pass
    elif m == '2':
        pass
    elif m == '3':
        pass
    elif m == '4':
        pass
    else:
        print('Invalid selection.')


