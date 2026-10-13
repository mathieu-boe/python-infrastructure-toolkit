from infra_toolkit.cli import main


def test_health_command_prints_status(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr("sys.argv", ["infra-toolkit", "health"])

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "Status: operational\n"
    assert captured.err == ""


def test_help_command_exits_successfully(
    monkeypatch,
) -> None:
    monkeypatch.setattr("sys.argv", ["infra-toolkit", "--help"])

    try:
        main()
    except SystemExit as exc:
        assert exc.code == 0
    else:
        raise AssertionError("Help should exit successfully")


def test_system_info_command_prints_system_details(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr("sys.argv", ["infra-toolkit", "system-info"])

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "System Information" in captured.out
    assert "Operating system:" in captured.out
    assert "Python version:" in captured.out
    assert "Architecture:" in captured.out
    assert captured.err == ""


def test_resource_usage_command_prints_metrics(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr("sys.argv", ["infra-toolkit", "resource-usage"])
    monkeypatch.setattr(
        "infra_toolkit.cli.get_resource_usage",
        lambda: {
            "cpu_percent": 25.0,
            "memory_percent": 60.0,
            "disk_percent": 75.0,
        },
    )

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == ("Resource Usage\n--------------\nCPU usage: 25.0%\nMemory usage: 60.0%\nDisk usage: 75.0%\n")
    assert captured.err == ""
