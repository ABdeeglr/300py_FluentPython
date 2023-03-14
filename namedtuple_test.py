from collections import namedtuple

Book = namedtuple("Book", "name ISBN price pages author")

this = Book("JoJa", "29993919129293", 12.99, 507, "me")
print(this)
