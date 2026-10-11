# PM Cockpit packs catalog

The list of packs (add-ons) that PM Cockpit's **Add-ons** screen shows. The app reads [`packs.yaml`](packs.yaml) from
this repository's `main` branch, at its raw address:

```
https://raw.githubusercontent.com/skywalkr2/PMCockpit-Catalog/main/packs.yaml
```

Release builds of PM Cockpit carry that address (the `PACK_CATALOG` repository variable of the app's repository). A
workspace can turn the catalog off or add its own catalogs in its settings (`workspace.plugins.catalog`).

## What the app does with an entry

- It shows the name, summary, publisher, price and how to get the pack, as **plain text**: nothing here is ever
  treated as an instruction, and only the `homepage` becomes a link, shown with its real domain.
- It writes **what the pack adds, reaches and keeps** from the entry's `provides` and `requires`, the same summary a
  person approves when turning the pack on. Copy both from the pack's `plugin.yaml` exactly; if they disagree with
  the installed pack, the installed pack's own manifest is what people approve.
- It prices each of the pack's typical **AI jobs** (`ai_jobs`) on the person's own accounts and prices, or shows the
  size of the work when the price isn't known.
- It reads this file only when someone opens the Add-ons screen or presses Refresh, with a plain request that carries
  nothing about them, and keeps a copy for offline use.

## The format

```yaml
version: 1
packs:
  - id: bindery                       # the pack's plugin name, lowercase letters, digits and dashes
    name: Bindery pack                # up to 80 characters
    summary: One line on what it does # up to 300
    publisher: Who makes it           # up to 80
    maintainers: true                 # made by PM Cockpit's maintainers (false for a third party)
    updated: "2030-03-01"
    version: 1.2.0                    # the latest version
    plugin_api: ">=0.3,<0.4"          # as in its plugin.yaml
    price:
      model: subscription             # free, one_time, subscription or see_publisher
      amount: 9                       # for one_time and subscription
      currency: USD                   # three letters
      period: month                   # month or year, for a subscription
      note: Free for your first book  # optional, up to 200
    homepage: https://example.com/bindery   # https only
    install: uv tool install --with bindery-pack pm-cockpit   # what to run, or a short instruction
    demo: true                        # it ships made-up data for `cockpit demo --plugin bindery`
    ai_jobs:                          # its typical AI work; up to 20
      - {label: Drafting a chapter, input_tokens: 6000, output_tokens: 4000}
      - {label: A full edit pass, input_tokens: 90000, output_tokens: 30000, role: check, data_level: restricted}
    provides: {...}                   # copied from plugin.yaml
    requires: {...}                   # copied from plugin.yaml
```

`role` is `write`, `check` or `research` (default `write`); `data_level` is `open`, `internal` or `restricted`
(default `internal`).

**Private packs.** A pack whose package isn't public can still be listed: give an `install` line that says how to
get it ("Ask the publisher for the package file, then: uv tool install --with <the file> pm-cockpit") and a
`see_publisher` price. Listing is a choice: an entry here is public even when the pack isn't.

## Being listed

- Packs are listed by the process in [PUBLISHING.md](PUBLISHING.md): the pack's builder asks, the PM Cockpit host
  session checks and opens a pull request, and the owner merges it. Nobody else writes to `main`.
- For now the catalog lists only packs made by PM Cockpit's maintainers.
- The check on every change reads the file exactly as the app does and fails on any entry the app would leave out,
  any id listed twice, or anything it can't read.
- Keep entries current: a new version, a new price or a change to what a pack provides or requires is a change here.
