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
