marks = {"math": 80, "science": 88, "cs": 66, "en": 40}
marks["math"] = 500
del marks["en"]

for mark in marks.values():
    if mark > 50:
        print("all good")
    else:
        print(f"not so great ")

for subject, mark in marks.items():
    if mark < 50:
        print(f"good luck next time at {subject}")


# print (marks.keys())
# =============================================================================
import string

fname = input("Enter file name ")
try:
    myfile = open(fname)
except:
    print("file does not exist")
count = {}
for line in myfile:  # type: ignore
    line = line.rstrip()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1


print(count)
print(max(count.values()))
