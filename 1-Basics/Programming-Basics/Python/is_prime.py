n = int(input("Masukkan angka: "))
if n < 2:
    print("Bukan prima")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Bukan prima")
            break
    else:
        print("Prima")