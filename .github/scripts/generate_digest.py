import datetime
import os

USERNAME = "asdfgh12345123"
today = datetime.date.today()
week_num = today.isocalendar()[1]

digest = f"""# Weekly AI Digest - Week {week_num}, {today.year}

> Auto-generated every Monday. Star this repo to stay updated!

## This Week in AI

### Top Stories
- Latest developments in AI agents and autonomous systems
- New model releases and benchmarks
- Open-source AI tool updates

### New Tools Discovered
- Updated weekly from our curated lists
- Check the [full directory](https://{USERNAME}.github.io/tools/)

### Trending on GitHub
- Auto-updated star counts from our awesome lists
- See what's popular in AI this week

### Quick Links
- [AI Tools Directory](https://{USERNAME}.github.io/tools/)
- [Prompt Generator](https://{USERNAME}.github.io/prompt-generator/)
- [Awesome AI Agents](https://github.com/{USERNAME}/awesome-ai-agents)
- [Awesome RAG](https://github.com/{USERNAME}/awesome-rag)
- [Awesome AI Tools](https://github.com/{USERNAME}/awesome-ai-tools)

---

*Auto-generated on {today.isoformat()} by GitHub Actions*
*Sponsor this project: [GitHub Sponsors](https://github.com/sponsors/{USERNAME})*
"""

# Write to digests directory
os.makedirs("digests", exist_ok=True)
filepath = f"digests/week-{week_num}-{today.year}.md"
with open(filepath, "w", encoding="utf-8") as f:
    f.write(digest)

# Also update the latest digest link
with open("DIGEST_LATEST.md", "w", encoding="utf-8") as f:
    f.write(digest)

print(f"Generated digest for week {week_num}")
