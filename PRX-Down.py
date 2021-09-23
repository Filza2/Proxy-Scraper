import requests,time
print("""
╔═╗ ╦═╗ ═╗ ╦  ╔═╗┌─┐┬─┐┌─┐┌─┐┌─┐
╠═╝ ╠╦╝ ╔╩╦╝  ╚═╗│  ├┬┘├─┤├─┘├┤ 
╩   ╩╚═ ╩ ╚═  ╚═╝└─┘┴└─┴ ┴┴  └─┘
<\> @TweakPY
""")
print('____________________')                
p=int(input("Proxy Type\n\n[1]-http   [2]-https\n[3]-socks4 [4]-socks5\n> "))
print('____________________')
if p==1:proxy_type="http"
elif p==2:proxy_type="https"
elif p==3:proxy_type="socks4"
elif p==4:proxy_type="socks5"
ssl=int(input("SSL\n\n[1]-Yes [2]-No [3]-All\n>"))
print('____________________')
if ssl==1:ssl_type="yes"
elif ssl==2:ssl_type="no"
elif ssl==3:ssl_type="all"
time_out=int(input("TimeOut\n\n[50-10000]\n>"))
print('____________________')
print(f"[!] Auto country:[all] Protocol:[{proxy_type}] SSL:[{ssl_type}] Time Out:[{time_out}]")
time.sleep(0.5)
print('____________________')
req=requests.get(f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxy_type}&timeout={time_out}&country=all&ssl={ssl_type}&anonymity=all').text
with open('proxy.txt','w') as Proxy:
	Proxy.write(req)
	print('[+] Done')
	print('[\/] Proxy List Added To File : "proxy.txt"')

