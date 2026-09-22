# Social Media Auto-Poster (Demo)

Turn spreadsheet rows into scheduled social media posts. Write a week of content in one sitting — the automation handles the posting schedule.

## How it works
1. Add posts to `posts.csv` (text, image URL, scheduled time, platforms)
2. Run the scheduler (or trigger it on a schedule in n8n / Make)
3. Due posts get "published" (dry-run prints them — wire up real APIs when ready)
4. Published rows are marked `posted` so nothing ever double-posts

## Try it
```bash
python scheduler.py
```

## No-code version
Google Sheet → schedule trigger → platform modules (LinkedIn, X, Instagram) in Make / n8n. Same logic, zero code.

## Roadmap
- [ ] Real LinkedIn / X API posting
- [ ] Image upload support
- [ ] Best-time-to-post suggestions

*Built while learning automation — feedback welcome!*

## Support My Work

If you find this project useful, consider supporting my work with a Bitcoin donation:

`BC1Q6Q75K8ZJXVW7W02LMDPRPY6XX6QK4LZZ2RMVAY`
