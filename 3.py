c = {}

with open("en-ru.txt","r") as f:
    for l in f:
        en_words = l.split("-")[0].strip()
        ru_words = l.split("-")[1].strip().split(',')
        for i in ru_words:
            i = i.strip()
            if i in c.keys():
                c[i] = c[i] + ", " + en_words
            else:
                c[i] = en_words

with open("ru-en.txt", "w") as f:
    for i in sorted(c.keys()):
        f.writelines(i,"-" ,c[i] , "\n")