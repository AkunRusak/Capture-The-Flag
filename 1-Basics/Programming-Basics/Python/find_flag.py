with open('file.txt', 'r') as f:
    for line in f:
        if "flag" in line.lower():
            print("Flag ditemukan:", line.strip())