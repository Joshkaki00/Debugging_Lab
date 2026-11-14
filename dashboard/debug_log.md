# DB-3: The slow dashboard

## Reproduce
- Ada (user 1): 4 projects in 0.03s
- Grace (user 2): 2500 projects in 15.73s

## Notes
- I expected Grace's dataset to load as fast as Ada's, but it turns out to be a very slow algorithm that takes more than 15 seconds for 2500 projects, which means that it doesn't scale well for larger sets.
- There is no error message. Everything runs correctly, just not fast.
- Lines 18-20 are causing very slow queries for bigger sets and slowing down the dashboard.
- This algorithm doesn't scale with larger sets because of the N+1 queries (one query for the project list, then one more query per project).
