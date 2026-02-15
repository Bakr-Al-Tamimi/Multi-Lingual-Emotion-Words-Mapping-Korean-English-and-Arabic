```markdown
# Multi-Lingual Emotion Words Mapping: Korean, English, and Arabic

## Overview
This project expands upon the **EVOKE (Emotion Vocabulary Of Korean and English)** dataset by introducing an Arabic translation layer. EVOKE is a comprehensive, parallel dataset of emotion vocabulary that provides many-to-many translations between Korean and English. By incorporating Arabic counterparts using automated translation workflows, this repository aims to broaden the cross-linguistic scope of emotion semantics for natural language processing (NLP), psycholinguistics, and computational linguistics.

## Features
- Extends the existing Korean-English emotion dataset with Arabic translations.
- Handles automated bulk translation utilizing the `deep-translator` library to ensure robust API interaction.
- Retains proper encoding (`utf-8-sig`) for RTL (Right-to-Left) language support in standard spreadsheet software like Microsoft Excel.
- Implements delays and error handling to respect external translation API rate limits.

## Installation & Setup

1. **Clone or Download the Repository**
   Ensure all project files, including the base dataset (`Emotion_Words_Combined_Clean.csv`), are in your working directory.

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate

```

3. **Install Dependencies**
```bash
pip install pandas deep-translator

```



## Usage

1. **Verify the Environment:** Run the verification script to ensure dependencies are installed and the dataset is present.
```bash
python verify_env.py

```


2. **Execute the Translation:** Run the main script to process the CSV file. Progress will be printed to the console.
```bash
python main.py

```


*The output will be saved as `Emotion_Words_Combined_Arabic.csv`.*

## Acknowledgments and References

This project builds directly upon the foundational work provided by the EVOKE dataset authors. For more information on the original dataset, theory, and linguistic properties mapped in their study, please refer to the following resources:

### Primary References

* **Original Repository:** [EVOKE GitHub Repository](https://github.com/yoonwonj/EVOKE/tree/main)
* **Preprint Publication:** Jung, Y., Shin, H., & Bergen, B. K. (2026). *EVOKE: Emotion Vocabulary Of Korean and English*. [PDF link via arXiv](https://arxiv.org/pdf/2602.10414)

### Academic Citation for EVOKE

If utilizing the foundational Korean-English mapping in academic work, please cite the original authors using the proper academic formatting:

> Jung, Y., Shin, H., & Bergen, B. K. (2026). EVOKE: Emotion Vocabulary Of Korean and English. *arXiv preprint arXiv:2602.10414*.
> **Subjects:** Computation and Language (cs.CL)
> **Cite as:** [arXiv:2602.10414 [cs.CL]](https://www.google.com/search?q=https://arxiv.org/abs/2602.10414) (or arXiv:2602.10414v1 [cs.CL] for this version)
> **DOI:** [https://doi.org/10.48550/arXiv.2602.10414](https://doi.org/10.48550/arXiv.2602.10414)

### Further Knowledge Resources

* **[Deep-Translator Documentation](https://deep-translator.readthedocs.io/):** A flexible python package to translate text across multiple providers.
* **[Pandas Documentation](https://pandas.pydata.org/docs/):** Core library utilized for the CSV data manipulation.
* **[Computation and Language (cs.CL) on arXiv](https://arxiv.org/list/cs.CL/recent):** Keep up to date with the latest publications in natural language processing and computational linguistics.

```

```