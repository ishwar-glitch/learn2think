"""Screen bodies for the D3 mock-ups, keyed by page slug (metadata stays in pages_a/pages_b)."""
from bodies_a import B as _A
from bodies_b import B as _B

BODIES = {**_A, **_B}
