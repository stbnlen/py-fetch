from functions import (
    get_os,
    get_host,
    get_kernel,
    get_uptime,
    get_packages,
    get_shell,
    get_resolution,
    get_de,
    get_cpu,
    get_gpu,
    get_ram,
)
from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align


if __name__ == "__main__":
    console = Console()

    os_info = get_os()
    host = get_host()
    kernel = get_kernel()
    uptime = get_uptime()
    packages = get_packages()
    shell = get_shell()
    resolution = get_resolution()
    de = get_de()
    cpu = get_cpu()
    gpu = get_gpu()
    memory = get_ram()

    table = Table(show_header=False, box=None, padding=(0, 1))

    label_color = "bold cyan"
    value_color = "white"

    table.add_row(Text("OS:", style=label_color), Text(os_info, style=value_color))
    table.add_row(Text("Host:", style=label_color), Text(host, style=value_color))
    table.add_row(Text("Kernel:", style=label_color), Text(kernel, style=value_color))
    table.add_row(Text("Uptime:", style=label_color), Text(uptime, style=value_color))
    table.add_row(
        Text("Packages:", style=label_color), Text(packages, style=value_color)
    )
    table.add_row(Text("Shell:", style=label_color), Text(shell, style=value_color))
    table.add_row(
        Text("Resolution:", style=label_color), Text(resolution, style=value_color)
    )
    table.add_row(Text("DE/WM:", style=label_color), Text(de, style=value_color))
    table.add_row(Text("CPU:", style=label_color), Text(cpu, style=value_color))
    table.add_row(Text("GPU:", style=label_color), Text(gpu, style=value_color))
    table.add_row(Text("RAM:", style=label_color), Text(memory, style=value_color))

    logo = """
wena 
cauros
    """

    logo_text = Text(logo, style="bold yellow")
    logo_panel = Panel.fit(logo_text, border_style="yellow", padding=(0, 2))

    layout = Table.grid(expand=True)
    layout.add_column(justify="left", ratio=1)
    layout.add_column(justify="left", ratio=4)
    layout.add_row(logo_panel, table)

    console.print(Align.left(layout))
