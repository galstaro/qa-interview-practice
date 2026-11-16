"""
Tests for main.py

Run from the folder that contains main.py:
    pip install pytest
    pytest -v                 # all tests
    pytest -v -k balanced     # only tests with "balanced" in the name
    pytest -v -m smoke        # only tests marked smoke
"""
import pytest

from main import (
    is_palindrome1,
    is_palindrome2,
    word_count,
    first_unique_char,
    two_sum,
    is_balanced,
    merge_sorted,
    analyze_log,
)


# ---------------------------------------------------------------
# 1. The simplest test: a function whose name starts with test_
#    and a plain assert
# ---------------------------------------------------------------
@pytest.mark.smoke
def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_two_sum_no_solution():
    assert two_sum([1, 2], 10) is None


# ---------------------------------------------------------------
# 2. parametrize: one test, many inputs
#    each tuple = one separate test in the report
# ---------------------------------------------------------------
@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("", True),
        ("No 'x' in Nixon", True),  # apostrophe - check this one!
    ],
)
def test_is_palindrome1(text, expected):
    assert is_palindrome1(text) == expected


# You can also run the same cases on two implementations at once
@pytest.mark.parametrize("func", [is_palindrome1, is_palindrome2])
@pytest.mark.parametrize("text", ["racecar", "Was it a car or a cat I saw?"])
def test_both_palindromes_agree(func, text):
    assert func(text) is True


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()[]{}", True),
        ("{[()]}", True),
        ("(]", False),
        ("([)]", False),
        ("(((", False),  # check this one!
        ("", True),
    ],
)
def test_is_balanced(s, expected):
    assert is_balanced(s) == expected


# ---------------------------------------------------------------
# 3. fixture: preparation that several tests share
# ---------------------------------------------------------------
@pytest.fixture
def sample_log(tmp_path):
    """Creates a temporary log file and returns its path.
    tmp_path is a built-in pytest fixture: a fresh empty folder per test,
    deleted automatically afterwards."""
    content = (
        "2026-11-15 10:00:01 ERROR 10.0.0.5 Connection refused\n"
        "2026-11-15 10:00:02 INFO 10.0.0.7 Device discovered\n"
        "2026-11-15 10:00:05 WARNING 10.0.0.5 High latency\n"
        "2026-11-15 10:00:09 ERROR 10.0.0.9 Timeout\n"
    )
    log_file = tmp_path / "app.log"
    log_file.write_text(content)
    return str(log_file)


def test_analyze_log_counts_levels(sample_log):
    result = analyze_log(sample_log)
    # NOTE: when you finish analyze_log, change this to result["levels"]["ERROR"]
    assert result["ERROR"] == 2
    assert result["INFO"] == 1


def test_analyze_log_empty_file(tmp_path):
    empty = tmp_path / "empty.log"
    empty.write_text("")
    assert analyze_log(str(empty)) == {}


def test_analyze_log_broken_lines(tmp_path):
    bad = tmp_path / "bad.log"
    bad.write_text("\nthis line is broken\n")
    analyze_log(str(bad))  # should not crash


# ---------------------------------------------------------------
# 4. pytest.raises: checking that an error is raised
# ---------------------------------------------------------------
def test_analyze_log_missing_file():
    with pytest.raises(FileNotFoundError):
        analyze_log("this_file_does_not_exist.log")


# ---------------------------------------------------------------
# TODO - your turn:
#   - word_count: 3 cases with parametrize (basic, empty string, multiple spaces)
#   - first_unique_char: "swiss" -> "w", "aabbcc" -> None, "" -> None
#   - merge_sorted: 4 cases from the exercise sheet
#   - two_sum: negative numbers, the same number twice ([3, 3], 6)
# ---------------------------------------------------------------
