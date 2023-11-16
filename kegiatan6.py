def point(x, y):
    return x, y

def line_equation_of(p1, M):
    # Inner function untuk menghitung nilai C
    def calculate_C(p, m):
        x1, y1 = p
        return y1 - m * x1

    C = calculate_C(p1, M)

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (6, -2) dan bergradien -2:")
print(line_equation_of(point(6, -2), -2))
