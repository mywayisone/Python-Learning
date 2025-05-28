# 4. Loop Through a Dictionary
# Print all key-value pairs from any dictionary

books = {

    "001" : {"title" : "Book One", "author" : "Author A"},
    "002" : {"title" : "Book Two", "author" : "Author B"},
    "003" : {"title" : "Book Three", "author" : "Author C"}
}

for key, pair in books.items():
    print(f"{key} => {pair}")