"""Recommended figure widths for journals.

Widths are in inches and keyed by the number of columns spanned: ``1`` is one
column, ``2`` is two columns, ``3`` is three columns (for journals with a
three column layout). Some journals also define ``1.5``. The page width is the
widest entry, see `width`.

Rules differ between journals, even from the same publisher (and sometimes
between sister journals), so journals get their own entries. Where a stylesheet
name differs from the entry name (``apl``, ``prl``, ``optlett``, ``nature_com``),
it is an alias of the entry it shares rules with. Journal names are not case
sensitive. Take the numbers from the journal's own
author guidelines and note the source and check date in a comment next to the
entry. Widths that were derived rather than stated should say so.

Usage::

    plt.figure(figsize=(width("aps"), 3.5))
    plt.figure(figsize=(width("aps", "page"), 3.5))
"""

__all__ = ["mm2in", "width", "WIDTHS"]


def mm2in(mm):
    """Convert millimeters to inches."""
    return mm / 25.4


# Keys are lowercase, `width` lowercases the journal name before the lookup.
WIDTHS = {
    # Checked against ACS guidelines. Same widths appear in guides for other ACS
    # journals. The guide gives 2 columns as 4.167 to 7 in; 7 is the maximum.
    "acs_nano": {1: 3.33, 2: 7},
    # https://pubs.aip.org/aip/apl/pages/manuscript 2026-11-18
    "aip": {1: 3.37, 2: 6.69},
    # https://journals.aps.org/authors/style-basics 2026-11-18
    # Page states 1 column = 8.5 cm or 3 3/8 in, and allows 1.5 or 2 columns.
    # The 1.5 and 2 column widths are multiples of the column width, not stated.
    "aps": {1: 3+3/8, 1.5: 1.5*(3+3/8), 2: 2*(3+3/8)},
    # https://www.nature.com/documents/NRJs-guide-to-preparing-final-artwork.pdf 2026-11-18
    # Research and review articles: 2 column layout.
    "nature_research": {1: mm2in(88), 2: mm2in(180)},
    # Other article types: 3 column layout.
    "nature_other": {1: mm2in(58), 2: mm2in(121), 3: mm2in(185)},
    # from opticajnl.cls v1.01 geometry, derived 2026-11-18
    "optica": {1: 3.46, 2: 7.25},
    # https://www.pnas.org/pb-assets/authors/digitalart-1675347574760.pdf 2026-11-18
    "pnas": {1: 3.42, 1.5: 4.5, 2: 7.0},
}

# Convenience aliases
WIDTHS["apl"] = WIDTHS["aip"]
WIDTHS["prl"] = WIDTHS["aps"]
WIDTHS["optlett"] = WIDTHS["optica"]
# Nature Communications follows Nature, which depends on the article type.
# The stylesheet matches research and review articles, use "nature_other" for
# the other article types.
WIDTHS["nature_com"] = WIDTHS["nature_research"]


def width(journal, cols=1):
    """Recommended figure width in inches.

    Parameters
    ----------
    journal : str
        Journal name, as a key of `WIDTHS` (including aliases). Not case
        sensitive.
    cols : int, float or "page"
        Number of columns spanned. "page" gives the widest entry.
    """
    try:
        widths = WIDTHS[journal.lower()]
    except KeyError:
        raise KeyError(
            f"Unknown journal {journal!r}. Available: {sorted(WIDTHS)}"
        ) from None
    if isinstance(cols, str):
        cols = cols.lower()
    if cols == "page":
        cols = max(widths)
    try:
        return widths[cols]
    except (KeyError, TypeError):  # TypeError: unhashable `cols`
        raise KeyError(
            f"No width for {cols!r} columns in {journal!r}. "
            f"Available: {sorted(widths)} or 'page'"
        ) from None
