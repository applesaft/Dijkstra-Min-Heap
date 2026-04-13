import sys
from min_heap import *
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Ask the user for the size of the graph and fill the adjacency matrix row by row through the CLI.
def get_matrix_from_user():
    console.print(Panel.fit(
        "[white]Welcome to DijkstraFromScratch[/white]\n"
        "[white]Shortest path algorithm using a custom min-heap[/white]",
        border_style="white"
    ))

    console.print("\n[white]Define your graph[/white]\n")
    while True:
        try:
            size = int(console.input(
                "[white]Enter the number of nodes in your graph: [/white]"
            ))
            if size <= 0:
                console.print("[white]Size must be a positive number. Try again.[/white]")
            else:
                break
        except ValueError:
            console.print("[white]Invalid input. Please enter a whole number.[/white]")

    console.print(f"\n[white]Fill the adjacency matrix[/white]")
    console.print(f"[white]Enter each row as {size} space-separated values.[/white]")
    console.print(f"[white]Use 0 for no connection, any positive number for weight.[/white]\n")

    matrix = []

    for i in range(size):
        while True:
            try:
                row_input = console.input(f"[white]Row {i} → [/white]")
                row = list(map(int, row_input.split()))

                if len(row) != size:
                    console.print(f"[white]Expected {size} values, got {len(row)}. Try again.[/white]")
                    continue

                if any(value < 0 for value in row):
                    console.print("[white]Negative delays are not allowed. Try again.[/white]")
                    continue

                if row[i] != 0:
                    console.print(f"[white]Diagonal value at position {i} must be 0. Try again.[/white]")
                    continue

                matrix.append(row)
                break

            except ValueError:
                console.print("[white]Invalid input. Use whole numbers separated by spaces.[/white]")

    console.print(f"\n[white]Graph defined successfully![/white]\n")

    table = Table(
        title="[white]Adjacency Matrix[/white]",
        border_style="white",
        header_style="white"
    )

    table.add_column("Node", style="white", justify="center")

    for i in range(size):
        table.add_column(str(i), justify="center", style="white")

    for i in range(size):
        row_values = []
        for value in matrix[i]:
            if value == 0:
                row_values.append("[dim white]0[/dim white]")
            else:
                row_values.append(f"[white]{value}[/white]")
        table.add_row(str(i), *row_values)

    console.print(table)

    console.print(f"\n[white]Step 3: Choose your source node[/white]\n")

    while True:
        try:
            source = int(console.input(
                f"[white]Enter source node (0 to {size - 1}): [/white]"
            ))
            if source < 0 or source >= size:
                console.print(f"[white]Source must be between 0 and {size - 1}. Try again.[/white]")
            else:
                break
        except ValueError:
            console.print("[white]Invalid input. Please enter a whole number.[/white]")

    console.print(f"\n[white]Source node set to {source}[/white]\n")

    while True:
        try:
            destination = int(console.input(
                f"[white]Enter destination node (0 to {size - 1}): [/white]"
            ))
            if destination < 0 or destination >= size:
                console.print(f"[white]Must be between 0 and {size - 1}. Try again.[/white]")
            elif destination == source:
                console.print("[white]Destination must be different from source. Try again.[/white]")
            else:
                break
        except ValueError:
            console.print("[white]Invalid input. Please enter a whole number.[/white]")

    console.print(f"\n[white]Routing from node {source} to node {destination}[/white]\n")

    return matrix, size, source, destination

def display_results(distances, previous, source, destination, matrix):
    console.print(Panel.fit(
        f"[white]Shortest path from node {source} to node {destination}[/white]",
        border_style=None
    ))

    if distances[destination] == sys.maxsize:
        console.print(
            f"\n[white]No path found from node {source} "
            f"to node {destination}.[/white]\n"
        )
        return

    # Reconstruct the path by walking backwards
    path = []
    current = destination

    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    console.print(f"\n[white]Path:[/white]\n")

    table = Table(
        border_style="white",
        header_style="white",
        show_header=None
    )

    table.add_column("", style="white", justify="center")
    table.add_column("From", style="white", justify="center")
    table.add_column("To", style="white", justify="center")
    table.add_column("Weight", style="white", justify="center")
    table.add_column("Cumulative Cost", style="white", justify="center")

    # Walk through the path and display each hop
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]

        edge_weight = matrix[from_node][to_node]
        cumulative_cost = distances[to_node]

        table.add_row(
            str(i + 1),
            f"Node {from_node}",
            f"Node {to_node}",
            str(edge_weight),
            str(cumulative_cost)
        )

    console.print(table)
    console.print(
        f"\n[white]Total cost: {distances[destination]}[/white]\n"
    )
