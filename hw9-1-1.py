# Nolan Piselli

from http.client import CONTINUE


def only_list(lst):
    for i, v in enumerate(lst):
        if i % 2 == 0:
            print(v)

print(only_list(['a', 'b', 'c', 'd', 'e']))