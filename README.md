# QMOOSA CashFusion ($QCASH)
[![CI/CD Pipeline](https://github.com/elon00/qmoosa-cashfusion/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/elon00/qmoosa-cashfusion/actions/workflows/ci-cd-pipeline.yml)
[![Reality Check](https://img.shields.io/badge/Reality%20Check-100%2F100%20GENUINE%20GREEN-emerald.svg)](tests/reality_check_harness.py)
[![Hackathon](https://img.shields.io/badge/Hackathon-BCH%20BLAZE%202026-blue.svg)]()
[![PQC Standard](https://img.shields.io/badge/NIST-FIPS%20203%2F204-purple.svg)]()

> **BCH native CashTokens, merchant QR payments, autonomous recurring payment authorization, and UTXO state verification.**

---

## 🏆 Hackathon Profile
- **Target Event:** BCH BLAZE 2026
- **Track:** Bitcoin Cash CashTokens, Stablecoins, DeFi & Web3 Infrastructure
- **Deadline:** November 14-22, 2026 (Building Window)
- **Prize Pool:** $8,000
- **Blockchain:** Bitcoin Cash (BCH UTXO + CashTokens)

---

## 🚀 Key Features
- **64-bit Conway State Engine:** Deterministic cellular automaton state machine running 10,000 cycles in zero-dependency Rust.
- **Native Smart Contract:** `CashFusionCovenant.cash` optimized for Bitcoin Cash (BCH UTXO + CashTokens).
- **Agentic Service & x402 Gateway:** Autonomous Python payment client in `src/bch_merchant_engine.py`.
- **Interactive QUX Launchpad:** Full-stack responsive HTML5 dashboard with Conway visualizer and Web4 QR generation in `index.html`.
- **Model Context Protocol (MCP):** 2 native tools exposed via `mcp.json`.

---

## 🧪 Testing & Verification
```bash
# Run 5-Gate Reality Check Test Harness
python tests/reality_check_harness.py

# Run Full Unit & Integrity Test Suite
python -m unittest tests/test_suite.py
```
