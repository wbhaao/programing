import numpy

print("hello world")
word_lists = [
    ["수학", "좋다"],
    ["수학", "AI", "어렵다", "재밌다"],
    ["AI", "노잼", "어려움"],
]
list2 = {string: i for i, string in [0, list(set(sum(word_lists, [])))]}
print(list2)
