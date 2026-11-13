# Aerospace Parameter Optimizer

This project provides a flexible and efficient tool for optimizing parameters in aerospace-related calculations, leveraging search-based tuning strategies to streamline complex orbital mechanics computations. Built from the ground up in pure Python, it offers a robust foundation for real-world applications. With comprehensive testing and documentation, users can quickly integrate this optimizer into their workflows.

## What makes it unique

Combines orbital mechanics calculations with a search-based tuner (grid, random, and annealing strategies) — a niche where few ready-made tools exist.

## Features

- **`aerospace_optimizer/optimizer.py`** — Main optimizer class implementing search strategies
- **`aerospace_optimizer/grid_optimizer.py`** — Grid-based optimization strategy implementation
- **`aerospace_optimizer/random_optimizer.py`** — Random search optimization strategy implementation
- **`aerospace_optimizer/simulated_annealing.py`** — Simulated annealing optimization strategy implementation
- **`aerospace_optimizer/parameter.py`** — Data structure and methods for parameter handling (e.g. bounds, constraints)
- **`aerospace_optimizer/test_optimizer.py`** — Unit tests for optimizer classes

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/aerospace-optimizer.git
cd aerospace-optimizer

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
aerospace-optimizer/
├── aerospace_optimizer/
│   ├── optimizer.py
│   ├── grid_optimizer.py
│   ├── random_optimizer.py
│   ├── simulated_annealing.py
│   ├── parameter.py
│   ├── test_optimizer.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **aerospace** · Archetype: **optimizer** ·
Built autonomously by JARVIS on 2026-11-13. MIT licensed.
