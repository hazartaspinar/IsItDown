import requests
import socket
import subprocess
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table

def check_http_status(url):
    """Check HTTP response status."""
    try:
        response = requests.get(f"https://{url}", timeout=5)
        if response.status_code == 200:
            return "Success", "200 OK"
        else:
            return "Failed", f"{response.status_code} {response.reason}"
    except requests.exceptions.RequestException as e:
        return "Failed", str(e)

def check_icmp_ping(host):
    """Check ICMP ping response."""
    try:
        result = subprocess.run(["ping", "-c", "1", "-W", "2", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Success" if result.returncode == 0 else "Failed"
    except Exception:
        return "Failed"

def check_tcp_connection(host, port):
    """Check TCP connection on a specific port."""
    try:
        with socket.create_connection((host, port), timeout=5):
            return "Success"
    except (socket.timeout, socket.error):
        return "Failed"

def continuous_test(host, port):
    """Run continuous test using multiple methods."""
    console.print(f"\n[bold yellow]Starting continuous test on[/bold yellow] [bold cyan]{host}:{port}[/bold cyan]...")
    console.print("[yellow]Press [bold red]Ctrl+C[/bold red] to stop.[/yellow]\n")

    table = Table(title="Already Down! - Test Results")
    table.add_column("Test", justify="center", style="cyan", no_wrap=True)
    table.add_column("Result", justify="center", style="green", no_wrap=True)
    table.add_column("Details", justify="left", style="magenta", no_wrap=False)

    try:
        with Live(table, refresh_per_second=0.5) as live:
            while True:
                http_result, http_details = check_http_status(host)
                icmp_result = check_icmp_ping(host)
                tcp_result = check_tcp_connection(host, port)

                table.rows.clear()
                table.add_row("HTTP Test", http_result, http_details)
                table.add_row("ICMP Ping Test", icmp_result, "")
                table.add_row("TCP Connection Test", tcp_result, "")

                if http_result == "Failed" and icmp_result == "Failed" and tcp_result == "Failed":
                    table.caption = "[bold red]Target is already down! Congratulations! 🎉[/bold red]"
                else:
                    table.caption = "[bold green]Target is responding to at least one method![/bold green]"

                time.sleep(3)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Continuous testing stopped by user.[/bold yellow]")

def display_banner():
    """Display the ASCII banner."""
    banner = """
 █████╗ ██╗     ██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
███████║██║     ██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ 
██╔══██║██║     ██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  
██║  ██║███████╗██║  ██║███████╗██║  ██║██████╔╝   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   
                                                          
██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗                 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║                 
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║                 
██║  ██║██║   ██║██║███╗██║██║╚██╗██║╚═╝                 
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║██╗                 
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝                 
"""
    console.print(f"[bold yellow]{banner}[/bold yellow]")
    console.print("[bold cyan]A powerful tool to celebrate your success in taking down a server![/bold cyan]")
    console.print("[bold yellow]=" * 30)

def interactive_mode():
    """Run the tool in interactive mode."""
    display_banner()
    host = input("Enter the target domain or external IP: ").strip()
    port = int(input("Enter the TCP port to check: "))
    continuous_test(host, port)

def main():
    interactive_mode()

if __name__ == "__main__":
    console = Console()
    main()
