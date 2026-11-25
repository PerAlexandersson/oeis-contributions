# Guide for agents

Agents may add and update proposals by pull request. Read the [README](README.md) and the
[template](proposals/TEMPLATE.toml) first.

## Rules

- **Never submit to the OEIS.** Prepare text only. A person submits and records the outcome.
- **Public material only.** Do not add unpublished results, private notes or private repository
  names unless the owner of that material has explicitly approved publication here.
- **Check the live entry first.** For additions and corrections, read the current OEIS entry and
  quote what you are changing. For new sequences, search the OEIS for the first terms and for the
  row sums (or another natural statistic) and record the searches and date in `oeis_search`.
- **Reproducible data.** Every proposal that contains terms needs a generator in `generators/`
  that prints them exactly; the validator compares the two.
- **OEIS style.** Follow the [OEIS style sheet](https://oeis.org/wiki/Style_Sheet): plain text or
  OEIS markup, no LaTeX in `%N`; data lines within the length limit; offsets as the entry uses them.
  State conjectures as conjectures.
- **Evidence.** Set `evidence` honestly (`proved`, `proof-draft`, `experimental`, `conjectural`)
  and cite sources with exact theorem numbers.
- **One proposal per file**, named `<A-number or new>-<short-slug>.toml`.
- Run `python3 scripts/validate.py --index` before opening the pull request.
