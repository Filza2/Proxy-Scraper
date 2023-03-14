from requests import get
from rich.console import Console
from time import sleep
import re,os

#We recommend using a VPN if you are in the Middle East

console=Console();count=list();count2=list()
headers={'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 12; ANN-AN00 Build/HONORANN-AN00'}

def header():
    os.system("cls" if os.name=='nt' else "clear");console.print("""
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                     
                                By @TweakPY - @vv1ck
""",style='bold dark_magenta',justify='left')


def Total():
    header()
    for i in count:
        url=str(i).split("|")[0]
        protcol=str(i).split("|")[1]
        counter=str(i).split("|")[2]
        console.print(f'[+] We Got [ {counter} ] - [ {protcol} ]  From  [ {url.replace("https://","").replace("http://","")} ] ')
    console.print(f'\n[+] We Got in Total [ {len(count2)} ] Proxies ');console.print('\n');exit()
    
def Proxies_Saver(proxys,url,protocol):
    try:
        total=0
        for proxys in re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}\b",str(proxys)):
            with open(f'{protocol}_Proxies.txt','a') as p:
                p.write(str(proxys+'\n'))
                count2.append(proxys)
                total+=1
        count.append(f"{url}|{protocol}|{total}")
        console.print(f'[+] Download From [ {url} ] Done [bold green]successfully[/bold green]')
    except Exception as e:console.print(f"[-] Download From [ {url} ] [bold red]Failed[/bold red]")
    

def https_proxies():
    urls=[
        'https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://alexa.lr2b.com/proxylist.txt',
        'http://olaf4snow.com/public/proxy.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt', 
        'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
        'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
        'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
        'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt']
    for url in urls:
        try:
            r=get(url,headers=headers).text
            Proxies_Saver(r,url,'https')
        except Exception as e:console.print(f"[-] Download From [ {url} ] [bold red]Failed[/bold red]")

def http_proxies():
    urls=[
        'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
        'https://www.proxy-list.download/api/v1/get?type=http',
        'https://api.openproxylist.xyz/http.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
        'https://raw.githubusercontent.com/almroot/proxylist/master/list.txt',
        'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt',
        'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
        'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt',
        'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt',
        'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
        'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt',
        'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',]
    for url in urls:
        try:
            r=get(url,headers=headers).text
            Proxies_Saver(r,url,'http')
        except Exception as e:console.print(f"[-] Download From [ {url} ] [bold red]Failed[/bold red]")

def socks4_proxies():
    urls=[
        'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all',
        'https://api.openproxylist.xyz/socks4.txt',
        'https://www.proxy-list.download/api/v1/get?type=socks4',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt',
        'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
        'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt',
        'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks4.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt']
    for url in urls:
        try:
            r=get(url,headers=headers).text
            Proxies_Saver(r,url,'socks4')
        except Exception as e:console.print(f"[-] Download From [ {url} ] [bold red]Failed[/bold red]")

def socks5_proxies():
    urls=[
        'https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all',
        'https://www.proxy-list.download/api/v1/get?type=socks5',
        'https://api.openproxylist.xyz/socks5.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
        'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
        'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
        'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
        'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt',
        'https://raw.githubusercontent.com/hyperbeats/proxy-list/main/socks5.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
        'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt',
        'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks5.txt',
        'https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt',
        'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
        'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt']
    for url in urls:
        try:
            r=get(url,headers=headers).text
            Proxies_Saver(r,url,'socks5')
        except Exception as e:console.print(f"[-] Download From [ {url} ] [bold red]Failed[/bold red]")
        
        
def Proxy_Scraper_Core():
    header()
    https_proxies()
    http_proxies()
    socks4_proxies()
    socks5_proxies()
    sleep(1.9)
    Total()
    
    
    
    
    
    
Proxy_Scraper_Core()
