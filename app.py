
"""
The Mountain Path Academy — Finance Excel Functions Dashboard
Searchable & filterable reference for financial analysts
Prof. V. Ravichandran | themountainpathacademy.com
"""

import streamlit as st
import pandas as pd

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Excel Finance Functions | The Mountain Path Academy",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── BRANDING & CSS ───────────────────────────────────────────────────────────
# st.html() is required for Streamlit ≥ 1.36 — unsafe_allow_html is deprecated
st.html("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Root palette (Mountain Path Academy) ── */
:root {
    --navy:      #0D1B3E;
    --navy-mid:  #162552;
    --gold:      #C8962E;
    --gold-lt:   #E8B84B;
    --slate:     #2C3E6B;
    --cream:     #F8F5EF;
    --white:     #FFFFFF;
    --muted:     #8A94AB;
    --success:   #27AE60;
    --warn:      #E67E22;
    --danger:    #C0392B;
    --text:      #1C2333;
    --border:    #DDE2ED;
}

/* ── App background ── */
.stApp { background: var(--cream); }
section[data-testid="stSidebar"] { background: var(--navy) !important; }
section[data-testid="stSidebar"] * { color: #D4DAE8 !important; }
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stMultiSelect label,
section[data-testid="stSidebar"] .stTextInput label { color: var(--gold-lt) !important; font-weight: 600 !important; }
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 { color: var(--gold-lt) !important; }

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, var(--navy) 0%, var(--slate) 100%);
    border-radius: 16px;
    padding: 36px 44px;
    margin-bottom: 28px;
    border-left: 6px solid var(--gold);
    box-shadow: 0 8px 32px rgba(13,27,62,0.18);
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    color: var(--white);
    font-size: 2.05rem;
    margin: 0 0 6px 0;
    letter-spacing: -0.3px;
}
.hero p { color: #B0BCDA; font-size: 0.95rem; margin: 0; line-height: 1.6; }
.hero .gold { color: var(--gold-lt); font-weight: 600; }

/* ── Stat chips ── */
.stat-row { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; }
.stat-chip {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--navy);
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
}
.stat-chip span { color: var(--gold); font-size: 1.15rem; }

/* ── Category badge ── */
.cat-badge {
    display: inline-block;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.4px;
    text-transform: uppercase;
}
.cat-Core\ Math        { background:#EBF5FF; color:#1565C0; }
.cat-Conditional       { background:#FFF3E0; color:#E65100; }
.cat-Lookup            { background:#F3E5F5; color:#6A1B9A; }
.cat-Date\ &\ Time     { background:#E8F5E9; color:#1B5E20; }
.cat-Financial         { background:#FCE4EC; color:#880E4F; }
.cat-Statistical       { background:#E0F2F1; color:#004D40; }
.cat-Text              { background:#FFF9C4; color:#827717; }
.cat-Dynamic\ Arrays   { background:#E8EAF6; color:#283593; }
.cat-Error\ &\ Info    { background:#FFEBEE; color:#B71C1C; }
.cat-Math\ Extras      { background:#F1F8E9; color:#33691E; }
.cat-Info\ &\ Cell     { background:#E0F7FA; color:#006064; }

/* ── Difficulty badge ── */
.diff-Beginner     { background:#E8F5E9; color:#2E7D32; border:1px solid #A5D6A7; }
.diff-Intermediate { background:#FFF3E0; color:#E65100; border:1px solid #FFCC80; }
.diff-Advanced     { background:#FCE4EC; color:#880E4F; border:1px solid #F48FB1; }

/* ── Function card ── */
.fn-card {
    background: var(--white);
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
    border: 1px solid var(--border);
    box-shadow: 0 2px 10px rgba(0,0,0,0.055);
    transition: box-shadow 0.2s;
}
.fn-card:hover { box-shadow: 0 6px 20px rgba(13,27,62,0.12); border-color: #B0BCDA; }
.fn-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    color: var(--navy);
    font-weight: 700;
    margin-bottom: 4px;
}
.fn-syntax {
    font-family: 'Courier New', monospace;
    background: #EEF1F8;
    color: var(--slate);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.85rem;
    border-left: 3px solid var(--gold);
    margin: 10px 0;
    word-break: break-all;
}
.fn-desc { font-size: 0.9rem; color: var(--text); line-height: 1.55; }
.fn-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin-top: 12px;
    margin-bottom: 4px;
}
.fn-usecase {
    background: linear-gradient(135deg, #F0F4FF 0%, #F8F5EF 100%);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 0.86rem;
    color: var(--navy-mid);
    line-height: 1.5;
    border-left: 3px solid var(--gold);
}
.fn-tip {
    background: #FFFDE7;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 0.84rem;
    color: #5D4037;
    line-height: 1.5;
    border-left: 3px solid #FBC02D;
}
.fn-tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 10px; }
.tag {
    background: #EEF1F8;
    color: var(--slate);
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 0.73rem;
    font-weight: 600;
}

/* ── Section header ── */
.section-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: var(--navy);
    border-bottom: 2px solid var(--gold);
    padding-bottom: 8px;
    margin: 24px 0 16px 0;
    font-weight: 700;
}

/* ── No results ── */
.no-result {
    text-align: center;
    padding: 60px 20px;
    color: var(--muted);
    font-size: 1rem;
}
.no-result .icon { font-size: 2.5rem; margin-bottom: 12px; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 24px;
    color: var(--muted);
    font-size: 0.8rem;
    border-top: 1px solid var(--border);
    margin-top: 40px;
}
.footer a { color: var(--gold); text-decoration: none; }

/* ── Streamlit overrides — main area ── */
div[data-testid="stTextInput"] input {
    border-radius: 10px !important;
    border: 1.5px solid var(--border) !important;
    padding: 10px 14px !important;
    font-size: 0.95rem !important;
    background: var(--white) !important;
    color: var(--text) !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(200,150,46,0.15) !important;
}
/* ── Sidebar search input — fix invisible text on dark bg ── */
section[data-testid="stSidebar"] div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.10) !important;
    color: #FFFFFF !important;
    border: 1.5px solid rgba(232,184,75,0.4) !important;
    caret-color: #E8B84B !important;
}
section[data-testid="stSidebar"] div[data-testid="stTextInput"] input::placeholder {
    color: rgba(255,255,255,0.40) !important;
}
section[data-testid="stSidebar"] div[data-testid="stTextInput"] input:focus {
    background: rgba(255,255,255,0.15) !important;
    border-color: var(--gold-lt) !important;
    box-shadow: 0 0 0 3px rgba(232,184,75,0.18) !important;
}
/* ── Sidebar profile links ── */
.profile-links { display:flex; gap:12px; justify-content:center; margin-top:12px; }
.profile-link {
    display:inline-flex; align-items:center; gap:6px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(232,184,75,0.3);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 0.72rem;
    font-weight: 600;
    color: #E8B84B !important;
    text-decoration: none !important;
    transition: background 0.2s;
}
.profile-link:hover { background: rgba(232,184,75,0.18) !important; }
/* ── Category icon strip ── */
.cat-icon-row {
    display:flex; gap:10px; flex-wrap:wrap; margin-bottom:20px;
}
.cat-icon-chip {
    display:inline-flex; align-items:center; gap:6px;
    background: var(--white);
    border:1px solid var(--border);
    border-radius:10px;
    padding:7px 14px;
    font-size:0.78rem;
    font-weight:600;
    color: var(--navy);
    box-shadow:0 1px 4px rgba(0,0,0,0.06);
    cursor:pointer;
}
</style>
""")


# ─── DATA ─────────────────────────────────────────────────────────────────────
FUNCTIONS = [
    # ── CORE MATH ──
    {
        "name": "SUM", "category": "Core Math", "difficulty": "Beginner",
        "syntax": "=SUM(range)",
        "description": "Adds all numbers in a range.",
        "use_case": "FP&A: Total revenue or expense line items in a P&L model across multiple periods.",
        "tip": "⚠️ Watch out for text-formatted numbers — SUM silently skips them. Use VALUE() to convert first.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "AVERAGE", "category": "Core Math", "difficulty": "Beginner",
        "syntax": "=AVERAGE(range)",
        "description": "Returns the arithmetic mean of a range of numbers.",
        "use_case": "FP&A: Calculate average monthly revenue or average EBITDA margin over trailing 12 months.",
        "tip": "⚠️ AVERAGE ignores blanks but includes zeros. Use AVERAGEIF to exclude zero-revenue months.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "MIN / MAX", "category": "Core Math", "difficulty": "Beginner",
        "syntax": "=MIN(range)  /  =MAX(range)",
        "description": "Returns the smallest or largest value in a range.",
        "use_case": "Valuations: Find the floor/ceiling interest rate in a sensitivity table; flag covenant breach levels.",
        "tip": "⚠️ Text cells are ignored — MINA/MAXA count them as 0 instead.",
        "applications": ["FP&A", "Valuations", "Reporting"],
    },
    {
        "name": "MEDIAN", "category": "Core Math", "difficulty": "Beginner",
        "syntax": "=MEDIAN(range)",
        "description": "Returns the middle value of a dataset.",
        "use_case": "Reporting: Median deal size in an M&A pipeline avoids distortion from mega-deals.",
        "tip": "⚠️ Unlike AVERAGE, MEDIAN is resistant to outliers — prefer it for skewed distributions like deal values.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "ROUND / ROUNDUP / ROUNDDOWN", "category": "Core Math", "difficulty": "Beginner",
        "syntax": "=ROUND(num, digits)  /  =ROUNDUP(num, digits)  /  =ROUNDDOWN(num, digits)",
        "description": "Rounds a number to specified decimal places. ROUNDUP always away from zero; ROUNDDOWN always toward zero.",
        "use_case": "FP&A: Round EPS to 2 decimals in earnings models; round tax provisions up to the nearest rupee.",
        "tip": "⚠️ Never ROUND intermediate calculations — only round final outputs to avoid compounding errors.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "ABS", "category": "Core Math", "difficulty": "Beginner",
        "syntax": "=ABS(number)",
        "description": "Returns the absolute (positive) value of a number.",
        "use_case": "Risk: Calculate absolute deviation of actual vs. budget; compute absolute drawdown from peak NAV.",
        "tip": "⚠️ Combine with IF for sign-aware comparisons: =IF(ABS(variance)>threshold, \"Alert\", \"OK\").",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "SUMPRODUCT", "category": "Core Math", "difficulty": "Intermediate",
        "syntax": "=SUMPRODUCT(array1, array2, ...)",
        "description": "Multiplies corresponding elements across arrays, then sums all products.",
        "use_case": "FP&A: Weighted-average cost of capital (WACC) — multiply each tranche weight by its cost; portfolio revenue = price × units across SKUs.",
        "tip": "⚠️ All arrays must be the same size. Use double-negatives (--) to convert TRUE/FALSE to 1/0 in filtered SUMPRODUCTs.",
        "applications": ["FP&A", "Valuations"],
    },

    # ── CONDITIONAL ANALYSIS ──
    {
        "name": "IF", "category": "Conditional", "difficulty": "Beginner",
        "syntax": "=IF(logical_test, value_if_true, value_if_false)",
        "description": "Returns one of two values based on whether a condition is TRUE or FALSE.",
        "use_case": "Valuations: Toggle between DCF and comparables output based on a model-switch cell; flag negative EBITDA companies.",
        "tip": "⚠️ Deep nesting (IF inside IF) is hard to audit. Use IFS or SWITCH for 3+ conditions.",
        "applications": ["FP&A", "Valuations", "Reporting"],
    },
    {
        "name": "IFS", "category": "Conditional", "difficulty": "Intermediate",
        "syntax": "=IFS(test1, val1, test2, val2, ...)",
        "description": "Tests multiple conditions in sequence; returns the value for the first TRUE condition.",
        "use_case": "FP&A: Assign revenue tier labels (Tier 1/2/3) based on revenue brackets in a customer segmentation model.",
        "tip": "⚠️ Always end with a TRUE, 'default' pair — otherwise IFS returns #N/A when no condition matches.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "AND / OR", "category": "Conditional", "difficulty": "Beginner",
        "syntax": "=AND(cond1, cond2, ...)  /  =OR(cond1, cond2, ...)",
        "description": "AND returns TRUE only if all conditions are met. OR returns TRUE if any condition is met.",
        "use_case": "Risk: Flag a loan for review if AND(LTV > 80%, DSCR < 1.2x); highlight any covenant breach using OR.",
        "tip": "⚠️ AND/OR do not short-circuit in Excel — all arguments are evaluated even if the first resolves the result.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "IFERROR", "category": "Conditional", "difficulty": "Beginner",
        "syntax": "=IFERROR(value, value_if_error)",
        "description": "Returns an alternative value if the expression produces any error (#DIV/0!, #N/A, etc.).",
        "use_case": "Reporting: Wrap VLOOKUP in IFERROR so missing tickers display 'N/A' instead of breaking the model.",
        "tip": "⚠️ IFERROR silences ALL errors — it may hide genuine formula mistakes. Use IFNA for lookup-only safety.",
        "applications": ["FP&A", "Valuations", "Reporting"],
    },
    {
        "name": "IFNA", "category": "Conditional", "difficulty": "Beginner",
        "syntax": "=IFNA(value, value_if_na)",
        "description": "Catches only #N/A errors, leaving all other errors visible.",
        "use_case": "Reporting: Wrap XLOOKUP with IFNA to catch missing reference data while surfacing genuine formula errors.",
        "tip": "⚠️ Prefer IFNA over IFERROR for lookups — it's safer because only #N/A is suppressed.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "SUMIF / SUMIFS", "category": "Conditional", "difficulty": "Intermediate",
        "syntax": "=SUMIF(range, criteria, sum_range)  /  =SUMIFS(sum_range, range1, crit1, ...)",
        "description": "SUMIF sums cells matching one condition; SUMIFS handles multiple conditions simultaneously.",
        "use_case": "FP&A: Sum revenue for a specific BU and region in a multi-dimensional P&L; sum capex by project type.",
        "tip": "⚠️ In SUMIFS the sum_range is the FIRST argument (opposite of SUMIF). Wildcard * works in text criteria.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "COUNTIF / COUNTIFS", "category": "Conditional", "difficulty": "Intermediate",
        "syntax": "=COUNTIF(range, criteria)  /  =COUNTIFS(range1, crit1, range2, crit2, ...)",
        "description": "COUNTIF counts cells meeting one condition; COUNTIFS counts on multiple simultaneous conditions.",
        "use_case": "Reporting: Count deals above a valuation threshold by deal type in an M&A pipeline tracker.",
        "tip": "⚠️ Text criteria must be in quotes: =COUNTIF(A:A,\">0\") not =COUNTIF(A:A,>0).",
        "applications": ["FP&A", "Reporting"],
    },

    # ── LOOKUP & REFERENCE ──
    {
        "name": "XLOOKUP", "category": "Lookup", "difficulty": "Intermediate",
        "syntax": "=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])",
        "description": "Modern replacement for VLOOKUP — searches any column/row, returns any column, handles not-found natively.",
        "use_case": "Valuations: Pull EV/EBITDA multiples for a target company from a comps table without column-counting.",
        "tip": "⚠️ Requires Excel 365/2021+. The [if_not_found] arg replaces IFERROR wrapping. Default is exact match.",
        "applications": ["FP&A", "Valuations", "Reporting"],
    },
    {
        "name": "VLOOKUP", "category": "Lookup", "difficulty": "Beginner",
        "syntax": "=VLOOKUP(lookup_value, table_array, col_index_num, FALSE)",
        "description": "Searches the leftmost column of a table and returns a value from a specified column to the right.",
        "use_case": "FP&A: Map account codes to cost-centre names in a chart of accounts; pull FX rates by currency code.",
        "tip": "⚠️ Always use FALSE (exact match). Inserting columns shifts col_index — prefer INDEX+MATCH or XLOOKUP instead.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "INDEX + MATCH", "category": "Lookup", "difficulty": "Intermediate",
        "syntax": "=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))",
        "description": "Classic two-function combo: MATCH finds the position, INDEX returns the value. Works in any direction.",
        "use_case": "Valuations: Two-way lookup — find the IRR in a sensitivity matrix by matching both the entry multiple row and exit multiple column.",
        "tip": "⚠️ The 0 in MATCH is critical for exact match. Wrap in IFERROR for cleaner output when the key is missing.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "MATCH / XMATCH", "category": "Lookup", "difficulty": "Intermediate",
        "syntax": "=MATCH(lookup_value, lookup_array, 0)  /  =XMATCH(lookup_value, lookup_array)",
        "description": "Returns the relative position (row or column number) of a value within a range.",
        "use_case": "FP&A: Find which year column a specific budget period falls in to dynamically reference it in formulas.",
        "tip": "⚠️ MATCH returns position, not value. XMATCH supports wildcard and binary search modes not available in MATCH.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "OFFSET", "category": "Lookup", "difficulty": "Advanced",
        "syntax": "=OFFSET(reference, rows, cols, [height], [width])",
        "description": "Returns a cell or range offset from a starting reference by a given number of rows and columns.",
        "use_case": "FP&A: Build dynamic named ranges that expand automatically as new periods are added to a rolling forecast.",
        "tip": "⚠️ OFFSET is volatile — it recalculates on every change, slowing large models. Use INDEX where possible.",
        "applications": ["FP&A"],
    },
    {
        "name": "INDIRECT", "category": "Lookup", "difficulty": "Advanced",
        "syntax": "=INDIRECT(ref_text, [a1])",
        "description": "Converts a text string into a live cell or range reference.",
        "use_case": "Reporting: Dynamically reference a different sheet tab (e.g., by month name stored in a cell) in a consolidated report.",
        "tip": "⚠️ INDIRECT is volatile (like OFFSET). Also, it breaks when sheets are renamed — use INDEX+MATCH as a stable alternative.",
        "applications": ["Reporting"],
    },
    {
        "name": "CHOOSE", "category": "Lookup", "difficulty": "Intermediate",
        "syntax": "=CHOOSE(index_num, value1, value2, ...)",
        "description": "Returns a value from a list based on an index number (1 to 254).",
        "use_case": "Valuations: Build scenario toggles — CHOOSE(scenario_switch, bear_case, base_case, bull_case) to flip between DCF assumptions.",
        "tip": "⚠️ Index must be 1 to N. Using 0 or >N returns #VALUE! — add data validation to the toggle cell.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "ADDRESS", "category": "Lookup", "difficulty": "Advanced",
        "syntax": "=ADDRESS(row_num, col_num, [abs_num], [a1])",
        "description": "Constructs a cell address as text from row and column numbers.",
        "use_case": "Reporting: Dynamically build references for use with INDIRECT in automated report generators.",
        "tip": "⚠️ ADDRESS returns text, not a value. Combine with INDIRECT to make it a live reference.",
        "applications": ["Reporting"],
    },

    # ── DATE & TIME ──
    {
        "name": "TODAY / NOW", "category": "Date & Time", "difficulty": "Beginner",
        "syntax": "=TODAY()  /  =NOW()",
        "description": "TODAY() returns the current date; NOW() returns the current date and time. Both update automatically.",
        "use_case": "Reporting: Stamp dashboards with 'Data as of [TODAY()]'; calculate days since last report.",
        "tip": "⚠️ Both are volatile — they recalculate on every sheet change. Freeze with Ctrl+Shift+; to hard-code a static date.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "DATE / YEAR / MONTH / DAY", "category": "Date & Time", "difficulty": "Beginner",
        "syntax": "=DATE(year, month, day)  /  =YEAR(date)  /  =MONTH(date)  /  =DAY(date)",
        "description": "DATE builds a date from components; YEAR/MONTH/DAY extract those components from a date.",
        "use_case": "FP&A: Construct period-end dates dynamically in a rolling 12-month model using =DATE(YEAR(start)+1, MONTH(start), 0).",
        "tip": "⚠️ DATE(2024, 13, 1) rolls to Feb 2025 — Excel normalises out-of-range months, which is useful for period math.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "EOMONTH", "category": "Date & Time", "difficulty": "Intermediate",
        "syntax": "=EOMONTH(start_date, months)",
        "description": "Returns the last day of the month a specified number of months before or after a date.",
        "use_case": "FP&A: Generate quarter-end or year-end dates in a budget model; calculate bond maturity dates.",
        "tip": "⚠️ =EOMONTH(date, 0) gives current month-end; =EOMONTH(date, -1)+1 gives the first day of the current month.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "EDATE", "category": "Date & Time", "difficulty": "Intermediate",
        "syntax": "=EDATE(start_date, months)",
        "description": "Returns a date exactly N months before or after a given date.",
        "use_case": "Valuations: Calculate loan maturity, bond coupon dates, or option expiry by advancing from issue date.",
        "tip": "⚠️ Unlike adding 30 days, EDATE respects month-end — March 31 + 1 month = April 30, not May 1.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "NETWORKDAYS", "category": "Date & Time", "difficulty": "Intermediate",
        "syntax": "=NETWORKDAYS(start_date, end_date, [holidays])",
        "description": "Counts working days between two dates, excluding weekends and optional holidays.",
        "use_case": "FP&A: Calculate settlement periods (T+2), SLA tracking days, or project timelines excluding weekends.",
        "tip": "⚠️ Both start and end dates are inclusive. Pass a holiday list to get accurate business-day counts.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "YEARFRAC", "category": "Date & Time", "difficulty": "Advanced",
        "syntax": "=YEARFRAC(start_date, end_date, [basis])",
        "description": "Returns the fraction of a year between two dates using various day-count conventions.",
        "use_case": "Valuations: Accurate interest accrual in bond pricing (Act/360, Act/365); pro-rate fees in M&A models.",
        "tip": "⚠️ Basis matters: 0=US(30/360), 1=Actual/Actual, 3=Actual/365. Wrong basis = systematic pricing error.",
        "applications": ["Valuations"],
    },

    # ── FINANCIAL MODELING ──
    {
        "name": "PV", "category": "Financial", "difficulty": "Intermediate",
        "syntax": "=PV(rate, nper, pmt, [fv], [type])",
        "description": "Calculates the present value of a stream of equal periodic payments at a constant rate.",
        "use_case": "Valuations: Value an annuity stream; compute the present value of lease obligations under IFRS 16.",
        "tip": "⚠️ Cash outflows must be negative. Rate and nper must match periods (monthly loan: rate=APR/12, nper=years×12).",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "FV", "category": "Financial", "difficulty": "Intermediate",
        "syntax": "=FV(rate, nper, pmt, [pv], [type])",
        "description": "Calculates the future value of an investment with periodic equal payments at a constant rate.",
        "use_case": "FP&A: Project a pension fund balance or sinking fund; model compound growth of a retained-earnings reserve.",
        "tip": "⚠️ Contributions are negative (cash out). Mix signs carefully: =FV(rate, nper, -payment, -initial_pv).",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "PMT", "category": "Financial", "difficulty": "Intermediate",
        "syntax": "=PMT(rate, nper, pv, [fv], [type])",
        "description": "Calculates the fixed periodic payment required to fully amortise a loan.",
        "use_case": "FP&A: Build a debt-service schedule for a term loan; calculate EMI for a capital expenditure financing plan.",
        "tip": "⚠️ PMT returns a negative (outflow). Negate it with -PMT(...) when displaying as a positive repayment amount.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "IPMT / PPMT", "category": "Financial", "difficulty": "Advanced",
        "syntax": "=IPMT(rate, per, nper, pv)  /  =PPMT(rate, per, nper, pv)",
        "description": "IPMT returns the interest component of a specific loan payment; PPMT returns the principal component.",
        "use_case": "FP&A: Build a fully amortising loan schedule showing the split between interest expense (P&L) and principal (balance sheet) for each period.",
        "tip": "⚠️ Check: IPMT + PPMT = PMT for every period. If not, your rate/nper periods are mismatched.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "NPV", "category": "Financial", "difficulty": "Intermediate",
        "syntax": "=NPV(rate, value1, value2, ...)",
        "description": "Discounts a series of equally-spaced future cash flows to present value at a given rate.",
        "use_case": "Valuations: Quick DCF check — but remember NPV assumes Year 1 flows arrive at end of period 1.",
        "tip": "⚠️ NPV does NOT include the initial investment. Structure: =NPV(rate, CF1:CFn) + CF0 (CF0 is negative).",
        "applications": ["Valuations"],
    },
    {
        "name": "XNPV", "category": "Financial", "difficulty": "Advanced",
        "syntax": "=XNPV(rate, values, dates)",
        "description": "Discounts irregular cash flows at exact actual dates — far more accurate than NPV for real-world projects.",
        "use_case": "Valuations: Value a project with milestone-based cash flows (construction, ramp-up, steady-state) at irregular intervals rather than assuming year-end timing.",
        "tip": "⚠️ First value must be the initial investment on Day 0. Dates must be in ascending order.",
        "applications": ["Valuations"],
    },
    {
        "name": "IRR", "category": "Financial", "difficulty": "Intermediate",
        "syntax": "=IRR(values, [guess])",
        "description": "Finds the discount rate that makes the NPV of an equally-spaced cash flow series equal to zero.",
        "use_case": "Valuations: Compute IRR on a PE fund's J-curve; benchmark project returns against WACC hurdle rate.",
        "tip": "⚠️ Multiple sign changes in cash flows produce multiple IRRs — use XIRR or MIRR for complex profiles.",
        "applications": ["Valuations"],
    },
    {
        "name": "XIRR", "category": "Financial", "difficulty": "Advanced",
        "syntax": "=XIRR(values, dates, [guess])",
        "description": "Calculates IRR for cash flows at irregular (non-periodic) dates — the industry standard for PE/VC returns.",
        "use_case": "Valuations: Calculate PE fund IRR from actual investment and distribution dates rather than assuming quarterly intervals.",
        "tip": "⚠️ #NUM! means no convergence — try a guess value (e.g., 0.1). Ensure at least one positive and one negative flow.",
        "applications": ["Valuations"],
    },
    {
        "name": "RATE", "category": "Financial", "difficulty": "Advanced",
        "syntax": "=RATE(nper, pmt, pv, [fv], [type], [guess])",
        "description": "Finds the implied periodic interest rate of an annuity.",
        "use_case": "Valuations: Back out the implied yield on a bond; solve for the financing rate implied by lease payments.",
        "tip": "⚠️ RATE iterates to a solution — add a guess if it returns #NUM!. Check: result × nper periods = total cost of borrowing.",
        "applications": ["Valuations"],
    },
    {
        "name": "SLN", "category": "Financial", "difficulty": "Beginner",
        "syntax": "=SLN(cost, salvage, life)",
        "description": "Calculates straight-line depreciation per period.",
        "use_case": "FP&A: Build the depreciation schedule for PP&E in a 3-statement model using straight-line method.",
        "tip": "⚠️ SLN gives the same charge every period — if assets are acquired mid-year, pro-rate by months in service.",
        "applications": ["FP&A"],
    },
    {
        "name": "DB / DDB / SYD", "category": "Financial", "difficulty": "Advanced",
        "syntax": "=DB(cost, salvage, life, period)  /  =DDB(...)  /  =SYD(cost, salvage, life, period)",
        "description": "Accelerated depreciation methods: DB (fixed declining rate), DDB (double declining), SYD (sum-of-years'-digits).",
        "use_case": "FP&A: Model accelerated depreciation for tax planning; compare after-tax NPV across depreciation methods for capex decisions.",
        "tip": "⚠️ DDB can depreciate below salvage value — use MIN(DDB, book_value - salvage) to cap it correctly.",
        "applications": ["FP&A", "Valuations"],
    },

    # ── STATISTICAL ──
    {
        "name": "COUNT / COUNTA", "category": "Statistical", "difficulty": "Beginner",
        "syntax": "=COUNT(range)  /  =COUNTA(range)",
        "description": "COUNT counts cells with numbers; COUNTA counts all non-empty cells.",
        "use_case": "Reporting: Count the number of active deals in a pipeline (COUNTA) or periods with reported revenue (COUNT).",
        "tip": "⚠️ COUNT ignores text and blanks. A cell with a space or apostrophe will be counted by COUNTA but not COUNT.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "STDEV.S / STDEV.P", "category": "Statistical", "difficulty": "Intermediate",
        "syntax": "=STDEV.S(range)  /  =STDEV.P(range)",
        "description": "STDEV.S estimates standard deviation from a sample; STDEV.P calculates it for an entire population.",
        "use_case": "Risk: Calculate the volatility of asset returns for VaR estimation; measure earnings variability for credit analysis.",
        "tip": "⚠️ For market return analysis always use STDEV.S (sample). STDEV.P understates volatility for small datasets.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "PERCENTILE.INC / QUARTILE.INC", "category": "Statistical", "difficulty": "Intermediate",
        "syntax": "=PERCENTILE.INC(range, k)  /  =QUARTILE.INC(range, quart)",
        "description": "PERCENTILE returns the value at the kth percentile (0 to 1); QUARTILE returns Q0 through Q4.",
        "use_case": "Risk: Calculate 95th-percentile credit loss for stress testing; report median and interquartile revenue range.",
        "tip": "⚠️ PERCENTILE.INC vs .EXC: INC includes 0 and 1 (min/max), EXC excludes them — use INC unless told otherwise.",
        "applications": ["Valuations", "Reporting"],
    },
    {
        "name": "CORREL / SLOPE", "category": "Statistical", "difficulty": "Advanced",
        "syntax": "=CORREL(array1, array2)  /  =SLOPE(known_y's, known_x's)",
        "description": "CORREL measures linear correlation between two datasets (−1 to +1); SLOPE calculates the regression coefficient.",
        "use_case": "Valuations: Calculate beta (slope of stock returns vs. market); measure correlation between revenue drivers for scenario planning.",
        "tip": "⚠️ Correlation ≠ causation. Always plot the data first — CORREL can give misleading results for non-linear relationships.",
        "applications": ["Valuations"],
    },
    {
        "name": "RANK.EQ / LARGE / SMALL", "category": "Statistical", "difficulty": "Beginner",
        "syntax": "=RANK.EQ(number, ref)  /  =LARGE(array, k)  /  =SMALL(array, k)",
        "description": "Rank a value in a list; LARGE/SMALL return the kth largest or smallest value.",
        "use_case": "FP&A: Rank sales reps by revenue; identify top-3 and bottom-3 performing products in a portfolio.",
        "tip": "⚠️ RANK.EQ assigns the same rank to ties — use RANK.AVG if you need averaged ranks for statistical purposes.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "FORECAST.LINEAR", "category": "Statistical", "difficulty": "Intermediate",
        "syntax": "=FORECAST.LINEAR(x, known_y's, known_x's)",
        "description": "Predicts a future value based on a linear trend in historical data.",
        "use_case": "FP&A: Project next quarter's revenue based on historical trend; extrapolate headcount from hiring run-rate.",
        "tip": "⚠️ FORECAST.LINEAR assumes linearity. For seasonal data use FORECAST.ETS (exponential smoothing) instead.",
        "applications": ["FP&A"],
    },

    # ── TEXT ──
    {
        "name": "TRIM / LEN", "category": "Text", "difficulty": "Beginner",
        "syntax": "=TRIM(text)  /  =LEN(text)",
        "description": "TRIM removes leading, trailing, and extra internal spaces; LEN counts characters.",
        "use_case": "Reporting: Clean company names imported from ERP before VLOOKUP — mismatched spaces cause silent lookup failures.",
        "tip": "⚠️ TRIM removes normal spaces but NOT non-breaking spaces (CHAR(160)) common in web-scraped data. Use SUBSTITUTE(TRIM(A1),CHAR(160),\"\") for full cleaning.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "LEFT / RIGHT / MID", "category": "Text", "difficulty": "Beginner",
        "syntax": "=LEFT(text, n)  /  =RIGHT(text, n)  /  =MID(text, start, n)",
        "description": "Extract characters from the left, right, or middle of a text string.",
        "use_case": "Reporting: Extract cost-centre code from an account string; parse year from a period label like '2024-Q3'.",
        "tip": "⚠️ Always pair with LEN and FIND/SEARCH for variable-length strings rather than hardcoding character counts.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "FIND / SEARCH", "category": "Text", "difficulty": "Intermediate",
        "syntax": "=FIND(find_text, within_text, [start])  /  =SEARCH(find_text, within_text, [start])",
        "description": "Both return the character position of a substring. FIND is case-sensitive; SEARCH supports wildcards.",
        "use_case": "Reporting: Locate the delimiter in a composite key (e.g., 'CC-1234') to split it with LEFT/MID.",
        "tip": "⚠️ Both return #VALUE! if the text isn't found — wrap in IFERROR to handle mismatches gracefully.",
        "applications": ["Reporting"],
    },
    {
        "name": "SUBSTITUTE / REPLACE", "category": "Text", "difficulty": "Intermediate",
        "syntax": "=SUBSTITUTE(text, old, new, [instance])  /  =REPLACE(text, start, n, new)",
        "description": "SUBSTITUTE replaces all occurrences of a substring; REPLACE replaces text at a known position.",
        "use_case": "Reporting: Standardise currency symbols in imported data; strip special characters from account codes.",
        "tip": "⚠️ SUBSTITUTE is case-sensitive. Use the [instance] argument to replace only the Nth occurrence.",
        "applications": ["Reporting"],
    },
    {
        "name": "TEXTJOIN", "category": "Text", "difficulty": "Intermediate",
        "syntax": "=TEXTJOIN(delimiter, ignore_empty, text1, text2, ...)",
        "description": "Concatenates text values with a specified delimiter, optionally ignoring empty cells.",
        "use_case": "Reporting: Build a comma-separated list of deal conditions or investor names from a column of values.",
        "tip": "⚠️ Set ignore_empty to TRUE to avoid double-delimiter issues when some cells are blank.",
        "applications": ["Reporting"],
    },
    {
        "name": "TEXT", "category": "Text", "difficulty": "Intermediate",
        "syntax": "=TEXT(value, format_text)",
        "description": "Converts a number to formatted text using Excel format codes (currency, date, percentage, etc.).",
        "use_case": "Reporting: Format EPS as '$0.00' or date as 'MMM-YY' for dynamic labels in dashboard headers.",
        "tip": "⚠️ TEXT returns text — you cannot do arithmetic on the result. Never use TEXT on a value you'll sum later.",
        "applications": ["Reporting"],
    },
    {
        "name": "VALUE", "category": "Text", "difficulty": "Beginner",
        "syntax": "=VALUE(text)",
        "description": "Converts a number stored as text into an actual numeric value.",
        "use_case": "FP&A: Convert text-formatted revenue figures imported from a PDF or ERP extract before summing them.",
        "tip": "⚠️ If the text contains non-numeric characters (like spaces or currency symbols) VALUE returns #VALUE!. Clean with SUBSTITUTE first.",
        "applications": ["FP&A", "Reporting"],
    },

    # ── DYNAMIC ARRAYS ──
    {
        "name": "UNIQUE", "category": "Dynamic Arrays", "difficulty": "Intermediate",
        "syntax": "=UNIQUE(array, [by_col], [exactly_once])",
        "description": "Returns a list of distinct values from a range — spills results automatically.",
        "use_case": "Reporting: Extract unique cost centres, product lines, or regions from a transaction list for a dynamic summary table.",
        "tip": "⚠️ Leave adjacent cells below UNIQUE empty — the spill range will error if any cell in it is occupied.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "FILTER", "category": "Dynamic Arrays", "difficulty": "Intermediate",
        "syntax": "=FILTER(array, include, [if_empty])",
        "description": "Returns only the rows (or columns) that meet a condition — spills the filtered results.",
        "use_case": "Reporting: Dynamically show only 'Won' deals above a deal-size threshold from a pipeline table.",
        "tip": "⚠️ Always supply [if_empty] (e.g., 'No results') to avoid #CALC! errors when no rows match.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "SORT / SORTBY", "category": "Dynamic Arrays", "difficulty": "Intermediate",
        "syntax": "=SORT(array, [sort_index], [sort_order])  /  =SORTBY(array, by_array1, [order1], ...)",
        "description": "SORT sorts a range by its own column; SORTBY sorts one range by another helper range.",
        "use_case": "Reporting: Rank portfolio companies by descending EBITDA margin in a dashboard table — auto-updates as data changes.",
        "tip": "⚠️ SORT doesn't sort in place — it spills a copy. The original data is unchanged.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "SEQUENCE", "category": "Dynamic Arrays", "difficulty": "Intermediate",
        "syntax": "=SEQUENCE(rows, [cols], [start], [step])",
        "description": "Generates an array of sequential numbers — spills automatically.",
        "use_case": "FP&A: Generate period numbers (1 to 60) for a 5-year monthly model without manual entry.",
        "tip": "⚠️ Use =SEQUENCE(1,12,1,1) to create a horizontal row of months; wrap in DATE() to make real dates.",
        "applications": ["FP&A"],
    },
    {
        "name": "LET", "category": "Dynamic Arrays", "difficulty": "Advanced",
        "syntax": "=LET(name1, value1, [name2, value2, ...], calculation)",
        "description": "Assigns intermediate calculation results to named variables for reuse within a single formula.",
        "use_case": "Valuations: Compute WACC once inside a LET and reuse it multiple times in a complex DCF formula without repeated logic.",
        "tip": "⚠️ LET names are local to the formula — they don't conflict with named ranges. Debug by evaluating inner names step by step.",
        "applications": ["Valuations", "FP&A"],
    },
    {
        "name": "LAMBDA", "category": "Dynamic Arrays", "difficulty": "Advanced",
        "syntax": "=LAMBDA(parameter1, [parameter2, ...], calculation)",
        "description": "Creates a reusable custom function without VBA — call it as a Named Range from anywhere in the workbook.",
        "use_case": "FP&A: Define a custom WACC or EBITDA-bridge function once (via Name Manager) and call it across all entity tabs.",
        "tip": "⚠️ LAMBDA by itself returns a #CALC! error — it must be called with arguments or saved as a named function.",
        "applications": ["FP&A", "Valuations"],
    },
    {
        "name": "TAKE / DROP", "category": "Dynamic Arrays", "difficulty": "Intermediate",
        "syntax": "=TAKE(array, rows, [cols])  /  =DROP(array, rows, [cols])",
        "description": "TAKE returns the first N rows/cols; DROP removes the first N rows/cols from a spilled range.",
        "use_case": "Reporting: Take the top 5 or bottom 5 deals from a SORT output for an executive summary table.",
        "tip": "⚠️ Use negative numbers in TAKE/DROP to count from the end: =TAKE(array, -3) returns the last 3 rows.",
        "applications": ["Reporting"],
    },

    # ── ERROR & INFO ──
    {
        "name": "ISERROR / ISNUMBER / ISTEXT / ISBLANK", "category": "Error & Info", "difficulty": "Beginner",
        "syntax": "=ISERROR(value)  /  =ISNUMBER(value)  /  =ISTEXT(value)  /  =ISBLANK(value)",
        "description": "Information functions that return TRUE/FALSE based on the content or type of a cell.",
        "use_case": "FP&A: Build model health checks — flag cells that should be numeric but contain text; highlight blank input cells.",
        "tip": "⚠️ ISBLANK returns FALSE for cells containing a formula that returns ''. Use LEN(A1)=0 for formula-blank detection.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "AGGREGATE", "category": "Error & Info", "difficulty": "Advanced",
        "syntax": "=AGGREGATE(function_num, options, array, [k])",
        "description": "Performs 19 aggregate functions (SUM, AVERAGE, LARGE, etc.) while ignoring hidden rows, errors, or nested SUBTOTALs.",
        "use_case": "Reporting: SUM a filtered table that contains error cells without IFERROR wrapping — AGGREGATE handles both in one step.",
        "tip": "⚠️ Options=6 ignores errors; options=5 ignores hidden rows; combine them: options=7 ignores both.",
        "applications": ["FP&A", "Reporting"],
    },
    {
        "name": "SUBTOTAL", "category": "Error & Info", "difficulty": "Intermediate",
        "syntax": "=SUBTOTAL(function_num, range)",
        "description": "Aggregates a range while automatically ignoring other SUBTOTAL cells and filtered-out rows.",
        "use_case": "Reporting: Build a P&L template where subtotals (Gross Profit, EBITDA) auto-exclude filtered rows without double-counting.",
        "tip": "⚠️ 101–111 function codes ignore manually hidden rows too; 1–11 count them. Use 109 for SUM that excludes hidden rows.",
        "applications": ["FP&A", "Reporting"],
    },

    # ── MATH EXTRAS ──
    {
        "name": "MROUND / CEILING / FLOOR", "category": "Math Extras", "difficulty": "Intermediate",
        "syntax": "=MROUND(num, multiple)  /  =CEILING(num, multiple)  /  =FLOOR(num, multiple)",
        "description": "Round to the nearest, up to, or down to a specified multiple.",
        "use_case": "FP&A: Round headcount to nearest 5 for budgeting; round capital draws up to the nearest $1M tranche size.",
        "tip": "⚠️ MROUND returns #NUM! if num and multiple have opposite signs. CEILING/FLOOR handle signs differently from ROUND.",
        "applications": ["FP&A"],
    },
    {
        "name": "MOD", "category": "Math Extras", "difficulty": "Intermediate",
        "syntax": "=MOD(number, divisor)",
        "description": "Returns the remainder after division.",
        "use_case": "FP&A: Determine which quarter a month number falls in: =CHOOSE(MOD(month-1,3)+1,...) or flag every Nth period.",
        "tip": "⚠️ MOD with a negative divisor returns a negative result. Use ABS() if you only need the magnitude.",
        "applications": ["FP&A"],
    },
    {
        "name": "POWER / SQRT", "category": "Math Extras", "difficulty": "Beginner",
        "syntax": "=POWER(number, power)  /  =SQRT(number)",
        "description": "POWER raises a number to any exponent; SQRT returns the square root.",
        "use_case": "Valuations: Compute CAGR = POWER(end/start, 1/n) - 1; annualise daily volatility by SQRT(252).",
        "tip": "⚠️ SQRT returns #NUM! for negatives. Use POWER(x, 0.5) — same result but easier to extend to cube roots etc.",
        "applications": ["FP&A", "Valuations"],
    },

    # ── INFORMATION & CELL ──
    {
        "name": "ROW / COLUMN", "category": "Info & Cell", "difficulty": "Beginner",
        "syntax": "=ROW([reference])  /  =COLUMN([reference])",
        "description": "Return the row or column number of a cell.",
        "use_case": "FP&A: Auto-number periods in a model: =ROW()-ROW($A$1) for period 1, 2, 3… without manual entry.",
        "tip": "⚠️ Without an argument ROW()/COLUMN() return the current cell's position — can shift unexpectedly when copied.",
        "applications": ["FP&A"],
    },
    {
        "name": "SHEET / SHEETS", "category": "Info & Cell", "difficulty": "Intermediate",
        "syntax": "=SHEET([value])  /  =SHEETS([reference])",
        "description": "SHEET returns the sheet number of a reference; SHEETS returns the total count of sheets in a workbook.",
        "use_case": "Reporting: Build workbook audit formulas that count the number of entity tabs in a multi-company consolidation model.",
        "tip": "⚠️ SHEET numbers change when tabs are reordered — never hardcode sheet numbers; rely on tab names instead.",
        "applications": ["Reporting"],
    },
    {
        "name": "ISFORMULA / CELL / TYPE", "category": "Info & Cell", "difficulty": "Advanced",
        "syntax": "=ISFORMULA(ref)  /  =CELL(info_type, ref)  /  =TYPE(value)",
        "description": "ISFORMULA checks if a cell contains a formula; CELL returns metadata; TYPE identifies the data type.",
        "use_case": "Reporting: Build model-integrity checks that highlight hardcoded values in cells that should always hold formulas.",
        "tip": "⚠️ CELL is volatile — it recalculates on any change. Avoid in large models; use for one-off audits only.",
        "applications": ["Reporting"],
    },
]

df = pd.DataFrame(FUNCTIONS)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.html("""
    <div style='text-align:center; padding: 20px 0 12px 0;'>
        <div style='font-size:2rem;'>⛰️</div>
        <div style='font-family:"Playfair Display",serif; font-size:1.1rem; color:#E8B84B; font-weight:700; margin-top:4px;'>
            The Mountain Path<br>Academy
        </div>
        <div style='font-size:0.72rem; color:#8A9ABC; margin-top:4px;'>
            Finance Functions Reference
        </div>
    </div>
    <hr style='border-color:#2C3E6B; margin:4px 0 16px 0;'>
    """)

    st.markdown("###  Search")
    search_query = st.text_input(
        "Function name or keyword",
        placeholder="e.g. XNPV, depreciation, IRR…",
        label_visibility="collapsed",
    )

    st.markdown("###  Category")
    categories = ["All"] + sorted(df["category"].unique().tolist())
    selected_cat = st.selectbox("Category", categories, label_visibility="collapsed")

    st.markdown("###  Difficulty")
    difficulty_opts = ["All", "Beginner", "Intermediate", "Advanced"]
    selected_diff = st.selectbox("Difficulty", difficulty_opts, label_visibility="collapsed")

    st.markdown("###  Model Application")
    app_opts = ["All", "FP&A", "Valuations", "Reporting"]
    selected_app = st.selectbox("Application", app_opts, label_visibility="collapsed")

    st.html("""
    <hr style='border-color:#2C3E6B; margin:16px 0;'>
    <div style='font-size:0.72rem; color:#6A7A9B; line-height:1.8;'>
        <strong style='color:#E8B84B;'>Difficulty guide</strong><br>
         Beginner — no prior formula knowledge needed<br>
         Intermediate — comfortable with basic Excel<br>
         Advanced — financial modelling experience required
    </div>
    <hr style='border-color:#2C3E6B; margin:14px 0;'>
    <div style='text-align:center;'>
        <div style='font-size:0.78rem; color:#E8B84B; font-weight:700; margin-bottom:4px;'>Prof. V. Ravichandran</div>
        <div style='font-size:0.68rem; color:#6A7A9B; margin-bottom:10px;'>28+ yrs · Corporate Finance &amp; Banking</div>
        <div style='display:flex; gap:8px; justify-content:center; flex-wrap:wrap;'>
            <a style='display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,0.07);border:1px solid rgba(232,184,75,0.35);border-radius:20px;padding:5px 12px;font-size:0.70rem;font-weight:600;color:#E8B84B;text-decoration:none;'
               href='https://www.linkedin.com/in/trichyravis' target='_blank'>
                <svg width='11' height='11' viewBox='0 0 24 24' fill='#E8B84B'>
                    <path d='M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z'/>
                </svg>
                LinkedIn
            </a>
            <a style='display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,0.07);border:1px solid rgba(232,184,75,0.35);border-radius:20px;padding:5px 12px;font-size:0.70rem;font-weight:600;color:#E8B84B;text-decoration:none;'
               href='https://github.com/trichyravis' target='_blank'>
                <svg width='11' height='11' viewBox='0 0 24 24' fill='#E8B84B'>
                    <path d='M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12'/>
                </svg>
                GitHub
            </a>
        </div>
    </div>
    """)

# ─── FILTERING ────────────────────────────────────────────────────────────────
filtered = df.copy()

if search_query.strip():
    q = search_query.strip().lower()
    filtered = filtered[
        filtered["name"].str.lower().str.contains(q) |
        filtered["description"].str.lower().str.contains(q) |
        filtered["use_case"].str.lower().str.contains(q) |
        filtered["syntax"].str.lower().str.contains(q)
    ]

if selected_cat != "All":
    filtered = filtered[filtered["category"] == selected_cat]

if selected_diff != "All":
    filtered = filtered[filtered["difficulty"] == selected_diff]

if selected_app != "All":
    filtered = filtered[filtered["applications"].apply(lambda apps: selected_app in apps)]

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.html("""
<div class="hero">
    <h1>⛰️ Excel Finance Functions Reference</h1>
    <p>
        A practitioner's guide to <span class="gold">90+ essential Excel functions</span> for financial modelling —
        with real-world use cases, syntax, and error-avoidance tips.<br>
        Curated by <span class="gold">Prof. V. Ravichandran</span> · themountainpathacademy.com
    </p>
</div>
""")

# ─── STAT CHIPS ───────────────────────────────────────────────────────────────
total = len(df)
shown = len(filtered)
cats  = df["category"].nunique()

st.html(f"""
<div class="stat-row">
    <div class="stat-chip"><span>{total}</span> Total Functions</div>
    <div class="stat-chip"><span>{cats}</span> Categories</div>
    <div class="stat-chip"><span>{shown}</span> Showing Now</div>
    <div class="stat-chip"><span>3</span> Model Types</div>
</div>
""")

# ─── CATEGORY ILLUSTRATION STRIP ─────────────────────────────────────────────
CAT_ICONS = {
    "Core Math":      ("➕", "#EBF5FF", "#1565C0"),
    "Conditional":    ("", "#FFF3E0", "#E65100"),
    "Lookup":         ("", "#F3E5F5", "#6A1B9A"),
    "Date & Time":    ("", "#E8F5E9", "#1B5E20"),
    "Financial":      ("", "#FCE4EC", "#880E4F"),
    "Statistical":    ("", "#E0F2F1", "#004D40"),
    "Text":           ("", "#FFF9C4", "#827717"),
    "Dynamic Arrays": ("⚡", "#E8EAF6", "#283593"),
    "Error & Info":   ("️", "#FFEBEE", "#B71C1C"),
    "Math Extras":    ("", "#F1F8E9", "#33691E"),
    "Info & Cell":    ("", "#E0F7FA", "#006064"),
}

icon_chips = "".join(
    f'''<div style="display:inline-flex;align-items:center;gap:6px;background:{bg};
        border:1px solid {col}33;border-radius:10px;padding:7px 13px;
        font-size:0.78rem;font-weight:600;color:{col};white-space:nowrap;
        box-shadow:0 1px 4px rgba(0,0,0,0.06);">
        <span style="font-size:1rem;">{icon}</span>{cat}
        <span style="background:{col};color:#fff;border-radius:10px;
              padding:0 6px;font-size:0.65rem;margin-left:2px;">
            {len(df[df["category"]==cat])}
        </span>
    </div>'''
    for cat, (icon, bg, col) in CAT_ICONS.items()
)
st.html(f"""
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:24px;padding:16px 20px;
     background:#fff;border-radius:12px;border:1px solid #DDE2ED;
     box-shadow:0 2px 8px rgba(0,0,0,0.05);">
  <div style="width:100%;font-size:0.72rem;font-weight:700;color:#8A94AB;
       text-transform:uppercase;letter-spacing:0.7px;margin-bottom:8px;">
     Browse by Category
  </div>
  {icon_chips}
</div>
""")

# ─── RESULTS ──────────────────────────────────────────────────────────────────
DIFF_EMOJI = {"Beginner": "", "Intermediate": "", "Advanced": ""}
APP_COLOUR  = {"FP&A": "#1565C0", "Valuations": "#880E4F", "Reporting": "#2E7D32"}

if filtered.empty:
    st.html("""
    <div class="no-result">
        <div class="icon"></div>
        <strong>No functions matched your filters.</strong><br>
        Try a broader search term or clear one of the filters.
    </div>
    """)
else:
    # Group by category for display
    for cat in ["Core Math", "Conditional", "Lookup", "Date & Time", "Financial",
                "Statistical", "Text", "Dynamic Arrays", "Error & Info", "Math Extras", "Info & Cell"]:
        group = filtered[filtered["category"] == cat]
        if group.empty:
            continue

        st.html(f'<div class="section-header"> {cat}</div>')

        for _, row in group.iterrows():
            diff_badge = f'<span class="cat-badge diff-{row["difficulty"]}">{DIFF_EMOJI[row["difficulty"]]} {row["difficulty"]}</span>'
            app_tags   = " ".join(
                f'<span class="tag" style="background:{APP_COLOUR[a]}22;color:{APP_COLOUR[a]};border:1px solid {APP_COLOUR[a]}44;">{a}</span>'
                for a in row["applications"]
            )
            cat_badge  = f'<span class="cat-badge cat-{cat}">{cat}</span>'

            st.html(f"""
<div class="fn-card">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
        <div class="fn-name">{row['name']}</div>
        <div style="display:flex; gap:8px; flex-wrap:wrap; align-items:center;">
            {diff_badge}
            {cat_badge}
        </div>
    </div>

    <div class="fn-syntax">{row['syntax']}</div>

    <div class="fn-desc">{row['description']}</div>

    <div class="fn-label"> Real-World Use Case</div>
    <div class="fn-usecase">{row['use_case']}</div>

    <div class="fn-label">⚠️ Error Avoidance Tip</div>
    <div class="fn-tip">{row['tip']}</div>

    <div class="fn-tags" style="margin-top:14px;">{app_tags}</div>
</div>
""")

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.html("""
<div class="footer">
    © 2026 <a href="https://themountainpathacademy.com" target="_blank">The Mountain Path Academy</a> ·
    Prof. V. Ravichandran · All rights reserved<br>
    Practitioner-led finance courses in Financial Modelling, Risk Management, Derivatives & Valuation
</div>
""")
