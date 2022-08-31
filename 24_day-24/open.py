file = open("scarlett.txt",encoding="utf8")
shows_txt = file.read()
print(shows_txt)
file.close()

with open("Jennifer_Lawrence.txt",mode="w") as book:
    book.write(""
               "Jennifer Lawrence born on August 15, 1990,\n in Indian Hills, Kentucky, United States, is an American film"
               "\n actress who primarily works in Hollywood films.")
