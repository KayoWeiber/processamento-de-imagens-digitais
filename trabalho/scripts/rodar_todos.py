from pathlib import Path
import subprocess
import sys


SCRIPTS = [
    "01_bolas_grama/processar_01_bolas_grama.py",
    "02_brinquedo_pelucia/processar_02_brinquedo_pelucia.py",
    "03_cachorro_jardim/processar_03_cachorro_jardim.py",
    "04_praia_cidade/processar_04_praia_cidade.py",
    "05_lago_parque/processar_05_lago_parque.py",
    "06_ferramentas_mesa/processar_06_ferramentas_mesa.py",
    "07_flor_planta/processar_07_flor_planta.py",
    "08_rua_dia/processar_08_rua_dia.py",
    "09_cidade_noite/processar_09_cidade_noite.py",
]


if __name__ == "__main__":
    base = Path(__file__).resolve().parent

    for script in SCRIPTS:
        caminho_script = base / script
        print(f"Executando: {caminho_script}", flush=True)
        subprocess.run([sys.executable, str(caminho_script)], check=True)
