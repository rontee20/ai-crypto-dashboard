import requests, json

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
"vs_currency":"usd",
"order":"market_cap_desc",
"per_page":200,
"page":1
}

data = requests.get(url,params=params).json()

coins=[]

for c in data:
    coins.append({
        "symbol":c["symbol"],
        "price":c["current_price"],
        "change":c["price_change_percentage_24h"]
    })

with open("data/coins.json","w") as f:
    json.dump(coins,f)
