"""
To run:
uv venv --seed
uv pip install -e ".[de]"
uv run examples/usage_de.py
"""

from misaki.de import DEG2P

g2p = DEG2P()

text = "Donald Trump von Scrum und Kanban kennen, sondern konnten diese Methoden direkt in praktischen Gruppenübungen anwenden und ihre Erfahrungen anschließend gemeinsam reflektieren."

phonemes, tokens = g2p(text)

print(phonemes)
print(tokens)  # None: DEG2P does not return MTokens, unlike en.G2P