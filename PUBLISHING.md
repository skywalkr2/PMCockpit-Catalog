# Publishing a pack

Packs are listed here by one set process. A plugin's own builder never writes to this repository: the PM Cockpit
host session opens the pull request, and the owner decides by merging it. The same steps are in PM Cockpit's plugin
developer guide ("Publishing a pack").

## 1. Release it in its own repository

- Raise the version in `plugin.yaml` and in the package's own metadata.
- Say what changed, in a changelog or the release notes.
- Run its tests, tag the release (`v1.2.0`), and let its own checks build the package from the tag.

## 2. Write its catalog entry

Keep it in the pack's repository as `catalog/pack.yaml`, in the format in this repository's [README](README.md):

- `provides` and `requires` copied **exactly** from `plugin.yaml`;
- its price and how to get it (for a private pack: "Ask the publisher for the package file, then: uv tool install
  --with <the file> pm-cockpit", and price model `see_publisher`);
- its typical AI jobs, so the app can price them on each person's own accounts.

## 3. Check it

```sh
cockpit pack check <the pack's plugin folder> --entry catalog/pack.yaml
```

Run it with the host at a version the pack declares. It checks that the manifest reads and fits the host, that the
pack loads in a throwaway demo workspace, and that the entry fits this catalog's format and matches `plugin.yaml` as
written. Every line must pass.

## 4. Ask for it to be published

Add a section to the pack repository's `docs/host-questions.md`:

```
# Publish request N (not yet sent, YYYY-MM-DD)

- Pack: <id>, version <x.y.z>, tag <vx.y.z>
- What changed: <a few lines>
- Listing: the owner has said it may be listed publicly: yes / not yet
- Check output:
  <the lines `cockpit pack check` printed>
```

Then tell the host's session with one short message.

## 5. The host verifies and proposes

The host's session:

- runs the check itself, runs the pack's tests, and tries it in the demo sandbox (`cockpit demo --plugin`);
- opens a pull request here with the entry, saying what the pack adds, reaches and keeps, and what it asks for that
  its last listing didn't;
- when the pack's own repository is private, puts the release's package file in this repository's `releases/` folder,
  checked against the release's own checksum, and points the entry's `release.url` at its raw address on `main`, so
  the app installs it with no access key (owner, 2026-10-28). Only the package file is public; the pack's repository
  stays private;
- or answers the request with what to fix.

## 6. The owner decides

The pack is listed when the owner merges the pull request, never before. An update (a new version, a new price, a
change to what it provides or requires) follows the same path.
