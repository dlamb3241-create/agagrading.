# AGA Fullstack (Flask + Front-End)
Deploy a single service that serves both your rotating-cards site and minimal APIs.

## Deploy on Render
1. Zip this folder and upload as a **Web Service** (Python) on Render.
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn app:app`
4. After deploy, visit `/` for the site. Test API: `/api/health`.

## Notes
- No Stripe or webhooks included.
- SQLite is used by default; set `DATABASE_URL` to Postgres later if needed.
- Hero section is full-width but shorter (60vh / 50vh mobile).
- Headline uses reddish-orange gradient; site font is **Poppins**.
