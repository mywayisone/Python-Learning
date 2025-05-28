# 3. Create a Dictionary of 3 Books
# books = {
#     "001": {"title": "Book One", "author": "Author A"},
#     "002": {"title": "Book Two", "author": "Author B"},
#     ...
# }
# Print all titles

books = {

    "001" : {"title" : "Book One", "author" : "Author A"},
    "002" : {"title" : "Book Two", "author" : "Author B"},
    "003" : {"title" : "Book Three", "author" : "Author C"}
}

for key in books:
    print(books[key]["title"])