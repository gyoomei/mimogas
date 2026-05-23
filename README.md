<div align="center">

# ⛽ MiMoGas

### Multi-Chain Gas Optimizer & Predictor

**Powered by Xiaomi MiMo V2.5 AI**

[![Live Demo](https://img.shields.io/badge/Live-Demo-f97316?style=for-the-badge&logo=github&logoColor=white)](https://gyoomei.github.io/mimogas/)
[![Chains](https://img.shields.io/badge/Chains-15%20EVM-blue?style=for-the-badge&logo=ethereum&logoColor=white)](#supported-chains)
[![AI](https://img.shields.io/badge/AI-MiMo%20V2.5-purple?style=for-the-badge)](#ai-features)
[![Backend](https://img.shields.io/badge/Backend-Zero%20Backend-green?style=for-the-badge)](#architecture)

---

**Stop guessing gas fees.** MiMoGas gives you real-time gas prices across 15 EVM chains with AI-powered optimization advice — all in a single HTML file, zero backend.

</div>

---

## 🔥 The Problem

Gas fees are unpredictable. You want to:
- Swap tokens → but ETH gas is 45 Gwei
- Mint an NFT → but you don't know if Polygon is cheaper
- Bridge funds → but you're guessing the optimal chain

**MiMoGas solves this in 3 seconds.**

## ✨ Features

### 📊 Real-Time Gas Dashboard
- **15 EVM chains** in one view — Ethereum, BNB, Polygon, Arbitrum, Optimism, Base, Avalanche, Gnosis, Fantom, Celo, zkSync Era, Linea, Scroll, Mantle, Polygon zkEVM
- Live gas prices fetched from **Blockscout V2 API** (free, no API key)
- ETH transfer cost calculator per chain
- Visual gas intensity bars (green = cheap, yellow = moderate, red = expensive)

### 🧠 MiMo AI Gas Advisor
- **Xiaomi MiMo V2.5** analyzes real-time data and generates actionable advice
- "Best Now" / "Good Choice" / "Wait" recommendations
- Specific savings percentages (e.g., "Save 98% vs Ethereum")
- Timing advice based on historical patterns

### 📊 Gas Price Ranking
- All chains ranked from cheapest to most expensive
- Visual comparison bars for instant understanding
- Filter by: Cheap (<1 Gwei) / Moderate / Expensive (>10 Gwei) / L2 only

### 🔄 Auto-Refresh
- Data refreshes every **60 seconds**
- Always up-to-date for time-sensitive decisions

## 🎬 How It Works

1. **Open the page** → 15 chains load simultaneously
2. **See gas prices** → ranked, compared, visualized
3. **Read AI advice** → MiMo tells you where to transact now
4. **Filter & compare** → find the cheapest chain for your needs

**That's the entire UX.**

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                  MiMoGas (Browser)               │
│                                                  │
│  ┌──────────────┐   ┌──────────────────────┐    │
│  │  Blockscout   │   │  Xiaomi MiMo V2.5    │    │
│  │  V2 API       │   │  (via Pollinations)  │    │
│  │  15 chains    │   │  AI recommendations  │    │
│  └──────┬───────┘   └──────────┬───────────┘    │
│         │                      │                 │
│  ┌──────▼──────────────────────▼───────────┐    │
│  │         index.html (26 KB)              │    │
│  │   • Zero dependencies                   │    │
│  │   • Zero backend                        │    │
│  │   • Pure client-side                    │    │
│  └────────────────────────────────────────-┘    │
└─────────────────────────────────────────────────┘
```

## ⛓️ Supported Chains

| Chain | Type | API Source |
|-------|------|-----------|
| Ethereum | L1 | eth.blockscout.com |
| BNB Chain | L1 | api.bscscan.com |
| Polygon | L2 | polygon.blockscout.com |
| Arbitrum One | L2 | arbitrum.blockscout.com |
| Optimism | L2 | optimism.blockscout.com |
| Base | L2 | base.blockscout.com |
| Avalanche C | L1 | api.snowtrace.io |
| Gnosis | L1 | gnosis.blockscout.com |
| Celo | L1 | celo.blockscout.com |
| zkSync Era | L2 | zksync.blockscout.com |
| Scroll | L2 | scroll.blockscout.com |
| Mode | L2 | explorer.mode.network |
| Zora | L2 | explorer.zora.energy |
| Linea | L2 | api.lineascan.build |
| Mantle | L2 | api.routescan.io |

## 🔒 Security & Privacy

- **Zero API keys** — uses public Blockscout endpoints
- **Zero tracking** — no analytics, no cookies, no user data
- **Zero backend** — everything runs in browser
- **Open source** — inspect the single HTML file
- **No wallet connection** — read-only, no signing required

## ⚡ Performance

| Metric | Value |
|--------|-------|
| Page size | 26 KB (single HTML) |
| Dependencies | 0 |
| API calls | 15 parallel |
| Load time | <2s (all chains) |
| Refresh interval | 60s |
| Supported chains | 15 |

## 🛠️ Local Development

```bash
# Clone and serve
git clone https://github.com/gyoomei/mimogas.git
cd mimogas
python3 -m http.server 8080
# Open http://localhost:8080
```

No build step. No dependencies. Just open `index.html`.

## 📜 License

MIT

---

<div align="center">

**Built for [Xiaomi MiMo 100T Creator Program](https://mimo.xiaomimodel.com)**

Made with ⛽ by [@Limzyallin](https://x.com/Limzyallin)

</div>
