from src.pre_built.counter import count_ocurrences


def test_counter():
    value = count_ocurrences("data/jobs.csv", "Python")
    assert value == 1639
