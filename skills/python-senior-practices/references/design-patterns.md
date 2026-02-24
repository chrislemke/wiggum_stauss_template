# Design Patterns (Python-First)

Use this reference when choosing an implementation pattern for extensibility or complexity management.

## Selection Guide

| Pattern | Use When | Python Idiom | Avoid When |
|---|---|---|---|
| Strategy | Swap algorithms at runtime | First-class functions or `Protocol` implementations | Behavior is fixed and simple |
| Factory | Build complex objects with validation/defaults | `@classmethod` constructors or factory function | Construction is trivial |
| Decorator | Add cross-cutting behavior | `@functools.wraps` decorator stack | Behavior should be explicit inline |
| Observer | Notify multiple consumers of events | Callback lists, signal/event libraries | One direct call site is enough |
| Iterator | Stream large/sequential data | Generators with `yield` | You need random access materialization |
| Context Manager | Control resource lifecycle | `with` + `contextmanager` or `__enter__/__exit__` | No resource ownership/lifecycle concern |
| Adapter | Normalize external interfaces | Thin wrapper around SDK/client | Native interface already matches needs |

## Examples

## Strategy via Protocol

```python
from typing import Protocol

class ScoringStrategy(Protocol):
    def score(self, text: str) -> float: ...

class LengthScorer:
    def score(self, text: str) -> float:
        return float(len(text))

def rank(texts: list[str], strategy: ScoringStrategy) -> list[tuple[str, float]]:
    return [(text, strategy.score(text)) for text in texts]
```

## Factory for Valid Construction

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Endpoint:
    scheme: str
    host: str
    port: int

    @classmethod
    def from_host(cls, host: str, tls: bool = True) -> "Endpoint":
        return cls("https" if tls else "http", host, 443 if tls else 80)
```

## Context Manager for Resource Lifetime

```python
from contextlib import contextmanager

@contextmanager
def opened(path: str):
    handle = open(path, "r", encoding="utf-8")
    try:
        yield handle
    finally:
        handle.close()
```

## Review Checks

- Confirm the chosen pattern removes present complexity, not hypothetical future complexity.
- Confirm the pattern keeps call sites simpler, not harder.
- Confirm tests enforce the core contract (especially for `Protocol`-based designs).
