# OEIS contributions

A public worklist of proposed contributions to the [OEIS](https://oeis.org): new sequences,
comments, formulas, b-files, cross-references and corrections. Each proposal is one TOML file in
[`proposals/`](proposals/) with the exact text to paste into the OEIS editor, the evidence behind
it, and (for data) a generator that reproduces every term.

The repository makes contributions easy to review, reproduce and submit, by people and by agents.
Nothing here is submitted automatically: a proposal is sent to the OEIS by a person, who then
records the outcome in the file.

## Layout

| Path | Contents |
|---|---|
| [`proposals/`](proposals/) | One file per proposal; see the [template](proposals/TEMPLATE.toml). |
| [`generators/`](generators/) | Small, dependency-free scripts that print the terms of a proposal. |
| [`schema/`](schema/) | The field reference used by the validator. |
| [`scripts/validate.py`](scripts/validate.py) | Checks every proposal, regenerates data, writes b-files and the index. |
| [`PROPOSALS.md`](PROPOSALS.md) | Generated index of all proposals by status. |

## Proposal life cycle

`draft` → `ready` (text, evidence and data checked; ready to paste) → `submitted` (sent to the
OEIS, with the date) → `accepted` (A-number or edit approved) or `withdrawn` (with a reason).

## Kinds of proposal

- `new-sequence`: a complete new entry (`%N`, `%S/%T/%U` data, `%O`, `%K`, comments, formulas,
  example, program, links, cross-references, author).
- `comment`, `formula`, `example`, `program`, `link`, `crossref`: an addition to an existing entry.
- `bfile`: a new or extended b-file, generated from a script in `generators/`.
- `correction`: a fix to an existing entry, with the old and new text.

## Evidence levels

`proved` (a published or public proof is cited), `proof-draft` (a written but unpublished proof),
`experimental` (verified for a stated finite range), `conjectural`. Comments that state an
unproved property say so explicitly, as the OEIS requires.

## Checking locally

```sh
python3 scripts/validate.py            # validate all proposals and regenerate data
python3 scripts/validate.py --index    # also rewrite PROPOSALS.md
python3 scripts/validate.py --bfiles out/   # write b-files for proposals with generators
```

Python 3.11 or later; no third-party packages.

## Contributing

Open a pull request that adds or edits a file in `proposals/`. Agents should read
[AGENTS.md](AGENTS.md) first.

## License

Proposal text and data are released under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the license of the OEIS.
Scripts are released under the MIT license. See [LICENSE](LICENSE).
