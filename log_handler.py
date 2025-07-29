import time
from collections import defaultdict, deque
from blocker import block_ip
from ai_dectetor_model import predict_anomaly

MAX_REQUESTS_PER_IP = 100
TIME_WINDOW = 10 

ip_logs = defaultdict(lambda: deque())

def monitor_logs(path):
    with open(path, "r") as file:
        file.seek(0, 2)  # Vai para o final

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue

            parts = line.split()
            if len(parts) < 1:
                continue

            ip = parts[0]
            now = time.time()
            ip_logs[ip].append(now)

            # while ip_logs[ip] and now - ip_logs[ip][0] > TIME_WINDOW:
            #     ip_logs[ip].popleft()

            if len(ip_logs[ip]) >= MAX_REQUESTS_PER_IP:
                print(f"[:warning:] Alerta de monitoramento de logs. Ataque de {ip}, será bloqueado. Pois excedeu limite de requests")
                block_ip(ip)

            if len(ip_logs[ip]) >= MAX_REQUESTS_PER_IP:
                if predict_anomaly(len(ip_logs[ip])):
                    print(f"[:warning:] Alerta de modelo! Ataque de {ip} confirmado por ML, o mesmo sera bloqueado.")
                    block_ip(ip)
                else:
                    print(f"[:warning:] Pico de {ip}, que modelo não classificou como ataque.")