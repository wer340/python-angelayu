# change a bunch of letter
PLAaCE_HOLDER="[name]"
with open("./input/name.txt" ,encoding="utf8") as file:
    names=file.readlines()
    with open("./input/sample.docx", encoding="utf8",errors="ignore") as letter:
        article = letter.read()
        for name in names:
            name=name.strip()

            # article.replace(PLAaCE_HOLDER,name)
            print(name)