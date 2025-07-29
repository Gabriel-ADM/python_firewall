import subprocess

blocked = set()

def block_ip(ip):
    if ip not in blocked:
        print(f"Bloqueando IP: {ip}")
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        ip_lookup = subprocess.run(["nslookup", ip], capture_output=True, text=True)
        print(ip_lookup.stdout)
        blocked.add(ip)
