import os
import subprocess

# VULNERABILIDAD 1: Contraseña expuesta en el código (Hardcoded Secret)
DB_PASSWORD = "SuperSecretPassword123!"

def ejecutar_comando():
    # El usuario podría ingresar algo como: "archivo.txt; rm -rf /"
    archivo = input("Introduce el nombre del archivo a buscar: ")
    
    # VULNERABILIDAD 2: Uso peligroso de shell=True (Inyección de comandos)
    # Bandit detectará esto inmediatamente como un riesgo alto.
    comando = f"ls -la {archivo}"
    subprocess.call(comando, shell=True)

if __name__ == "__main__":
    ejecutar_comando()
