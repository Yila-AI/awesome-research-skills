# Rendering and editable-output guidance

## Preferred output

Deliver native editable text, tables, shapes, and charts whenever the host supports them. Embed source figures only when native reconstruction would risk changing the data; include the source crop and source map.

## Fonts

Use fonts available in the target environment. Prefer a CJK-capable sans family for Chinese text and a stable Latin fallback. Record the selected font in `run-log.md`. Test Chinese, Latin, math symbols, minus signs, and monospaced numbers in a smoke slide before the full build.

## Render loop

1. Export PPTX to PDF with the environment's Office renderer.
2. Rasterize each PDF page to PNG at a reviewable resolution.
3. Inspect full-size slides for clipping, missing glyphs, unexpected wrapping, stretched figures, and low contrast.
4. Rebuild and re-render after each substantive repair.

## Fallbacks

If the host cannot export an editable PPTX, provide the best supported format and state the limitation. A PDF or PNG deck must never be labelled editable. If a renderer lacks a Chinese font, keep the source PPTX, record the fallback, and recommend opening it in PowerPoint/Keynote with a CJK font installed.
