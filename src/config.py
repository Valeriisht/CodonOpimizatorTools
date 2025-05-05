from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class OptimizationConfig:
    organism: str = "e_coli"  # default
    strategy_name: str = "cai"  # default
    gc_bounds: tuple[float] = (40.0, 60.0)  # gc_stategy
    gc_target: float = None
    cai_threshold: float = 0.8  # CAI filtering
