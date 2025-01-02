import re
import os
import platform
import socket
import subprocess
from datetime import datetime

import distro
import psutil
from screeninfo import get_monitors
from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

def get_uptime():
    boot_time = psutil.boot_time()
    now = datetime.now().timestamp()

    uptime_seconds = int(now - boot_time)
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
    return uptime_str

def get_shell():
    shell = os.environ.get('SHELL')
    return os.path.basename(shell) if shell else 'N/A'

def get_de():
    de = os.environ.get('DESKTOP_SESSION') or os.environ.get('XDG_CURRENT_DESKTOP')
    return de if de else 'N/A'

def get_resolution():
    try:
        monitors = get_monitors()
        resolutions = [f"{m.width}x{m.height}" for m in monitors]
        return ','.join(resolutions)
    except Exception:
        return 'N/A'

def get_packages():
    try:
        result = subprocess.run(['dpgk', '--get-selections'], stdout=subprocess.PIPE, text=True)
        if result.returncode == 0:
            packages = len([line for line in result.stdout.split('\n') if line])
            return str(packages)
    except Exception:
        return 'N/A'
    
def get_os():
    return distro.name(pretty=True)

def get_cpu():
    cpu = platform.processor()
    return cpu if cpu else 'N/A'

def get_ram():
    return f"{round(psutil.virtual_memory().total / (1024 ** 3))}G"

def get_gpu():
    try:
        result = subprocess.run(['lspci'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        gpu_lines = re.findall(r'(VGA compatible controller|3D controller): (.+)', result.stdout, re.IGNORECASE)

        gpu_names = [gpu[1] for gpu in gpu_lines]

        return ','.join(gpu_names) if gpu_names else 'N/A'
    except Exception:
        return 'N/A'
    
def get_host():
    return socket.gethostname()

def get_kernel():
    return platform.release()