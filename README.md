# VerdantWatch – Decentralized Environmental Monitoring on Cardano

[![Catalyst Fund15 Proposal](https://img.shields.io/badge/Catalyst-Fund15_Proposal-green)](https://projectcatalyst.io/)

**Relentless Vigilance of Earth's vital resources.**

VerdantWatch deploys low-cost, field-ready sensors that stream tamper-proof air quality, soil health, water contaminants (including PFAS/PFOS), and biodiversity data directly to Cardano. Every reading is timestamped, immutable, and instantly queryable — creating a global, verifiable "verdant pulse" that communities, researchers, governments, and enterprises can trust and act upon.

By combining rugged hardware, edge computing, and Cardano’s energy-efficient ledger + Hydra scaling, VerdantWatch eliminates single points of failure and data manipulation risks that plague traditional monitoring systems.

Currently advancing a funded proposal in **Project Catalyst Fund 15**.

## 🌿 Catalyst Fund15 Proposal
[Final proposal link here after submission – e.g., https://cardano.ideascale.com/c/idea/XXXXXX]

## 🚀 Current Status – November 2025
- Working prototype: sensor → Cardano metadata transaction
- Mock dashboard with live-updating data visualization
- Full proposal, budget, milestones, and impact metrics in `/docs`
- `/code` contains real runnable scripts
- Open for community contributions & partnerships

## Quick Start (for reviewers & contributors)
```bash
git clone https://github.com/verdantwatch/verdantwatch-monitoring.git
cd verdantwatch-monitoring
# Run the mock sensor that prints real-time data every 5 seconds
python code/mock_sensor.py
```

## Tech Stack

Blockchain: Cardano mainnet + custom transaction metadata
Scaling: Hydra heads for instant, low-cost data streams
Hardware (planned): ESP32 / Arduino + LoRa sensors (partnerships in progress)
Backend: Python + Cardano serialization-lib
Frontend: React dashboard (live mock in /dashboard)
Data verification: On-chain timestamps + Merkle proofs

## Folder Structure

/code      → sensor scripts, Cardano integration, mock data generator
/dashboard → live React mock UI (deployed via GitHub Pages)
/docs       → full Catalyst proposal PDF, detailed budget, milestones, risk analysis
/data       → sample datasets & example queries

## Impact for Cardano
VerdantWatch leverages Cardano's efficiency to make environmental monitoring accessible and scalable, turning real-time eco-data into verifiable assets for global impact—aligning with Fund15's focus on transformative use cases

## Get Involved
We’re actively seeking:

Sensor hardware partners (PFAS, air quality, soil)
Cardano developers for Hydra & smart-contract governance layer
Environmental NGOs for pilot deployments
Impact investors & Catalyst voters

## MIT License • VerdantWatch LLC • Pleasanton, California, USA
## contact@verdantwatch.org • verdantwatch.org
