# ProvableFair AI

> **Algorithmic Transparency & Mathematical Audit Sandbox for AI Decision Systems.**  
> *Calculates demographic parity, disparate impact ratios (EEOC 80% rule), and zero-knowledge / HMAC commit-reveal cryptographic proofs.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/downloads/)
[![Zero-Dependency](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Grant-Ready](https://img.shields.io/badge/Grant--Eligible-Gates%20Foundation%20%7C%20Fintech%20Inclusion-orange.svg)]()

---

## 🎯 Abstract

As AI models are increasingly deployed across digital lending, micro-credit scoring, hiring screening, and automated underwriting, verifying that algorithms do not discriminate against protected groups is a vital regulatory and human rights imperative.

**ProvableFair AI** provides a lightweight mathematical audit harness and commit-reveal cryptographic framework. Model deployers can prove compliance with regulatory fairness criteria (such as the EEOC Four-Fifths rule and equalized odds) without revealing private individual training records or proprietary weights.

---

## ⚡ Key Capabilities

- **Pure Standard Python**: Zero complex neural dependencies or external numerical packages.
- **Regulatory Bias Metrics**: Computes Statistical Parity Difference, Disparate Impact Ratio, and Equal Opportunity Difference.
- **Commit-Reveal Proofs**: Cryptographic proof hashes ensure evaluation sets cannot be retroactively cherry-picked.

---

## 🚀 Quickstart

```bash
git clone https://github.com/abenih/provable-fair-ai.git
cd provable-fair-ai
./bin/provable-fair-ai --help
```

---

## 📄 License
MIT License. Created by [Susan (Abenezer)](https://satiralabs.com) at SatiraLabs.
