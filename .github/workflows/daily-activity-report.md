---
name: Daily Activity Report
on:
  schedule:
    - cron: '0 0 * * *' # daily at 00:00 UTC
description: |
  Generate a daily report of recent repository activity (commits, PR updates, and issues) and open it as an issue.
  This markdown is the human-friendly agentic workflow definition (follow the gh-aw create.md guidance).
---

# Daily Activity Report (Agentic workflow)

This workflow runs daily and produces a short report of repository activity in the last 24 hours. The compiled lock file (.lock.yml) contains a runnable implementation that creates an issue with the report.

Behavior:

- Determine activity since 24 hours ago (commits, pull requests updated, issues updated)
- Summarize counts and include short lists with links
- Create a new issue titled "Daily activity report — YYYY-MM-DD" with the summary

Notes:
- The .lock.yml in the same directory provides a runnable GitHub Actions job that implements the report generation using the GitHub API.
- The GITHUB_TOKEN provided to the workflow is used to create the issue.

If the repository uses a different schedule or wants additional details (e.g., filtering by directories or authors), adjust the compiled lock workflow accordingly.
