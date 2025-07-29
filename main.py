from traffic import start_packet_sniffing
from log_handler import monitor_logs
from ai_dectetor_model import train_model, predict_anomaly
from threading import Thread

if __name__ == "__main__":
    # Treina o modelo de detecção
    train_model()
    print("Modelo treinado com sucesso!!")

    # sniffing de pacotes
    Thread(target=start_packet_sniffing, daemon=True).start()
    print("Sniffing iniciado!")

    # monitoramento do access.log
    monitor_logs("access.log")
