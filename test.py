'''
To test using custom config.yaml file use commands:

Process entire directories of files with a single command:
 Parse all documents in a directory
    synthetic-data-kit -c config.yaml ingest ./resources/
        # Processes all .pdf, .html, .docx, .pptx, .txt files
        # Saves parsed text files to data/parsed/

Generate QA pairs for all text files
    synthetic-data-kit -c config.yaml create ./data/parsed/ --type qa
        # Processes all .txt files in the directory
        # Saves QA pairs to data/generated/

# Curate all generated files
    synthetic-data-kit curate ./data/generated/ --threshold 8.0
        # Processes all .json files in the directory
        # Saves curated files to data/curated/

# Convert all curated files to training format
    synthetic-data-kit save-as ./data/curated/ --format alpaca
        # Processes all .json files in the directory
        # Saves final files to data/final/
'''