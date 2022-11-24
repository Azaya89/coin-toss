from coin import Coin
from plotly import offline
import time


def main():
    n = 0
    while n <= 1_000_000:
        n += 100
        if (
            n == 10**2 or n == 10**3 or n == 10**4 or n == 10**5 or n == 10**6
        ):  # Plot the bar chart at 100, 1k, 10k, 100k and 1M coin tosses
            time.sleep(0.5)
            plot_toss(n)


def toss_number(n):
    """Returns a list containing the results of the number of coin tosses"""
    coin = Coin()
    results = []
    for _ in range(n):
        coin_toss = coin.toss()
        results.append(coin_toss)
    return results


def plot_toss(n):
    toss = toss_number(n)
    frequencies = {"Heads": toss.count("head"), "Tails": toss.count("tail")}

    x_values = list(frequencies.keys())
    frequency = list(frequencies.values())
    y_values = []
    for num in frequency:
        percentage = (num / sum(frequency)) * 100
        y_values.append(percentage)
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
    ]

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
    }
    fig = {"data": data, "layout": my_layout}
    offline.plot(fig)


if __name__ == "__main__":
    main()
