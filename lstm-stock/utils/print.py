from rich.console import Console
console = Console()

def printAsBanner(str: str):
    length = len(str)
    boarder = '=' * (length + 2)
    spaces = ' ' * length
    
    
    # console.print(
    #     f'''
    #     {boarder}
    #     |{spaces}|
    #     |[bold cyan]{str}[/bold cyan]|
    #     |{spaces}|
    #     {boarder}
    # ''',
    # justify="center"
    # )
    console.print(f"[u][bold cyan]{str}[/bold cyan][/u]",justify="center")

def printJustifiedLeftRed(str: str):
    console.print(f"[bold red]{str}[/bold red]",justify="left")