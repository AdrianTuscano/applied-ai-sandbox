from app import parse_tags


def test_parse_tags_basic():
    assert parse_tags("work, urgent") == ["Work", "Urgent"]


def test_parse_tags_trims_whitespace():
    assert parse_tags("  python ,  flask  ") == ["Python", "Flask"]


def test_parse_tags_capitalizes():
    assert parse_tags("AI,ml") == ["Ai", "Ml"]


def test_parse_tags_empty_string():
    assert parse_tags("") == []


def test_parse_tags_blank_entries_dropped():
    assert parse_tags(",  , ") == []


def test_parse_tags_single_tag():
    assert parse_tags("work") == ["Work"]
