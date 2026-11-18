import pytest
from scistyles import journals
from scistyles.journals import mm2in, width


def test_mm2in():
    assert mm2in(25.4) == pytest.approx(1)
    assert mm2in(86) == pytest.approx(3.3858, abs=1e-4)


@pytest.fixture
def fake(monkeypatch):
    monkeypatch.setitem(journals.WIDTHS, "fake", {1: 3.0, 2: 6.0, 3: 9.0})


def test_lookup(fake):
    assert width("fake") == 3.0
    assert width("fake", 2) == 6.0


def test_page(fake):
    assert width("fake", "page") == 9.0


def test_case_insensitive(fake):
    assert width("FAKE") == 3.0
    assert width("Fake", "Page") == 9.0
    assert width("PRL") == width("prl")


def test_errors(fake):
    with pytest.raises(KeyError, match="Unknown journal"):
        width("nope")
    with pytest.raises(KeyError, match="columns"):
        width("fake", 4)
    with pytest.raises(KeyError, match="columns"):
        width("fake", [2])  # unhashable


def test_structure():
    # every journal has a one column entry, and all widths are positive
    for name, widths in journals.WIDTHS.items():
        assert 1 in widths, name
        assert all(w > 0 for w in widths.values()), name


def test_known_values():
    assert width("aps") == pytest.approx(3.375)
    assert width("aps", "page") == pytest.approx(6.75)
    assert width("pnas", 1.5) == pytest.approx(4.5)
    assert width("nature_research", 2) == pytest.approx(mm2in(180))
    assert width("nature_other", "page") == pytest.approx(mm2in(185))


def test_aliases():
    for alias, target in [
        ("apl", "aip"),
        ("prl", "aps"),
        ("optlett", "optica"),
        ("nature_com", "nature_research"),
    ]:
        assert journals.WIDTHS[alias] is journals.WIDTHS[target], alias
