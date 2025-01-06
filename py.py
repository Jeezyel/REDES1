import subprocess as sub
import time

comando = ["python3 python.py"]
comandoLop = ["python3 py.py"]

time.sleep(60)

sub.run(comando , shell=True , capture_output=False , text=True)

time.sleep(3)

sub.run(comandoLop,  shell=True , capture_output=False , text=True)
