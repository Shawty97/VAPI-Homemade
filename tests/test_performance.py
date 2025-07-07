import time


def test_performance_placeholder() -> None:
    start = time.time()
    time.sleep(0.01)
    end = time.time()
    assert end - start < 0.5
