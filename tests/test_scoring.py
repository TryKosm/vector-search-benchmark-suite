from bench.scoring import precision_at_k


def test_precision_at_k() -> None:
    assert precision_at_k({"a", "b"}, ["a", "x", "b"], 3) == 2 / 3
