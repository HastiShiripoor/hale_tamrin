library = {}


def add_subject(subject):
    library[subject] = Book


def add_book(book):
    Book.append(book)


def search_book(subject):
    if subject in library:
        print(library[subject])


def search(subject, book):
    a = library[subject]
    for i in a:
        if book in i:
            return True
        else:
            return False


start = input("for start enter Yes(Y) for end enter No(N)")

while start == "Y":
    x = int(input("1.for add subject\n" + "2.find books \n" + "3.find book with subject\n"))

    if x == 1:
        subject = input("enter subj: ")

        if subject in library:
            a = input("do you want to add book? Yes(Y), No(N)")
            while a == "Y":
                add_book(book=input("enter book? "))
                a = input("do you want to add book? Yes(Y), No(N)")

        elif subject not in library:
            Book = []
            add_subject(subject)
            a = input("do you want to add book? Yes(Y), No(N)")
            while a == "Y":
                add_book(book=input("enter book? "))
                a = input("do you want to add book? Yes(Y), No(N)")
        print(library)

    elif x == 2:
        search_book(subject=input("enter your subject: "))

    elif x == 3:
        subject = input("enter your subject: ")
        book = input("enter the name of book: ")
        search(subject, book)

        if search(subject, book) == True:
            print("This book", "(", book, ")", "was found.")

        else:
            print("No book was found with this subject.")

        start = input("for start enter Yes(Y) for end enter No(N)")
