import re
import subprocess,os

class Run(object):
    def statusip(*args):
        for ip in args:
            ping =subprocess.Popen(
                ["ping ",str(ip)],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE)
            out,error = ping.communicate()
            online= re.search(r"Respuesta desde %s: bytes=\d\d\ tiempo=\d\d\w\w\ TTL=\d\d"%ip,str(out))
            destInaccesible= re.search(r"Host de destino \w\w\w\w\w\w\w\w\w\w\w\w",str(out))
            agotado=re.search(r"Tiempo de espera agotado para esta \w\w\w\w\w\w\w\w\w",str(out))

            if online:
                print ("STATUS %s ==> ONLINE\n"%ip,online.group())     
            elif destInaccesible:
                print ("STATUS %s==> destInaccesible "%ip,destInaccesible.group())     
            elif agotado:
                print ("STATUS %s==> Host OFFLINE\n"%ip,agotado.group())

ip = '192.168.1.1'
ip2='192.168.1.2'
t=Run()
t.statusip(ip,ip2)
