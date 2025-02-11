"""agents.py

File contains the party config tuples for each agent in the MultiMarket scenario. The
scenario runs a network with three markets each with a configurable number of market
order trader agents.

"""
from collections import namedtuple

PartyConfig = namedtuple("AgentConfig", ["wallet_name", "key_name"])

# Set-up wallets and keys for MarketManager agents
MARKET_MANAGERS = {
    "MARKET_A_CREATOR": PartyConfig("market_managers", "Market A Creator"),
    "MARKET_A_SETTLER": PartyConfig("market_managers", "Market A Settler"),
    "MARKET_B_CREATOR": PartyConfig("market_managers", "Market B Creator"),
    "MARKET_B_SETTLER": PartyConfig("market_managers", "Market B Settler"),
    "MARKET_C_CREATOR": PartyConfig("market_managers", "Market C Creator"),
    "MARKET_C_SETTLER": PartyConfig("market_managers", "Market C Settler"),
}

# Set-up wallets and keys for CurvedMarketMaker agents
MARKET_MAKERS = {
    "MARKET_A_MAKER": PartyConfig("market_makers", "Market A Maker"),
    "MARKET_B_MAKER": PartyConfig("market_makers", "Market B Maker"),
    "MARKET_C_MAKER": PartyConfig("market_makers", "Market C Maker"),
}

# Set-up wallets and keys for AuctionPass agents
MARKET_PASSERS = {
    "MARKET_A_PASSER_BID": PartyConfig("market_passers", "Market A Passer Bid"),
    "MARKET_A_PASSER_ASK": PartyConfig("market_passers", "Market A Passer Ask"),
    "MARKET_B_PASSER_BID": PartyConfig("market_passers", "Market B Passer Bid"),
    "MARKET_B_PASSER_ASK": PartyConfig("market_passers", "Market B Passer Ask"),
    "MARKET_C_PASSER_BID": PartyConfig("market_passers", "Market C Passer Bid"),
    "MARKET_C_PASSER_ASK": PartyConfig("market_passers", "Market C Passer Ask"),
}

# Set-up wallets and keys for MarketOrderTrader agents
MARKET_TRADERS = {
    f"MARKET_{i}_TRADER_{str(k).zfill(4)}": PartyConfig(
        "market_traders", f"Market {i} Trader {str(k).zfill(4)}"
    )
    for i in ["A", "B", "C"]
    for k in range(1000)
}
