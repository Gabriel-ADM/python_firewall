from scapy.all import sniff, IP
from collections import defaultdict, deque
import time
from blocker import block_ip
from ai_dectetor_model import predict_anomaly

MAX_PACKAGES_PER_IP = 100
TIME_WINDOW = 10

ip_timestamps = defaultdict(lambda: deque(maxlen=MAX_PACKAGES_PER_IP))

def package_handler(pkg):
    if IP in pkg:
        src_ip = pkg[IP].src
        now = time.time()
        ip_timestamps[src_ip].append(now)

        # Verifica se requisicao esta dentro dos 10 segundos
        while ip_timestamps[src_ip] and now - ip_timestamps[src_ip][0] > TIME_WINDOW:
            ip_timestamps[src_ip].popleft()

        if len(ip_timestamps[src_ip]) >= MAX_PACKAGES_PER_IP:
            print(f"[:warning:] Potencial DDoS de {src_ip}, novas requisições são bloqueadas.")
            block_ip(src_ip)
        if len(ip_timestamps[src_ip]) >= MAX_PACKAGES_PER_IP:
            if predict_anomaly(len(ip_timestamps[src_ip])):
                print(f"[:warning:] Ataque de {src_ip} confirmado por modelo")
                block_ip(src_ip)
            else:
                print(f"[:warning:] Pico de pacotes de {src_ip}, porem modelo nao classificou como ameaca.")


def start_packet_sniffing():
    sniff(prn=package_handler, store=False, filter="ip")