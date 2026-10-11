# PM Cockpit packs catalog

This repository holds one file the app reads, `packs.yaml`, plus its README and a check.

- The format is PM Cockpit's (design 3.11, `engine/packs.py` in skywalkr2/ProjectManagementAgent). Change the format
  there first; this file follows.
- `provides` and `requires` are copied exactly from each pack's `plugin.yaml`; never describe a pack as reaching or
  keeping less than it does.
- Only packs made by PM Cockpit's maintainers are listed for now, and only when the owner says so: an entry here is
  public, even for a private pack.
- No personal data, secrets or private addresses. Every change passes `check.py`.
- Packs are listed only by the process in PUBLISHING.md: changes arrive as pull requests from the PM Cockpit host
  session, and the owner merges them. Never push an entry to `main` directly.
