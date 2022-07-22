with open(r"C:\Users\home\Desktop\rt.txt") as file:
    book = file.read()

print(book)
with open(
        "C:/Users/home/Desktop/er.txt") as file:  # default use / forward slash  what is windows os or what this mac os
    book = file.read()

print(
    book)  # https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
