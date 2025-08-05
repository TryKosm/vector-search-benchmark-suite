from .scoring import precision_at_k


def run_case(expected: set[str], predicted: list[str]) -> dict[str, float]:
    return {"p_at_3": precision_at_k(expected, predicted, 3)}
