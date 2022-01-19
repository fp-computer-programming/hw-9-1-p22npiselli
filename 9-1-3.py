# Nolan Piselli

def find_thing(search,look):
    found = -1
    for i, v in enumerate(search):
        if v == look[0]:
            num = 1
            check = ''
            for x in range(len(search)):
                check += search[num]
                num += 1

            return i