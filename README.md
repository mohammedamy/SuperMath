# SuperMath — revised practice draft

This package updates the existing static GitHub Pages project. It contains the revised site, 4,250 active bilingual practice questions, scripts and the review record.

**Read `review/README.md` before publishing.** Quantity and software checks pass, but complete item-by-item examination fidelity and mathematical review are unfinished. The 2,210 added items are explicitly tagged parameterized practice variants.

## Apply the update

Copy the contents of this package into a working copy of `mohammedamy/SuperMath`, preserving the folders and replacing the corresponding files. Review the changes before committing and publishing with the repository’s normal GitHub Pages process. The package has not been pushed to GitHub.

The site uses `index.html`, `LOGO.jpg`, `assets/` and `data/`. Keep those paths relative so it works beneath `/SuperMath/`. Serve it over HTTP; opening `index.html` directly as a local file can prevent the JSON banks from loading.

## Validate

From the project directory:

```sh
python scripts/audit_banks.py
python scripts/validate_banks.py
node scripts/test-runtime.cjs
```

The scripts use Python’s and Node’s standard libraries. The site retains its original CDN dependencies for Tailwind, Chart.js, MathJax and fonts.

## Content maintenance

- Final active banks are `data/*.json`.
- `review/quarantined-items.json` preserves 700 excluded original records with reasons.
- `review/corrections.json` records individual corrections and ID changes.
- `review/item-audit.json` covers every active item; `baseline-summary.json` describes the original banks.
- `review/expansion-summary.json` distinguishes retained questions from new practice families/variants.
- `scripts/build_practice.py` can reconstruct the generated additions while retaining legacy records. It is optional, not required to install the update. Run `scripts/add_question_diagrams.py` afterward and repeat validation if you regenerate.
- Older root-level injection/generation scripts in the original repository can overwrite these corrections and should not be used to rebuild this revision.

Written responses are self-assessed against worked solutions, not automatically scored as mathematical proofs.
