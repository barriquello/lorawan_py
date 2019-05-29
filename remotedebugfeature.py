import sys
import os
import threading
 
global RemoteDebug
 
def RemoteDebug():
    try:
        #Tenta importar módulo presente no diretório raíz da aplicação.
        import pydevd
        sys.path.append("/home/pi/pydev/pysrc")
        global pydevd
 
        #Configura IP da estação remota e a porta de comunicação.
        pydevd.settrace("192.168.1.107",port=5678,suspend=True)
        
        #Define o ambiente de debug.
        os.environ['TERM']='xterm'
 
        print ("Remote Debug works")
 
    except ImportError:
        #Trata possíveis exceções.
        sys.stderr.write("Error:"+" Add pysrc to sys.path.append statement or PYTHONPATH.n")
        sys.exit(1)
