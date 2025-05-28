# 5. Use get() to Access a Key That Might Not Exist

books = {

    "001" : {"title" : "Book One", "author" : "Author A"},
    "002" : {"title" : "Book Two", "author" : "Author B"},
    "003" : {"title" : "Book Three", "author" : "Author C"}
}

print(books.get("004","Not Found"))