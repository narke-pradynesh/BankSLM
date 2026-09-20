# Dataset Creation with Synthetic Data Kit

Temporary guide for generating the BankSLM training dataset using `synthetic-data-kit` and the repository-provided `config.yaml`.

## 1. Prerequisites

Make sure `synthetic-data-kit` is installed and available in the current environment.

From the repository root:

```bash
synthetic-data-kit --help
```

Verify the installation and environment using:

```bash
synthetic-data-kit system-check
```

If using the repository-specific configuration, the configuration file is:

```text
./config.yaml
```

All commands that require the custom configuration should explicitly use:

```bash
-c config.yaml
```

This ensures that the configuration in the current repository is used instead of relying on a global/default configuration.

---

## 2. Dataset Directory Structure

The expected directory structure is:

```text
.
├── config.yaml
├── resources/
│   └── <source documents>
│
└── data/
    ├── parsed/
    ├── generated/
    ├── curated/
    └── final/
```

### Directory purpose

| Directory         | Purpose                                                      |
| ----------------- | ------------------------------------------------------------ |
| `resources/`      | Source documents such as PDF, HTML, DOCX, PPTX and TXT files |
| `data/parsed/`    | Parsed text extracted from source documents                  |
| `data/generated/` | Generated QA pairs                                           |
| `data/curated/`   | QA pairs that pass the curation threshold                    |
| `data/final/`     | Final dataset converted to the required training format      |

---

## 3. Use the Repository `config.yaml`

The repository contains a custom `config.yaml` for dataset generation.

Use the configuration explicitly with:

```bash
-c config.yaml
```

For example:

```bash
synthetic-data-kit -c config.yaml ingest ./resources/ -o ./data/input
```

**Note:** The `-c config.yaml` option should be used for commands that need the custom repository configuration.

---

## 4. Parse All Source Documents

Process the entire `resources/` directory with a single command:

```bash
synthetic-data-kit -c config.yaml ingest ./resources/ -o ./data/input
```

This processes supported files such as:

```text
.pdf
.html
.docx
.pptx
.txt
```

The parsed text files are saved to:

```text
data/parsed/
```

Expected flow:

```text
resources/
    │
    ├── document1.pdf
    ├── document2.pdf
    ├── document3.docx
    └── ...
            │
            ▼
synthetic-data-kit ingest
            │
            ▼
data/parsed/
```

---

## 5. Generate QA Pairs

Generate question-answer pairs from all parsed text files:

```bash
synthetic-data-kit -c config.yaml create ./data/parsed/ -o ./data/output --type qa
```

This:

* Processes all `.txt` files in `data/parsed/`
* Generates QA pairs
* Saves the generated JSON files to:

```text
data/generated/
```

Expected flow:

```text
data/parsed/
    │
    ├── document1.txt
    ├── document2.txt
    └── ...
            │
            ▼
synthetic-data-kit create --type qa
            │
            ▼
data/generated/
```

---

## 6. Curate Generated QA Pairs

Curate all generated JSON files using the specified quality threshold:

```bash
synthetic-data-kit curate ./data/generated/ -o ./data/curated --threshold 8.0
```

This:

* Processes all `.json` files in `data/generated/`
* Applies the curation threshold of `8.0`
* Saves the curated files to:

```text
data/curated/
```

---

## 7. Convert to Training Format

Convert all curated datasets into the Alpaca training format:

```bash
synthetic-data-kit save-as ./data/curated/ -o ./data/final --format alpaca
```

This:

* Processes all `.json` files in `data/curated/`
* Converts them to Alpaca format
* Saves the final training files to:

```text
data/final/
```

---

## 8. Complete Dataset Generation Workflow

The complete workflow is:

### Step 1 — System Check

```bash
synthetic-data-kit system-check
```

### Step 2 — Parse Documents

```bash
synthetic-data-kit -c config.yaml ingest ./resources/
```

### Step 3 — Generate QA Pairs

```bash
synthetic-data-kit -c config.yaml create ./data/parsed/ --type qa
```

### Step 4 — Curate QA Pairs

```bash
synthetic-data-kit curate ./data/generated/ --threshold 8.0
```

### Step 5 — Convert to Alpaca Format

```bash
synthetic-data-kit save-as ./data/curated/ --format alpaca
```

---

## 9. Pipeline Overview

```text
                    Source Documents
                           │
                           ▼
                     resources/
                           │
                           │ ingest
                           ▼
                      data/parsed/
                           │
                           │ create --type qa
                           ▼
                    data/generated/
                           │
                           │ curate
                           │ threshold = 8.0
                           ▼
                     data/curated/
                           │
                           │ save-as
                           │ format = alpaca
                           ▼
                       data/final/
                           │
                           ▼
                  Training Dataset
```

## 10. Quick Start

From the repository root, run:

```bash
# Verify installation/environment
synthetic-data-kit system-check

# Parse source documents
synthetic-data-kit -c config.yaml ingest ./resources/

# Generate QA pairs
synthetic-data-kit -c config.yaml create ./data/parsed/ --type qa

# Curate generated QA pairs
synthetic-data-kit curate ./data/generated/ --threshold 8.0

# Convert to Alpaca training format
synthetic-data-kit save-as ./data/curated/ --format alpaca
```

After completion, the final training dataset will be available under:

```text
data/final/
```

## Notes

* Run the commands from the repository root.
* Keep the repository-specific `config.yaml` in the project root.
* Use `-c config.yaml` to explicitly load the repository configuration.
* Do not commit API keys or other secrets to `config.yaml`.
* The directories `data/parsed/`, `data/generated/`, `data/curated/`, and `data/final/` should be treated as intermediate/final dataset artifacts.
