import random
import streamlit as st

BINGO_ITEMS = [
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
    'huge fuckass ego'
]

st.set_page_config(
    page_title="Wings of Glory Bingo",
    page_icon="🎲",
    layout="centered"
)

CSS = """
<style>
.stApp {
    background: radial-gradient(circle at top, #172033 0%, #070910 60%);
    color: #f8fafc;
}

.block-container {
    max-width: 760px;
    padding-top: 1.2rem;
}

.title {
    text-align: center;
    color: #ffd166;
    font-size: 2.2rem;
    font-weight: 900;
    line-height: 1.1;
    text-shadow: 0 0 12px rgba(255, 209, 102, .45);
}

.subtitle {
    text-align: center;
    color: #a8b3c7;
    font-weight: 800;
    margin-bottom: .5rem;
}

.neon {
    height: 3px;
    margin: 8px 40px 18px 40px;
    background: linear-gradient(90deg, #ef476f, #ffd166, #06d6a0, #4cc9f0, #b517ff);
    border-radius: 999px;
    box-shadow: 0 0 16px rgba(255, 209, 102, .8);
    animation: glow 2.2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { filter: brightness(.8); opacity: .75; }
    to { filter: brightness(1.35); opacity: 1; }
}

.dice {
    text-align: center;
    color: #ffd166;
    font-size: 1.8rem;
    animation: bob 1.4s ease-in-out infinite alternate;
}

@keyframes bob {
    from { transform: translateY(0px); }
    to { transform: translateY(-4px); }
}

.board {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 3px;
    padding: 6px;
    background: #ffb703;
    border-radius: 14px;
    box-shadow: 0 0 24px rgba(255, 183, 3, .25);
}

.cell {
    min-height: 92px;
    border-radius: 10px;
    background: #172033;
    color: #f8fafc;
    border: 1px solid #30405a;
    padding: 8px;
    font-size: .78rem;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    word-break: normal;
    overflow-wrap: anywhere;
}

.cell.alt {
    background: #1b2740;
}

.cell.marked {
    background: #138a52;
    border-color: #33e28e;
    color: #ecfff4;
    box-shadow: inset 0 0 16px rgba(46, 232, 142, .25);
}

.cell.free {
    background: #532e86;
    border-color: #ffd166;
    color: #ffd166;
    font-size: 1rem;
    font-style: italic;
}

.big-bingo {
    text-align: center;
    font-size: 3rem;
    font-weight: 1000;
    color: #ffd166;
    text-shadow: 0 0 14px #ffd166, 0 0 30px #ef476f;
    animation: pulse 0.8s ease-in-out infinite alternate;
}

@keyframes pulse {
    from { transform: scale(1); filter: brightness(1); }
    to { transform: scale(1.05); filter: brightness(1.4); }
}

.rules {
    background: #141a24;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 12px 16px;
    color: #f8fafc;
    margin-top: 10px;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def make_board():
    items = BINGO_ITEMS.copy()
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


def winning_lines():
    lines = []
    for r in range(5):
        lines.append([r * 5 + c for c in range(5)])
    for c in range(5):
        lines.append([r * 5 + c for r in range(5)])
    lines.append([0, 6, 12, 18, 24])
    lines.append([4, 8, 12, 16, 20])
    return lines


def has_bingo(marked):
    return any(all(i in marked for i in line) for line in winning_lines())


if "board" not in st.session_state:
    st.session_state.board = make_board()
if "marked" not in st.session_state:
    st.session_state.marked = {12}
if "show_rules" not in st.session_state:
    st.session_state.show_rules = False


def roll():
    st.session_state.board = make_board()
    st.session_state.marked = {12}
    st.session_state.show_rules = False


def reset():
    st.session_state.marked = {12}


st.markdown('<div class="dice">⚂ 🎲 ⚄</div>', unsafe_allow_html=True)
st.markdown('<div class="title">✦ Wings of Glory ✦<br>LOW RANK BINGO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">casino roll mode</div>', unsafe_allow_html=True)
st.markdown('<div class="neon"></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.button("🎲 Roll", use_container_width=True, on_click=roll)
with c2:
    st.button("Reset", use_container_width=True, on_click=reset)
with c3:
    if st.button("Bingo?", use_container_width=True):
        st.session_state.show_rules = not st.session_state.show_rules

if st.session_state.show_rules:
    st.markdown(
        """
        <div class="rules">
        <b>Rules</b><br>
        • Click a square when it happens<br>
        • FREE SPACE is already marked<br>
        • 5 in a row = BINGO<br>
        • Rows, columns, diagonals count<br>
        • Roll makes a new random board
        </div>
        """,
        unsafe_allow_html=True
    )

# Render board as Streamlit buttons so clicks persist.
for r in range(5):
    cols = st.columns(5, gap="small")
    for c, col in enumerate(cols):
        i = r * 5 + c
        text = st.session_state.board[i]
        marked = i in st.session_state.marked
        label = "FREE SPACE" if i == 12 else text

        with col:
            clicked = st.button(
                label,
                key=f"cell_{i}_{text}",
                use_container_width=True,
                disabled=(i == 12)
            )
            if clicked:
                if i in st.session_state.marked:
                    st.session_state.marked.remove(i)
                else:
                    st.session_state.marked.add(i)
                st.rerun()

# Pretty visual board below/overrides button ugliness with CSS targeting is limited in Streamlit,
# so this gives a clean readout of current marked state.
html_cells = []
for i, item in enumerate(st.session_state.board):
    classes = ["cell"]
    if i % 2:
        classes.append("alt")
    if i == 12:
        classes.append("free")
    if i in st.session_state.marked:
        classes.append("marked")
    html_cells.append(f'<div class="{" ".join(classes)}">{item}</div>')

st.markdown('<div class="board">' + "".join(html_cells) + '</div>', unsafe_allow_html=True)

if has_bingo(st.session_state.marked):
    st.markdown('<div class="big-bingo">BINGO!<br>JACKPOT HIT</div>', unsafe_allow_html=True)
