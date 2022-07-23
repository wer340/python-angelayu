# change a bunch of letter
PLAaCE_HOLDER="[name]"
with open("./input/name.txt" ,encoding="utf8") as file:
    names=file.readlines()
    with open("./input/sample.txt", encoding="utf8",mode="r") as letter:
        article = letter.read()
        for name in names:
            name=name.strip()
            result=article.replace(PLAaCE_HOLDER,name)
            with open(f"./output/letter_for_{name}.txt", mode="w",encoding="utf8") as list:
                list.write(result)