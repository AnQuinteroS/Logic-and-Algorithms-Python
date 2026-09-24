"""Tests for the mini linter, using temporary folders with sample files."""
import textwrap

from mini_linter import run_linter


def write(tmp_path, name, code):
    """Writes a Python file inside the temporary test folder."""
    path = tmp_path / name
    path.write_text(textwrap.dedent(code), encoding="utf-8")
    return path


def test_clean_file_has_no_issues(tmp_path, capsys):
    write(tmp_path, "clean.py", '''
        def add(a, b):
            """Adds two numbers."""
            return a + b
    ''')
    assert run_linter(tmp_path) == 0
    assert "0 issues" in capsys.readouterr().out


def test_detects_long_line(tmp_path):
    write(tmp_path, "long.py", "x = '" + "a" * 100 + "'\n")
    assert run_linter(tmp_path) == 1


def test_line_of_exactly_79_characters_is_allowed(tmp_path):
    write(tmp_path, "limit.py", "x = '" + "a" * 73 + "'\n")  # 79 chars
    assert run_linter(tmp_path) == 0


def test_detects_uppercase_function_name(tmp_path, capsys):
    write(tmp_path, "names.py", '''
        def CalculateTotal():
            """Doc."""
            return 1
    ''')
    assert run_linter(tmp_path) == 1
    assert "should be lowercase" in capsys.readouterr().out


def test_detects_async_function_with_uppercase(tmp_path):
    write(tmp_path, "async_names.py", '''
        async def FetchData():
            """Doc."""
            return 1
    ''')
    assert run_linter(tmp_path) == 1


def test_private_and_dunder_names_are_not_flagged(tmp_path):
    write(tmp_path, "private.py", '''
        class Point:
            """A point."""

            def __init__(self):
                """Init."""
                self.x = 0

        def _helper():
            """Helper."""
            return 1
    ''')
    assert run_linter(tmp_path) == 0


def test_detects_missing_docstrings(tmp_path, capsys):
    write(tmp_path, "nodoc.py", '''
        class Shape:
            pass

        def area():
            return 0
    ''')
    assert run_linter(tmp_path) == 2
    assert "missing a docstring" in capsys.readouterr().out


def test_reports_syntax_errors(tmp_path, capsys):
    write(tmp_path, "broken.py", "def f(:\n    pass\n")
    assert run_linter(tmp_path) == 1
    assert "Syntax error" in capsys.readouterr().out


def test_ignores_non_python_files(tmp_path):
    (tmp_path / "notes.txt").write_text("x" * 200, encoding="utf-8")
    assert run_linter(tmp_path) == 0


def test_scans_subfolders(tmp_path):
    sub = tmp_path / "pkg"
    sub.mkdir()
    write(sub, "bad.py", "def BadName():\n    '''Doc.'''\n")
    assert run_linter(tmp_path) == 1


def test_crlf_files_are_measured_correctly(tmp_path):
    line = "x = '" + "a" * 73 + "'"  # 79 characters
    (tmp_path / "crlf.py").write_bytes((line + "\r\n").encode())
    assert run_linter(tmp_path) == 0
