Detector Básico de Ataques DDoS com Bloqueio Automático
Este projeto monitora tráfego de rede em tempo real, identifica potenciais ataques DDoS baseados em picos de requisições por IP e bloqueia IPs suspeitos automaticamente.

Funcionalidades
Armazena timestamps de requisições por IP e detecta picos acima de um limite configurável

Usa um modelo simples de Machine Learning (IsolationForest via scikit-learn) para validar anomalias

Bloqueia IPs suspeitos automaticamente usando iptables no Linux (com sudo)

Suporte para simulação e logs em arquivos

Fácil adaptação para Windows (alterando a função de bloqueio)

Pacotes Python:

scapy

scikit-learn

pandas

Linux com iptables instalado e sudo configurado (para bloqueio automático)

Crie e ative um ambiente virtual:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/macOS
Instale as dependências:

bash
Copy
Edit
pip install -r requirements.txt

Como usar
Execute o script principal:

bash
Copy
Edit
sudo python main.py
Sudo é necessário para que o Scapy capture pacotes e para aplicar regras no firewall.

Estrutura do projeto
main.py: ponto de entrada do programa

traffic.py: captura e análise de pacotes em tempo real

blocker.py: função para bloquear IPs via firewall (iptables no Linux)

ai_dectetor_model.py: modelo de machine learning para detecção de anomalias

log_handler.py: leitura e monitoramento de logs (ex: access.log)

requirements.txt: lista de dependências

Personalização
Ajuste o número máximo de pacotes e janela de tempo em traffic.py:

python
Copy
Edit
MAX_PACKAGES_PER_IP = 100
TIME_WINDOW = 10  # segundos# python_firewall
