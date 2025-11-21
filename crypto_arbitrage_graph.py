import requests
import json
from itertools import combinations
import networkx as nx

# Getting Exchange Rates From Coingecko
# Using the /simple/price endpoint to get the 7 coins

url = ("https://api.coingecko.com/api/v3/simple/price?"
       "ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,eos"
       "&vs_currencies=eth,btc,ltc,xrp,ada,bch,eos")

print("Requesting exchange rates...")
req = requests.get(url)
data = json.loads(req.text)

# id to ticker
id_to_ticker = {
    "ethereum": "eth",
    "bitcoin": "btc",
    "litecoin": "ltc",
    "ripple": "xrp",
    "cardano": "ada",
    "bitcoin-cash": "bch",
    "eos": "eos"
}

tickers = list(id_to_ticker.values())

# Create Graph
# Add edges: (from_ticker, to_ticker, exchange_rate)

g = nx.DiGraph()
edges = []

print("\nAdding edges to graph...\n")

for cid, rates in data.items():
    c_from = id_to_ticker[cid]

    for c_to, rate in rates.items():
        if c_to in tickers and rate > 0:
            edges.append((c_from, c_to, float(rate)))
            print("adding edge:", c_from, "to", c_to, "rate:", rate)

g.add_weighted_edges_from(edges)

print("\nGraph Nodes:", g.nodes, "\n")

# Traverse Graph
# For every currency pair, check all simple paths
# Calculate path weight, reverse path weight, arbitrage factor

smallest_factor = (999999999, None, None)
largest_factor = (0, None, None)

# combinations, ensures we cover each unordered pair once
for n1, n2 in combinations(g.nodes, 2):

    print("Paths from", n1, "to", n2)

    # n1 to n2
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print("\nPath To:", path)

        # path weight forward
        weight_to = 1.0
        for i in range(len(path) - 1):
            weight_to *= g[path[i]][path[i+1]]['weight']
        print("path weight:", weight_to)

        # reverse path
        rev = list(reversed(path))
        print("Path From:", rev)

        weight_from = 1.0
        valid_reverse = True

        for i in range(len(rev) - 1):
            if rev[i+1] not in g[rev[i]]:
                valid_reverse = False
                break
            weight_from *= g[rev[i]][rev[i+1]]['weight']

        if not valid_reverse:
            print("Reverse path does not exist\n")
            continue

        print("path weight:", weight_from)

        factor = weight_to * weight_from
        print("factor:", factor, "\n")

        # update smallest/largest
        if factor < smallest_factor[0]:
            smallest_factor = (factor, path, rev)
        if factor > largest_factor[0]:
            largest_factor = (factor, path, rev)

print("\nFINAL RESULTS\n")

print("Smallest Paths weight factor:", smallest_factor[0])
print("Paths:", smallest_factor[1], smallest_factor[2])

print("\nGreatest Paths weight factor:", largest_factor[0])
print("Paths:", largest_factor[1], largest_factor[2])
