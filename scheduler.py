"""
Social Media Auto-Poster demo.
Usage: python scheduler.py

Reads posts.csv, 'publishes' anything due (dry-run prints),
marks rows as posted so nothing double-posts.

Learning path (TODOs):
  1. Wire publish() to real LinkedIn / X APIs
  2. Run on a schedule via cron or an n8n Schedule Trigger
  3. Pull posts from Google Sheets instead of CSV
"""

import csv
from datetime import datetime

POSTS_FILE = "posts.csv"
TIME_FORMAT = "%Y-%m-%d %H:%M"


def publish(post):
    # TODO: replace with real API calls per platform
    print(f"[POSTED -> {post['platforms']}] {post['text']}")
    if post.get("image_url"):
        print(f"           image: {post['image_url']}")


def main():
    now = datetime.now()
    with open(POSTS_FILE, newline="") as f:
        rows = list(csv.DictReader(f))

    due = [
        r
        for r in rows
        if r.get("status", "").strip().lower() != "posted"
        and datetime.strptime(r["scheduled_at"].strip(), TIME_FORMAT) <= now
    ]
    for post in due:
        publish(post)
        post["status"] = "posted"

    with open(POSTS_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Done: {len(due)} post(s) published, {len(rows) - len(due)} remaining.")


if __name__ == "__main__":
    main()
