def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # Menghitung gradien (m)
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Menghitung konstanta (c)
    c = p1[1] - m * p1[0]

    return f"y = {m:.2f}x + {c:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 3), point(5, 9)))
