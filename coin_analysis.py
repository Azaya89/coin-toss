from coin import Coin
from plotly import offline
import time


def main():
    n = 0
    while n <= 1_000_000:  # Toss the coin one million times
        n += 10
        if (
            n == 10
            or n == 10**2
            or n == 10**3
            or n == 10**4
            or n == 10**5
            or n == 10**6
        ):
            time.sleep(0.5)
            plot_toss(
                n
            )  # Plot the bar chart at 10, 100, 1k, 10k, 100k and 1M coin tosses


def toss_number(n: int) -> list:
    """Returns a list containing the results of the number of coin tosses"""
    coin = Coin()  # Create a coin instance
    results = []  # Create empty list to store coin toss results
    for _ in range(n):
        coin_toss = coin.toss()  # Toss the coin n times
        results.append(coin_toss)  # Append each toss result to the empty list
    return results


def plot_toss(n):
    """Plot a bar chart showing the percentage results of a coin toss n number of times."""
    toss = toss_number(n)  # Get the list of coin toss results
    frequencies = {
        "Heads": toss.count("head"),
        "Tails": toss.count("tail"),
    }  # Create a dict with the number of 'Heads' and 'Tails'

    x_values = list(frequencies.keys())  # List containing the dict keys (Head and Tail)
    frequency = list(
        frequencies.values()
    )  # List containing the count of 'Head' and 'Tail'
    y_values = []  # Create empty list to store the percentage of the counts
    for num in frequency:
        percentage = (num / sum(frequency)) * 100  # Convert the frequency to percentage of total
        y_values.append(percentage)  # Append the percentage to empty list
    data = [
        {
            "type": "bar",
            "x": x_values,
            "y": y_values,
            "width": 0.3,
            "marker": {
                "color": "rgb(0,153,0)",
                "line": {"width": 2, "color": "rgb(102, 0, 204)"},
                "opacity": 0.6,
            },
        }
    ]  # Populate chart with the x and y values, add colour and width to chart.

    title = f"Coin toss {n} times"
    my_layout = {
        "title": title,
        "titlefont": {"size": 28},
        "xaxis": {
            "title": "Coin sides",
            "titlefont": {"size": 28},
            "tickfont": {"size": 14},
        },
        "yaxis": {
            "title": "Percentage",
            "titlefont": {"size": 28},
            "tickfont": {"size": 14},
        },
    }  # Label chart parameters
    fig = {"data": data, "layout": my_layout}
    offline.plot(fig)  # Plot chart in offline mode


if __name__ == "__main__":
    main()
