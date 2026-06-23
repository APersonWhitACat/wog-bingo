import random
import streamlit as st

ITEMS = [
    '"add 5th gen aircrafts!"',
    'DOGSHIT opinion or suggestion',
    'corny ass profile/pfp',
    '"errrmm is all bvr so it\'s LAME"',
    'chaff = flare',
    'thinks they\'re good',
    'nerf f14a or phoenix missiles',
    'compares wog to wt',
    "doesn't know any bfm/acm",
    '"codes?"',
    'add their favorite niche aircraft',
    '"i have a life/whats wrong with low rank"',
    'realized they have no image perms',
    '"My rank ingame is higher"',
    'extremely biased',
    'intentional rule breaking',
    '"when update?" bro the update is soon chilllll',
    'bitching about killstealing',
    '"(decent plane) is so bad"',
    '"(premium plane) is p2w..."',
    '"add (insert nation) tree!"',
    "can't lose their argument",
    'rants about russian aircrafts',
    'huge fuckass ego',
]

st.set_page_config(
    page_title="Wings of Glory Bingo",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
/* Hide the default Streamlit chrome so the title does not get cut */
header[data-testid="stHeader"] {
    display: none;
}
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}

.stApp {
    background:
        radial-gradient(circle at 50% -8%, rgba(255, 209, 102, .20), transparent 28%),
        radial-gradient(circle at 15% 25%, rgba(76, 201, 240, .10), transparent 24%),
        radial-gradient(circle at 85% 20%, rgba(181, 23, 255, .10), transparent 20%),
        linear-gradient(180deg, #080b14 0%, #05070d 100%);
    color: #f8fafc;
}

.block-container {
    padding-top: 1.1rem !important;
    padding-bottom: 2rem !important;
    max-width: 1180px;
}

.hero {
    text-align: center;
    margin: .2rem auto 1rem auto;
    padding: 1rem 1rem .7rem;
    border-radius: 26px;
    background: rgba(9, 13, 24, .72);
    border: 1px solid rgba(255, 209, 102, .14);
    box-shadow: 0 0 50px rgba(0,0,0,.35), inset 0 0 28px rgba(255,255,255,.025);
}

.dice-row {
    font-size: 1.65rem;
    height: 2rem;
    color: #ffd166;
    animation: diceFloat 1.8s ease-in-out infinite alternate;
}

@keyframes diceFloat {
    from { transform: translateY(0px) rotate(-1deg); filter: brightness(.95); }
    to { transform: translateY(-4px) rotate(1deg); filter: brightness(1.25); }
}

.title {
    color: #ffd166;
    font-size: clamp(2rem, 5.2vw, 4.2rem);
    font-weight: 1000;
    line-height: .96;
    letter-spacing: -.03em;
    text-shadow: 0 0 18px rgba(255, 209, 102, .42), 0 0 46px rgba(255, 183, 3, .17);
    margin-top: .25rem;
}

.neon {
    height: 4px;
    max-width: 760px;
    margin: 1rem auto .2rem auto;
    border-radius: 999px;
    background: linear-gradient(90deg, #ef476f, #ffd166, #06d6a0, #4cc9f0, #b517ff);
    box-shadow: 0 0 18px rgba(255, 209, 102, .75);
    animation: neonMove 3s linear infinite;
    background-size: 250% 100%;
}

@keyframes neonMove {
    0% { background-position: 0% 50%; filter: brightness(.92); }
    50% { background-position: 100% 50%; filter: brightness(1.22); }
    100% { background-position: 0% 50%; filter: brightness(.92); }
}

.controls-wrap {
    margin: .6rem auto 1rem auto;
    padding: .75rem;
    border-radius: 18px;
    background: rgba(16, 23, 38, .86);
    border: 1px solid rgba(255,255,255,.08);
    box-shadow: 0 12px 28px rgba(0,0,0,.22);
}

/* Control buttons */
.control-row div[data-testid="stButton"] > button {
    min-height: 44px;
    height: 44px;
    border-radius: 12px;
    border: 1px solid rgba(255, 209, 102, .38);
    background: linear-gradient(180deg, #2d210d, #181209);
    color: #ffd166;
    font-size: .92rem;
    font-weight: 900;
    box-shadow: 0 0 14px rgba(255,183,3,.10), inset 0 1px 0 rgba(255,255,255,.08);
}
.control-row div[data-testid="stButton"] > button:hover {
    border-color: #ffd166;
    color: #fff4c7;
    transform: translateY(-1px);
    box-shadow: 0 0 22px rgba(255,183,3,.22);
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background: #111827;
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 12px;
    min-height: 44px;
}

.rules-card {
    background: rgba(17, 24, 39, .95);
    border: 1px solid rgba(255, 209, 102, .20);
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin: .4rem 0 1rem;
    box-shadow: 0 0 24px rgba(0,0,0,.24);
    color: #f8fafc;
}

.board-title {
    color: #ffd166;
    text-align: center;
    font-size: 1.05rem;
    font-weight: 1000;
    letter-spacing: .08em;
    margin: .2rem 0 .5rem;
    text-shadow: 0 0 10px rgba(255, 209, 102, .35);
}

.board-shell {
    background: linear-gradient(135deg, #ffb703, #ffd166 35%, #7c5200);
    border-radius: 20px;
    padding: 5px;
    box-shadow: 0 0 26px rgba(255,183,3,.30);
    margin-bottom: 1.2rem;
}

.board-inner {
    background: #1b150b;
    border-radius: 15px;
    padding: 5px;
}

/* Cell buttons */
.cell-grid div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 92px;
    height: 92px;
    border-radius: 11px;
    border: 1px solid #34425a;
    background: linear-gradient(180deg, #1b2740, #141d31);
    color: #f8fafc;
    padding: 6px;
    font-size: clamp(.55rem, .82vw, .82rem);
    font-weight: 900;
    line-height: 1.12;
    white-space: normal;
    word-break: normal;
    overflow-wrap: anywhere;
    overflow: hidden;
    text-align: center;
    box-shadow: inset 0 0 15px rgba(255,255,255,.025);
}
.cell-grid div[data-testid="stButton"] > button:hover {
    border-color: #ffd166;
    color: #ffd166;
    background: linear-gradient(180deg, #23304c, #19253e);
}

.bingo-banner {
    text-align:center;
    font-size:2.7rem;
    font-weight:1000;
    color:#ffd166;
    text-shadow:0 0 14px #ffd166, 0 0 28px #ef476f;
    margin:.1rem 0 .6rem;
    animation: jackpot .85s ease-in-out infinite alternate;
}
@keyframes jackpot {
    from { transform: scale(1); filter: brightness(1); }
    to { transform: scale(1.045); filter: brightness(1.35); }
}

.small-note {
    text-align:center;
    color:#a8b3c7;
    font-size:.85rem;
    margin-top:.25rem;
}

@media (max-width: 850px) {
    .block-container { padding-left: .65rem !important; padding-right: .65rem !important; }
    .cell-grid div[data-testid="stButton"] > button {
        min-height: 78px;
        height: 78px;
        font-size: .55rem;
        padding: 3px;
    }
    .title { font-size: 2.2rem; }
}
</style>
""",
    unsafe_allow_html=True,
)


def make_board():
    items = ITEMS[:]
    random.shuffle(items)
    board = []
    idx = 0
    for i in range(25):
        if i == 12:
            board.append("FREE SPACE")
        else:
            board.append(items[idx])
            idx += 1
    return board


def win_lines():
    rows = [[r * 5 + c for c in range(5)] for r in range(5)]
    cols = [[r * 5 + c for r in range(5)] for c in range(5)]
    return rows + cols + [[0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]


def has_bingo(marked):
    return any(all(i in marked for i in line) for line in win_lines())


def ensure_state(count):
    if "boards" not in st.session_state:
        st.session_state.boards = []
    if "marked" not in st.session_state:
        st.session_state.marked = []
    if "rules_open" not in st.session_state:
        st.session_state.rules_open = False

    while len(st.session_state.boards) < count:
        st.session_state.boards.append(make_board())
        st.session_state.marked.append({12})

    while len(st.session_state.boards) > count:
        st.session_state.boards.pop()
        st.session_state.marked.pop()


def roll_all():
    for i in range(len(st.session_state.boards)):
        st.session_state.boards[i] = make_board()
        st.session_state.marked[i] = {12}


def reset_all():
    for i in range(len(st.session_state.marked)):
        st.session_state.marked[i] = {12}


def toggle_cell(board_i, cell_i):
    if cell_i == 12:
        return
    marked = st.session_state.marked[board_i]
    if cell_i in marked:
        marked.remove(cell_i)
    else:
        marked.add(cell_i)


# Default state before controls.
if "board_count" not in st.session_state:
    st.session_state.board_count = 1
ensure_state(st.session_state.board_count)

st.markdown(
    """
<div class="hero">
    <div class="dice-row">⚂ 🎲 ⚄</div>
    <div class="title">✦ Wings of Glory ✦<br>Low Rank Bingo</div>
    <div class="neon"></div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="controls-wrap"><div class="control-row">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns([1, 1, 1, 1.05], gap="medium")

with c1:
    if st.button("🎲 Roll", use_container_width=True):
        roll_all()
        st.rerun()

with c2:
    if st.button("Reset", use_container_width=True):
        reset_all()
        st.rerun()

with c3:
    if st.button("Rules", use_container_width=True):
        st.session_state.rules_open = not st.session_state.rules_open
        st.rerun()

with c4:
    selected_count = st.selectbox(
        "Boards",
        [1, 2, 3, 4, 5, 6],
        index=[1, 2, 3, 4, 5, 6].index(st.session_state.board_count),
        label_visibility="collapsed",
    )
    if selected_count != st.session_state.board_count:
        st.session_state.board_count = selected_count
        ensure_state(selected_count)
        st.rerun()

st.markdown("</div></div>", unsafe_allow_html=True)

if st.session_state.rules_open:
    st.markdown(
        """
<div class="rules-card">
<b>Rules</b><br>
• Click a square when it happens<br>
• FREE SPACE is already marked<br>
• 5 in a row wins<br>
• Rows, columns, and diagonals count<br>
• Roll creates a fresh board
</div>
""",
        unsafe_allow_html=True,
    )

ensure_state(st.session_state.board_count)

# Layout boards nicely.
count = st.session_state.board_count
boards_per_row = 1 if count == 1 else 2 if count <= 4 else 3

for start in range(0, count, boards_per_row):
    cols = st.columns(boards_per_row, gap="large")

    for offset, col in enumerate(cols):
        b = start + offset
        if b >= count:
            continue

        with col:
            st.markdown(f'<div class="board-title">BOARD {b + 1}</div>', unsafe_allow_html=True)

            if has_bingo(st.session_state.marked[b]):
                st.markdown('<div class="bingo-banner">BINGO!</div>', unsafe_allow_html=True)

            st.markdown('<div class="board-shell"><div class="board-inner"><div class="cell-grid">', unsafe_allow_html=True)

            for r in range(5):
                row_cols = st.columns(5, gap="small")
                for c, cell_col in enumerate(row_cols):
                    idx = r * 5 + c
                    item = st.session_state.boards[b][idx]
                    marked = idx in st.session_state.marked[b]

                    if idx == 12:
                        label = "FREE\nSPACE"
                    elif marked:
                        label = "✓ " + item
                    else:
                        label = item

                    with cell_col:
                        if st.button(
                            label,
                            key=f"board_{b}_cell_{idx}_{item}",
                            use_container_width=True,
                            disabled=(idx == 12),
                        ):
                            toggle_cell(b, idx)
                            st.rerun()

            st.markdown("</div></div></div>", unsafe_allow_html=True)

st.markdown('<div class="small-note">Tip: use fewer boards if text feels cramped.</div>', unsafe_allow_html=True)
