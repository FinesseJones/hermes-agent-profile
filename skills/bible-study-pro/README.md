# Bible Study Pro — Hermes Agent Skill

## Overview
This skill wires Hermes AI to the Bible Study Pro full-stack application.
The app is located at: `/Users/finessejones1/Downloads/bible-study-pro 2/`
It runs locally at: `http://localhost:5001`

## App Architecture
- **Frontend**: React 19 + Vite + TailwindCSS, located in `client/src/`
- **Backend**: Express + tRPC, located in `server/`
- **Database**: MySQL on Hetzner VPS, accessed via `DATABASE_URL` env var
- **AI**: OpenRouter API (`OPENROUTER_API_KEY`), model `google/gemini-2.5-flash-preview`
- **Auth**: OAuth via `sdk.authenticateRequest()`
- **ORM**: Drizzle ORM, schema in `drizzle/schema.ts`

## Pages
| Route | File | Purpose |
|---|---|---|
| `/` | `Home.tsx` | Library — browse studies, global search, upload PDF |
| `/notes` | `CornellNotes.tsx` | Live recording, Cornell notes, Logos Bible panel |
| `/assistant` | `Assistant.tsx` | AI chat with streaming, PDF upload, context selector |
| `/vault` | `Vault.tsx` | PDF library management, upload, Google Drive sync |
| `/journal` | `Journal.tsx` | Spiritual journal with AI reflection |
| `/history` | `History.tsx` | Lesson history timeline |
| `/iron` | `IronSharpenIron.tsx` | Discussion study tool |

## Key Server Routers (server/routers.ts)
- `studies.*` — CRUD for study items
- `pdfs.*` — CRUD for PDF library + search
- `cornellNotes.*` — Cornell note CRUD + AI sync
- `ai.chat` — AI Q&A with RAG over studies/PDFs
- `conversations.*` — persistent chat history
- `liveTranscripts.*` — live recording session storage
- `journalEntries.*` — spiritual journal CRUD

## Environment Variables (server/.env)
```
DATABASE_URL=mysql://...@<hetzner-ip>:3306/bible_study_pro
OPENROUTER_API_KEY=sk-or-v1-...
YOUTUBE_API_KEY=...
```

## Running the App
```bash
cd '/Users/finessejones1/Downloads/bible-study-pro 2'
pnpm run dev
```
Server starts on port 5001.

## What Hermes Can Do With This App
1. Read and modify any file in the app
2. Search the web for theology, IOG teachings, scripture references
3. Run `pnpm run check` to validate TypeScript
4. Run `pnpm run dev` to start the dev server
5. Query the app's tRPC API at `http://localhost:5001/trpc/...`
6. Upload PDFs by calling `pdfs.create` router
7. Crawl IOG content at theisraelofgod.com
