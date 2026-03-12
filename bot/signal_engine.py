import json

coins=json.load(open("data/coins.json"))

signals=[]

for c in coins:

    if c["change"] > 6:
        signals.append({
        "symbol":c["symbol"],
        "signal":"LONG"
        })

    elif c["change"] < -6:
        signals.append({
        "symbol":c["symbol"],
        "signal":"SHORT"
        })

with open("data/signals.json","w") as f:
 json.dump(signals,f)
