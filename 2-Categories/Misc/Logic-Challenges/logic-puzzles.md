# Logic Challenges for CTF Practice

## 🧠 1. Basic Puzzle

You see 100 prisoners in a room. A light bulb is placed in a separate room. They can enter the room one by one. How do they ensure everyone has been in the room at least once?

➡️ **Hint**: Use a counter strategy.

---

## 🔐 2. Truth Tellers and Liars

A classic CTF logic challenge. You're on an island where some people always tell the truth and some always lie.

You meet two guards:

- A says: "Only one of us is lying."
- B says nothing.

Who is telling the truth?

➡️ **Hint**: Assume each case and test consistency.

---

## 🔍 3. CTF-style Grid Puzzle

You're given a grid with binary inputs, and certain rows/columns must result in specific logical outputs (AND, OR, XOR). You must fill the grid to satisfy all conditions.

> Example:
> - Row 1: 1 0 1 → AND = 0, OR = 1, XOR = 0
> - What combinations satisfy both?

---

## Tools Recommended

- Truth Table Generator
- Logic Gate Simulators (online)
- Python with `itertools` or `sympy.logic.boolalg`

Good luck, logician!