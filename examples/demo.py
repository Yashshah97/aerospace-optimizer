"""Demo for Aerospace Parameter Optimizer."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import aerospace_optimizer

print("Aerospace Parameter Optimizer", "v" + aerospace_optimizer.__version__)
print("modules:", [m for m in dir(aerospace_optimizer) if not m.startswith('_')])
