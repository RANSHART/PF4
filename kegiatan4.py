import math

def translasi(tx, ty):
    def transformasi_translasi(x, y):
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return transformasi_translasi

def dilatasi(sx, sy):
    def transformasi_dilatasi(x, y):
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return transformasi_dilatasi

def rotasi(sudut):
    def transformasi_rotasi(x, y):
        sudut_rad = math.radians(sudut)
        new_x = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
        new_y = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
        return new_x, new_y
    return transformasi_rotasi

# Contoh penggunaan
titik = (3, 5)

# Translasi
translasi_func = translasi(2, -1)
titik_translasi = translasi_func(*titik)
print("Koordinat setelah translasi:", titik_translasi)

# Dilatasi
dilatasi_func = dilatasi(2, -1)
titik_dilatasi = dilatasi_func(*titik)
print("Koordinat setelah dilatasi:", titik_dilatasi)

# Rotasi
rotasi_func = rotasi(30)
titik_rotasi = rotasi_func(*titik)
print("Koordinat setelah rotasi:", titik_rotasi)
