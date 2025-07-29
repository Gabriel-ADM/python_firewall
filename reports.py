import json

def gerar_relatorio(ip_dict, filename="relatorio.json"):
    with open(filename, "w") as f:
        json.dump(ip_dict, f, indent=4)
