import pyautogui
import time

print("Você tem 5 segundos para posicionar o mouse no local desejado...")
time.sleep(5)

# Captura a posição atual do mouse
x, y = pyautogui.position()
print(f"Posição capturada: ({x}, {y})")

# Salva a posição em um arquivo para usar depois
with open('posicao.txt', 'w') as f:
    f.write(f"{x},{y}")

import pyautogui
import time
from datetime import datetime

# Lê a posição salva no arquivo
with open('posicao.txt', 'r') as f:
    pos = f.read().split(',')
    x = int(pos[0])
    y = int(pos[1])

# Define o horário do clique
hora_do_clique = "14:30"  # Exemplo: 14:30

# Função para verificar se é hora de clicar
def verificar_hora(horario):
    agora = datetime.now().strftime("%H:%M")
    return agora == horario

# Loop para verificar a hora continuamente
while True:
    if verificar_hora(hora_do_clique):
        print(f"Clicando na posição ({x}, {y})")
        pyautogui.click(x, y)
        break
    time.sleep(1)  # Espera 1 segundo antes de verificar novamente
