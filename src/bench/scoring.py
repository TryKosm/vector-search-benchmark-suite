def precision_at_k(expected: set[str], predicted: list[str], k: int) -> float:
    top = predicted[:k]
    if not top:
        return 0.0
    hits = sum(1 for x in top if x in expected)
    return hits / len(top)
