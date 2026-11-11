# Debugging Lab

Two small projects with real bugs, set up the way a debugging interview hands you code: download it, install it, run it, and find the problem. Getting an unfamiliar project running quickly is part of the test.

| Folder | Language | Bug report |
| --- | --- | --- |
| `cart/` | JavaScript (Node.js) | DB-2: The disappearing cart items |
| `dashboard/` | Python | DB-3: The slow dashboard |

## Before you install anything

Read `cart/package.json` and `dashboard/requirements.txt` first. You should know what you're installing and what `npm start` and `npm test` will run. Do this every time. Fake take-home assignments are a known way to spread malware.

## You'll need

- **Node.js 18 or newer:** check with `node -v`
- **Python 3.9 or newer:** check with `python3 --version` (on Windows, use `python` instead of `python3`)

---

## DB-2: The disappearing cart items (`cart/`)

> **Bug report:** "I added a mug, a t-shirt, some stickers, then went back and added another mug. My cart only has one mug in it!"

### Setup

```bash
cd cart
npm install
npm start      # replays the customer's steps and prints the cart
npm test       # runs the test suite
```

### Your task

1. Reproduce the bug with `npm start`. What did you expect to see, and what did you actually see?
1. The tests all pass. Why didn't they catch this?
1. Write a test that fails because of the bug *before* you change any code.
1. Fix the bug, then run `npm test` and `npm start` again.
1. Explain the root cause in one sentence.

---

## DB-3: The slow dashboard (`dashboard/`)

> **Bug report:** "The dashboard takes about 20 seconds to load for Grace, who has a lot of projects. It's instant for Ada."

### Setup

macOS / Linux:

```bash
cd dashboard
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python seed.py            # creates dashboard.db with sample data
python dashboard.py 1     # Ada: a few projects
python dashboard.py 2     # Grace: 2,500 projects
pytest                    # runs the test suite
```

Windows (PowerShell): same steps, but use `python -m venv .venv` and `.venv\Scripts\Activate.ps1`.

### Your task

1. Reproduce it: time the dashboard for user 1 and user 2. How does load time grow with the number of projects?
1. Read `dashboard.py` and `db.py`. How many database queries does one dashboard load make for Grace? (Hint: `db.query_count`.)
1. Form a hypothesis about where the time goes, and measure it before changing anything.
1. Fix it so the dashboard makes a small, fixed number of queries no matter how many projects a user has.
1. Run `pytest`. The tests check that the results are still correct. A fast answer that's wrong doesn't count.
1. Time it again, and explain the root cause in one sentence.

---

## The debugging process

1. Reproduce the bug reliably
1. Read the code path involved. Don't guess yet.
1. Form one hypothesis and test it (print statements, a debugger, a failing test)
1. Fix the smallest thing that resolves it
1. Verify the fix, and check that you didn't break anything else
1. Explain the root cause in one sentence
