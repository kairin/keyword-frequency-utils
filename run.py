"""Keyword frequency utility.

This script scans a directory for .txt files containing comma-separated
keywords, normalizes tokens by default (strip + lower), counts frequencies
across files, writes a CSV, and optionally saves a bar chart PNG.

This project prefers using the UV package manager for environment setup.
Usage example (from repo root):

  curl -LsSf https://astral.sh/uv/install.sh | sh
  uv sync --dev
  uv run python run.py --input-dir . --top 20

"""

from pathlib import Path
# argparse intentionally omitted; script runs with default behaviour
import logging
from collections import Counter

# Use non-interactive backend early to avoid GUI backend errors on headless CI
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


logger = logging.getLogger(__name__)


def collect_keywords_from_file(path: Path, normalize: bool = True):
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        # Fallback: read with latin-1 to avoid crashing on mixed encodings
        text = path.read_text(encoding='latin-1')

    tokens = [t.strip() for t in text.split(',')]
    if normalize:
        normalized = [t.lower() for t in tokens if t]
    else:
        normalized = [t for t in tokens if t]
    # filter out empty strings
    return [t for t in normalized if t]


def aggregate_keywords(input_dir: Path, normalize: bool = True):
    all_keywords = []
    for p in sorted(input_dir.glob('*.txt')):
        try:
            kws = collect_keywords_from_file(p, normalize=normalize)
            all_keywords.extend(kws)
        except Exception as e:
            logger.warning('Failed to read %s: %s', p, e)
    return Counter(all_keywords)


def save_csv(counter: Counter, out_csv: Path):
    df = pd.DataFrame(counter.items(), columns=['Keyword', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)
    df.to_csv(out_csv, index=False)
    logger.info('Saved CSV: %s', out_csv)
    return df


def save_plot(df: pd.DataFrame, out_png: Path, top: int = 20):
    top_df = df.head(top)
    plt.figure(figsize=(12, 8))
    plt.bar(top_df['Keyword'], top_df['Frequency'], color='skyblue')
    plt.xlabel('Keyword')
    plt.ylabel('Frequency')
    plt.title(f'Top {top} Keyword Frequencies')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()
    logger.info('Saved plot: %s', out_png)


def _run_default():
    """Run the default behaviour: scan current directory and write outputs.

    This intentionally avoids CLI flags and runs with sensible defaults so
    the script can be executed directly (as the user requested).
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s',
    )
    input_dir = Path('.')
    out_csv = Path('keyword_frequency.csv')
    out_png = Path('top_keywords_bar_chart.png')

    logger.info('Scanning directory: %s', input_dir.resolve())
    counter = aggregate_keywords(input_dir, normalize=True)

    if not counter:
        logger.info('No keywords found. Writing empty CSV and exiting.')
        save_csv(counter, out_csv)
        return

    df = save_csv(counter, out_csv)
    try:
        save_plot(df, out_png, top=20)
    except Exception as e:
        logger.warning('Plot generation failed: %s', e)


if __name__ == '__main__':
    _run_default()
