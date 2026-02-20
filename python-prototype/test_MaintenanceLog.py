import pytest
from unittest.mock import patch
from MaintenanceLogCLI import *


def test_load_tasks_file_not_found(capsys):
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_tasks()
    assert result == []
    captured = capsys.readouterr()
    assert LOADTASKSERROR in captured.out


def test_load_tasks_json_decode_error(capsys):
    with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
        result = load_tasks()
    assert result == []
    captured = capsys.readouterr()
    assert LOADTASKSERROR in captured.out