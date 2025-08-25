import tempfile
from pathlib import Path
from run import collect_keywords_from_file, aggregate_keywords, save_csv


def test_collect_and_aggregate(tmp_path):
    d = tmp_path
    # create two text files with comma-separated keywords
    p1 = d / 'a.txt'
    p1.write_text('Cat, Dog, bird')
    p2 = d / 'b.txt'
    p2.write_text('dog, fish, cat,')

    counter = aggregate_keywords(d)
    # normalize lower-casing expected
    assert counter['cat'] == 2
    assert counter['dog'] == 2
    assert counter['bird'] == 1
    assert counter['fish'] == 1

    out_csv = d / 'out.csv'
    df = save_csv(counter, out_csv)
    assert out_csv.exists()
    # check dataframe columns
    assert 'Keyword' in df.columns
    assert 'Frequency' in df.columns
