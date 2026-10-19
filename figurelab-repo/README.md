# FigureLab

FigureLab is a scientific data-processing and figure-generation project focused on materials-characterisation workflows such as XRD, FTIR/Raman spectroscopy, and TGA/DSC.

The repository is intentionally structured so that scientific processing is kept separate from plotting/UI code. This makes calculations testable, reproducible, and easier to review as the project grows.

## Repository structure

```text
figurelab/
├── .github/workflows/      # CI checks
├── docs/                   # product, scientific-method and architecture notes
├── sample_data/            # small, non-sensitive test/example datasets
├── src/figurelab/
│   ├── io/                 # data import and format parsers
│   ├── xrd/                # XRD processing and analysis
│   ├── spectroscopy/       # FTIR, Raman and related spectral workflows
│   ├── thermal/            # TGA/DSC workflows
│   ├── plotting/           # reusable plotting/export logic
│   ├── recipes/            # reproducible processing recipes
│   └── projects/           # samples, experiments and project-level context
├── tests/                  # automated tests
├── pyproject.toml
└── LICENSE.md
```

## Development setup

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"
pytest
```

## Design principles

1. **Scientific calculations are testable.** Analysis code should not be embedded directly in UI callbacks.
2. **Raw data remains traceable.** Processing steps should be represented explicitly rather than silently mutating source data.
3. **Recipes are reproducible.** A saved workflow should record processing steps and parameters.
4. **Instrument import is modular.** Native format parsers should live under `figurelab.io` and be added based on real user demand.
5. **Figures are outputs, not the source of truth.** Plot styling should be separate from quantitative analysis.

## Current status

This is a starter repository scaffold. Technique-specific scientific methods should only be added with documented assumptions, references, validation datasets and tests.

## Suggested first milestones

- Add representative XRD, FTIR/Raman and TGA/DSC example files.
- Implement a canonical internal dataset model.
- Port existing FigureLab analysis functions into the appropriate technique modules.
- Add regression tests against trusted calculations/software outputs.
- Define a recipe schema for processing provenance.
- Add publication export and experiment-comparison workflows only after the analysis layer is covered by tests.

## Licence

Copyright retained by the project owner. See `LICENSE.md`.
