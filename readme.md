# Detector Básico de Ataques DDoS com Bloqueio Automático

Este projeto monitora tráfego de rede em tempo real, identifica potenciais ataques DDoS baseados em picos de requisições por IP e bloqueia IPs suspeitos automaticamente.

## Funcionalidades

- Armazena timestamps de requisições por IP e detecta picos acima de um limite configurável
- Usa um modelo simples de Machine Learning (IsolationForest via scikit-learn) para validar anomalias
- Bloqueia IPs suspeitos automaticamente usando iptables no Linux (com sudo)
- Suporte para simulação e logs em arquivos
- Fácil adaptação para Windows (alterando a função de bloqueio)

## Pacotes Python:

- scapy
- scikit-learn
- pandas

## Linux com iptables instalado e sudo configurado (para bloqueio automático)

## Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
