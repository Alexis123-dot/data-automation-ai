


def print_twice(blue):
    print(blue)
    print(blue)


s = "+"
y = "-"
def print_grid(s, y):
    print((s + y *4)*2+s)
    appear = ( ("|" + " " * 4)*2 + "|")
    print (appear)
    print(appear)
    print(appear)
    print (appear)
    print((s + y *4)*2+s)
    appear = ( ("|" + " " * 4)*2 + "|")
    print (appear)
    print(appear)
    print(appear)
    print (appear)
    print((s + y *4)*2+s)

    
print_grid(s, y)
