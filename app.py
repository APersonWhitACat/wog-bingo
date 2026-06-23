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
)

st.markdown(
    """
<style>
.stApp {
    background:
        radial-gradient(circle at 50% 0%, rgba(255,209,102,.18), transparent 28%),
        linear-gradient(180deg, #0b1020 0%, #070910 100%);
    color: #f8fafc;
}

.block-container {
    padding-top: 1.1rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

.header {
    text-align: center;
    margin-bottom: .6rem;
}

.title {
    color: #ffd166;
    font-size: clamp(2rem, 4vw, 3.5rem);
    font-weight: 1000;
    line-height: 1;
    text-shadow: 0 0 18px rgba(255, 209, 102, .55);
}

.subtitle {
    color: #a8b3c7;
    font-weight: 900;
    letter-spacing: .12em;
    margin-top: .25rem;
}

.neon {
    height: 4px;
    max-width: 760px;
    margin: .7rem auto 1rem auto;
    border-radius: 999px;
    background: linear-gradient(90deg, #ef476f, #ffd166, #06d6a0, #4cc9f0, #b517ff);
    box-shadow: 0 0 18px rgba(255, 209, 102, .75);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { opacity: .7; filter: brightness(.9); }
    to { opacity: 1; filter: brightness(1.35); }
}

.rules {
    background: rgba(20, 26, 36, .96);
    border: 1px solid #34425a;
    border-radius: 14px;
    padding: .85rem 1rem;
    color: #f8fafc;
    margin-bottom: 1rem;
    box-shadow: 0 0 18px rgba(0,0,0,.22);
}

.board-title {
    color: #ffd166;
    text-align: center;
    font-size: 1.05rem;
    font-weight: 950;
    margin: .2rem 0 .45rem;
}

.board-shell {
    background: linear-gradient(135deg, #ffb703, #ffd166, #9a6b00);
    border-radius: 18px;
    padding: 5px;
    box-shadow: 0 0 25px rgba(255,183,3,.28);
    margin-bottom: 1.1rem;
}

.board-inner {
    background: #2b210e;
    border-radius: 14px;
    padding: 4px;
}

/* Streamlit button cells */
div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 90px;
    height: 90px;
    border-radius: 10px;
    border: 1px solid #30405a;
    background: #172033;
    color: #f8fafc;
    padding: 6px;
    font-size: clamp(.55rem, .85vw, .82rem);
    font-weight: 900;
    line-height: 1.12;
    white-space: normal;
    word-break: normal;
    overflow-wrap: anywhere;
    overflow: hidden;
    text-align: center;
    box-shadow: inset 0 0 12px rgba(255,255,255,.025);
}

div[data-testid="stButton"] > button:hover {
    border-color: #ffd166;
    color: #ffd166;
    background: #1d2740;
}

/* Main control buttons */
.control-row div[data-testid="stButton"] > button {
    min-height: 42px;
    height: 42px;
    font-size: .9rem;
    background: #251a08;
    color: #ffd166;
    border-color: #60430b;
}

/* marked/free styling by button text marker */
div[data-testid="stButton"] > button:has(p:contains("✓")) {
    background: #138a52;
}

/* Mobile / smaller screens */
@media (max-width: 800px) {
    div[data-testid="stButton"] > button {
        min-height: 76px;
        height: 76px;
        font-size: .56rem;
        padding: 3px;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


def new_board():
    shuffled = ITEMS[:]
    random.shuffle(shuffled)
    board = []
    idx = 0
    for i in range(25):
        if i == 12:
            board.append("FREE SPACE")
        else:
            board.append(shuffled[idx])
            idx += 1
    return board


def win_lines():
    lines = []
    for r in range(5):
        lines.append([r * 5 + c for c in range(5)])
    for c in range(5):
        lines.append([r * 5 + c for r in range(5)])
    lines.append([0, 6, 12, 18, 24])
    lines.append([4, 8, 12, 16, 20])
    return lines


def has_bingo(marked):
    return any(all(i in marked for i in line) for line in win_lines())


def ensure_boards(count):
    if "boards" not in st.session_state:
        st.session_state.boards = []
    if "marked" not in st.session_state:
        st.session_state.marked = []

    while len(st.session_state.boards) < count:
        st.session_state.boards.append(new_board())
        st.session_state.marked.append({12})

    while len(st.session_state.boards) > count:
        st.session_state.boards.pop()
        st.session_state.marked.pop()


def roll_all():
    for i in range(len(st.session_state.boards)):
        st.session_state.boards[i] = new_board()
        st.session_state.marked[i] = {12}


def reset_all():
    for i in range(len(st.session_state.marked)):
        st.session_state.marked[i] = {12}


def toggle(board_i, cell_i):
    if cell_i == 12:
        return
    marked = st.session_state.marked[board_i]
    if cell_i in marked:
        marked.remove(cell_i)
    else:
        marked.add(cell_i)


st.markdown(
    """
<div class="header">
    <div style="font-size:2rem;">⚂ 🎲 ⚄</div>
    <div class="title">✦ Wings of Glory ✦<br>LOW RANK BINGO</div>
    <div class="subtitle">casino roll mode</div>
    <div class="neon"></div>
</div>
""",
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="control-row">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1, 1, 1, 1.2])
    with c1:
        if st.button("🎲 Roll all", use_container_width=True):
            roll_all()
            st.rerun()
    with c2:
        if st.button("Reset marks", use_container_width=True):
            reset_all()
            st.rerun()
    with c3:
        rules = st.toggle("Rules", value=False)
    with c4:
        board_count = st.selectbox("Boards", [1, 2, 3, 4, 5, 6], index=0)
    st.markdown("</div>", unsafe_allow_html=True)

ensure_boards(board_count)

if rules:
    st.markdown(
        """
<div class="rules">
<b>Rules</b><br>
• Click a square when it happens<br>
• FREE SPACE is already marked<br>
• 5 in a row = BINGO<br>
• Rows, columns, diagonals count<br>
• Roll all makes fresh random boards
</div>
""",
        unsafe_allow_html=True,
    )

# 1-2 boards per row depending on count/window.
if board_count == 1:
    boards_per_row = 1
elif board_count <= 4:
    boards_per_row = 2
else:
    boards_per_row = 3

for start in range(0, board_count, boards_per_row):
    board_cols = st.columns(boards_per_row, gap="large")
    for offset, col in enumerate(board_cols):
        b = start + offset
        if b >= board_count:
            continue

        with col:
            st.markdown(f'<div class="board-title">BOARD {b + 1}</div>', unsafe_allow_html=True)

            if has_bingo(st.session_state.marked[b]):
                st.markdown(
                    """
<div style="
text-align:center;
font-size:2.2rem;
font-weight:1000;
color:#ffd166;
text-shadow:0 0 14px #ffd166, 0 0 28px #ef476f;
margin-bottom:.4rem;
animation: glow 1s ease-in-out infinite alternate;">
BINGO!
</div>
""",
                    unsafe_allow_html=True,
                )

            st.markdown('<div class="board-shell"><div class="board-inner">', unsafe_allow_html=True)

            for r in range(5):
                row_cols = st.columns(5, gap="small")
                for c, cell_col in enumerate(row_cols):
                    cell_i = r * 5 + c
                    label = st.session_state.boards[b][cell_i]

                    if cell_i == 12:
                        shown = "FREE\nSPACE"
                    elif cell_i in st.session_state.marked[b]:
                        shown = "✓ " + label
                    else:
                        shown = label

                    with cell_col:
                        if st.button(
                            shown,
                            key=f"b{b}_cell{cell_i}_{label}",
                            use_container_width=True,
                            disabled=(cell_i == 12),
                        ):
                            toggle(b, cell_i)
                            st.rerun()

            st.markdown("</div></div>", unsafe_allow_html=True)

st.caption("Tip: if text is still too tight, use fewer boards or make the browser window wider.")
