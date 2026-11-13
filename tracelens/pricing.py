"""Cost estimation from token counts.

Prices are USD per 1M tokens as (input, output). They are approximate defaults
and can be overridden with a JSON file via the TRACELENS_PRICING env var, e.g.
{"my-model": [1.0, 2.0]}.
"""
import json
import os
from typing import Dict, Tuple

DEFAULT_PRICES: Dict[str, Tuple[float, float]] = {
    "gpt-4o": (2.50, 10.00),
    "gpt-4o-mini": (0.15, 0.60),
    "claude-sonnet": (3.00, 15.00),
    "claude-haiku": (0.80, 4.00),
    "local": (0.0, 0.0),
}


def load_prices() -> Dict[str, Tuple[float, float]]:
    prices = dict(DEFAULT_PRICES)
    path = os.environ.get("TRACELENS_PRICING")
    if path and os.path.exists(path):
        with open(path) as fh:
            for model, pair in json.load(fh).items():
                prices[model.lower()] = (float(pair[0]), float(pair[1]))
    return prices


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Return estimated cost in USD. Unknown models cost 0.

    Matching uses the longest known prefix, so "gpt-4o-mini-2024" matches
    "gpt-4o-mini" and not "gpt-4o".
    """
    prices = load_prices()
    name = model.lower()
    best = None
    for key in prices:
        if name.startswith(key) and (best is None or len(key) > len(best)):
            best = key
    if best is None:
        return 0.0
    price_in, price_out = prices[best]
    return (input_tokens * price_in + output_tokens * price_out) / 1_000_000
