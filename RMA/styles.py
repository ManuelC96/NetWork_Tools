# create tuple freom txt
with open("rma.txt", "r") as f:
    text = f.read()
    split = text.split("\n")
    print(split)
    tupleList = list(split)
    for i in tupleList:
        tp = tuple(i)
        print(tp)
