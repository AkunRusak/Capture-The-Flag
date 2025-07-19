import base64
code = "ZmxhZ3t..."
while True:
    try:
        code = base64.b64decode(code).decode()
    except:
        break
print(code)
