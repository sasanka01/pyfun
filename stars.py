def draw_stars():
    x = [4, 6, 1, 3, 5, 7, 25]
    for i in x:
        print i*"*"

draw_stars()


def draw_stars1():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    for i in x:
        if isinstance(i,int):
            print i * "*"
        elif isinstance(i,str):
            print i[0][0].lower() * len(i)

draw_stars1()
