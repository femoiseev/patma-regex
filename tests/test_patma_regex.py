import pytest
from patma_regex import PatmaRegex


class TestPatmaRegex:
    def test_anchored_regex(self):
        pattern = PatmaRegex("(\\w+) (\\d+)", unanchored=False)
        match "Word 123":
            case pattern(x, y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

        match "Some Word 123":
            case pattern(x, y):
                assert False
            case _:
                assert True

        match "Word 123 Some":
            case pattern(x, y):
                assert False
            case _:
                assert True
        

    def test_unanchored_regex(self):
        pattern = PatmaRegex("(\\w+) (\\d+)", unanchored=True)
        match "Word 123":
            case pattern(x, y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

        match "Some Word 123":
            case pattern(x, y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

        match "Word 123 Some":
            case pattern(x, y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

        match "Some Word 123 Some":
            case pattern(x, y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

    def test_named_groups(self):
        pattern = PatmaRegex("(?P<word>\\w+) (?P<digit>\\d+)", unanchored=False)
        match "Word 123":
            case pattern(word=x, digit=y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

        match "Word 123":
            case pattern(x, digit=y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False

        match "Word 123":
            case pattern(x, y):
                assert x == "Word"
                assert y == "123"
            case _:
                assert False
