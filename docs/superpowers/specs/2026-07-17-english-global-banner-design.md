# English-first repository and banner design

Date: 2026-07-17

## Goal

Reposition `sci-ssci-skills` for a global research audience while preserving a complete Chinese entry point. Add an original, immediately legible GitHub banner that communicates the project's task, corpus funnel, and scientific-fidelity boundary.

## Documentation architecture

- Make `README.md` the canonical English landing page.
- Move the current Chinese landing page to `README_CN.md` and keep it fully functional.
- Add reciprocal language links near the top of both files.
- Keep all supporting methodology, benchmark, example, corpus, Skill, and code files in English.
- Use concise global positioning: `Polish the writing. Preserve the science.`
- State the corpus claim precisely as `1,000-paper metadata pool -> 200-paper shortlist -> 60-paper core corpus`; never imply that 1,000 full texts were downloaded or used for model training.

## Banner design

- Asset: original raster GitHub README banner, maximum 3:1 aspect ratio, saved under `assets/`.
- Visual tone: premium scientific editorial design, dark navy-to-indigo field, restrained cyan/violet highlights, clean typography, no imitation of the Nature wordmark or repository artwork.
- Primary hierarchy: `1,000 HIGH-QUALITY PAPERS. ONE SCI/SSCI POLISHING SKILL.`
- Supporting message: `Polish the writing. Preserve the science.`
- Visual story: manuscript text moving through a refined editorial layer while protected scientific tokens remain locked; `1,000` is the only corpus number shown; subtle cross-disciplinary nodes provide context without competing with the headline.
- Keep the `1,000 -> 200 -> 60` funnel in searchable README text for methodological transparency, not in the banner.
- Avoid: publisher logos, journal covers, fake seals, dense prose, decorative screenshots, watermarks, and claims of guaranteed publication.
- The banner must remain understandable at GitHub README width and should not be the sole location of any essential factual claim.

## Integration

- Place the banner at the top of both language READMEs.
- Keep installation, use cases, corpus transparency, evaluation limitations, copyright boundaries, and license information as searchable HTML text below it.
- Verify every relative link after renaming the Chinese README.

## Validation

- Inspect the generated banner for exact text, visual hierarchy, cropping, and legibility.
- Confirm the image is stored in the repository and referenced by both READMEs.
- Run Markdown-link validation, Skill validation, unit tests, corpus integrity checks, sensitive-value scanning, and clean remote-style installation discovery.
- Review the final Git diff before committing and pushing.
