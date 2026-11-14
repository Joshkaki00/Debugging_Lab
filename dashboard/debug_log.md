- I expected Grace's dataset to load as fast as Ada's, but it takes more than 15 seconds for 2500 projects, so it doesn't scale well for larger sets.
- There is no error message. Everything runs correctly, just not fast.
- Lines 18-20 are the problem — not because each query is slow, but because it runs one query per project, so bigger sets mean way more queries and the dashboard slows down.
- This doesn't scale with larger sets because of the N+1 queries.

## Fix
- Replaced the loop with one SQL query: LEFT JOIN projects/tasks, COUNT open tasks, GROUP BY project.
- Grace went from ~2501 queries / 15.73s down to 1 query / 0.02s. Ada is still fine. pytest passes.
- Root cause: N+1 — one query for projects, then one more per project for tasks.
