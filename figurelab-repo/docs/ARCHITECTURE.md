# FigureLab architecture

## Separation of concerns

FigureLab should distinguish four layers:

1. **Import** — read instrument or tabular files and preserve source metadata.
2. **Scientific processing** — perform explicit, testable transformations and calculations.
3. **Experiment/project context** — relate measurements to samples, experimental series and processing recipes.
4. **Presentation** — plots, tables, reports and publication exports.

This prevents scientific results from depending on UI state and makes methods easier to validate.

## Data flow

```text
Raw instrument file
        ↓
Parser / import adapter
        ↓
Canonical measurement representation
        ↓
Explicit processing recipe
        ↓
Technique-specific results
        ↓
Comparison / project context
        ↓
Plot / table / publication export
```

## Native instrument formats

Add parsers based on actual files received from researchers. Each parser should have fixtures and tests using redistributable or synthetic sample files.
