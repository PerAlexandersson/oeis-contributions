# Proposal fields

The validator (`scripts/validate.py`) enforces these rules; the [template](../proposals/TEMPLATE.toml)
shows every field.

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Equals the file name without `.toml`. |
| `kind` | yes | `new-sequence`, `comment`, `formula`, `example`, `program`, `link`, `crossref`, `bfile` or `correction`. |
| `target` | yes | An A-number, or `new` for a new sequence until it is accepted. |
| `also_targets` | no | Further A-numbers receiving the same edit. |
| `status` | yes | `draft`, `ready`, `submitted`, `accepted` or `withdrawn`. |
| `evidence` | yes | `proved`, `proof-draft`, `experimental` or `conjectural`. |
| `summary` | yes | One line, shown in the index. |
| `authors` | yes | Names as they should appear in the OEIS. |
| `submitted`, `a_number` | when submitted / accepted | Date sent; assigned or edited A-number. |
| `notes` | no | Reviewer notes; not submitted. |
| `[oeis_search]` | new sequences | `date`, `queries`, `result` of the OEIS searches. |
| `[data]` | when terms are given | `generator`, `args`, `offset`, `layout` (`list`, `tabl`, `tabf`), `terms` (at most about 260 characters). The validator reruns the generator and compares. |
| `[oeis]` | new sequences and additions | Text blocks to paste: `name`, `comments`, `formulas`, `example`, `programs`, `links`, `crossrefs`, `keywords`. Plain text or OEIS markup; no TeX in `name`. |
| `[correction]` | corrections | The field, the old text and the new text, and an `editor_note`. |
