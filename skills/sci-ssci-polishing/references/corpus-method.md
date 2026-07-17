# Corpus and distillation method

## V2 selection design

V2 uses a staged, frozen design:

1. build a metadata pool of 1,000 high-quality papers: 500 SCI and 500 SSCI;
2. screen a balanced shortlist of 200 papers;
3. select 60 papers across nine portfolio clusters;
4. assign 40 to rule distillation, 10 to calibration, and 10 to a sealed blind set;
5. acquire and analyze only distillation material before fixing the Skill;
6. calibrate without using blind material, freeze the Skill hash, and only then unseal blind papers.

The final 60 contains 30 SCI and 30 SSCI papers. SCI covers clinical/observational medicine, life/general science, chemistry/materials/environment, and computing/engineering. SSCI covers psychology/behavior, education/learning, communication/media, management/organization, and business/marketing/information systems.

The 40-paper distillation split contains 20 SCI and 20 SSCI papers from 28 journals. Aggregate extraction yielded 1,750 usable paragraphs and 220,158 words. Twelve newly acquired papers used lawful Europe PMC JATS, sixteen used lawful institutional access, one used an institutional repository, and one used a publisher OA PDF. Earlier pilot papers supply the rest of the 40-paper split. Copyrighted full text and private extraction remain outside the public Skill.

## What “distillation” means

This is not model training and does not copy journal prose. Distillation means:

1. identify recurring rhetorical functions and section structures;
2. compare how those functions vary across SCI and SSCI writing;
3. abstract reusable editing and preservation rules;
4. encode output and refusal contracts;
5. test the fixed rules on calibration and sealed blind material.

## V2 aggregate observations

- Rhetorical function is a stronger editing router than journal prestige or a generic SCI/SSCI label.
- Methods reward stable terminology and procedural order; Results keep evidence adjacent to claims; Discussion requires explicit separation of finding, interpretation, and implication.
- SSCI material uses more hedging in aggregate, but marker counts are descriptive signals rather than targets.
- SCI material contains denser technical entities and more first-person procedural statements in this sample; that does not justify adding first-person language where the source lacks it.
- Sentence and paragraph length vary substantially within both families. Length is therefore a diagnostic, never a template.
- Complete-section polishing needs a paragraph move map; sentence-level fluency alone cannot repair cross-paragraph progression safely.

## Selection and acquisition safeguards

- Match inaccessible replacements on index family, portfolio cluster, and training/calibration role.
- Prefer lawful OA or institutional access and record provenance for every file.
- Keep full text private and publish only metadata, aggregate observations, synthetic examples, and evaluation summaries.
- Never treat impact factor, citation count, or publication venue as proof that every sentence is an ideal template.

## Limitations

- Published articles show successful final prose, not editorial before/after decisions.
- The corpus cannot represent every discipline, article type, journal, English variety, or qualitative tradition.
- PDF extraction is noisier than JATS and may affect aggregate marker counts.
- Corpus evidence supports conservative cross-paper rules, not deterministic journal imitation or guaranteed acceptance.
