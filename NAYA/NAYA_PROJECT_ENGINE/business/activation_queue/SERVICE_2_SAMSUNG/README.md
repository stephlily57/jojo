# Arbitrage et prévention de risque stratégique

Target:
Groupe industriel / tech (Samsung)

SLA:
24-72h

Pricing:
- Base price: 11000000 XPF
- Model: Loss-based pricing

Pricing logic:
price = max(base_price, daily_loss * spread_factor)

Files:
- service_definition.py
- manifest.json
- requirements.txt