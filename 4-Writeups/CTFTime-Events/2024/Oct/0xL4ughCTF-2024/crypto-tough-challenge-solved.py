from Crypto.Util.number import long_to_bytes

n = 173847382938479238472938472394823
e = 65537
c = 132847123847123847123847128371283

# Misalnya diberikan faktor p dan q
p = 13123123123123123123
q = n // p
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)
m = pow(c, d, n)

print("Flag:", long_to_bytes(m).decode())