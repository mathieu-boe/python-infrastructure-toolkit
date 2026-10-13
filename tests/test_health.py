from infra_toolkit.health import check_status


def test_check_status_returns_operational() -> None:
    """This test verifies the function returns the expected value. Later, we'll extend the toolkit with useful infrastructure operations and more comprehensive tests."""
    assert check_status() == "operational"
