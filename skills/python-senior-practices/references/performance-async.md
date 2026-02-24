# Performance and Async Guide

Use this reference when performance matters or when selecting a concurrency model.

## Workflow

1. Measure first.
2. Identify the bottleneck type (CPU, I/O, memory, lock contention).
3. Pick the minimal concurrency model that addresses that bottleneck.
4. Re-measure and compare against baseline.

## Profiling Tools

- Use `cProfile` for deterministic CPU hotspot analysis.
- Use `py-spy` for low-overhead production-like sampling.
- Use app-level timing/metrics for end-to-end latency and throughput.

## Concurrency Decision Matrix

| Workload | Preferred Model | Notes |
|---|---|---|
| High network/file I/O | `asyncio` | Keep blocking calls out of event loop |
| CPU-heavy transforms | `multiprocessing` | Avoid GIL constraints |
| Legacy blocking libraries | `threading` | Use with bounded pools and explicit shutdown |

## Async Practices

- Keep async boundaries explicit (`async def`, `await`).
- Avoid blocking operations in coroutines; move them to thread/process executors.
- Use timeouts for external calls.
- Apply backpressure with semaphores/queues when fan-out is high.
- Cancel tasks intentionally and handle `CancelledError` when cleanup is needed.

## Data Structure Defaults

- Use `set` for membership tests.
- Use `collections.deque` for FIFO/LIFO queues.
- Use `defaultdict` or `Counter` for aggregate counting.
- Use generator expressions for single-pass computation.

## Anti-Patterns

- Optimizing before measuring.
- Unbounded task spawning.
- Mixing sync and async API layers without explicit adapters.
- Premature micro-optimizations that reduce readability without measurable gain.
