import sys
import os
import threading
 
global RemoteDebug
 
def RemoteDebug():
    try:
        #Tenta importar m�dulo presente no diret�rio ra�z da aplica��o.
        import pydevd
        sys.path.append("/home/pi/pydev/pysrc")
        global pydevd
 
        #Configura IP da esta��o remota e a porta de comunica��o.
        pydevd.settrace("192.168.1.107",port=5678,suspend=True)
        
        #Define o ambiente de debug.
        os.environ['TERM']='xterm'
 
        print ("Remote Debug works")
 
    except ImportError:
        #Trata poss�veis exce��es.
        sys.stderr.write("Error:"+" Add pysrc to sys.path.append statement or PYTHONPATH.n")
        sys.exit(1)
