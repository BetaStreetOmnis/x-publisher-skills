# x-publisher-skills

A public collection of reusable Codex/CLI skills for publishing workflows.

## Included Skills

### `xhs-auto-publisher`

Drive the local `xhs_ai_publisher` project as an automation backend for Xiaohongshu/Rednote publishing.

Capabilities:
- start or reuse the local Web publishing service
- verify Xiaohongshu login state
- run preview publish without final submission
- run controlled real publish when explicitly requested

Location:
- `xhs-auto-publisher/`

## Structure

```text
x-publisher-skills/
├── README.md
└── xhs-auto-publisher/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/
```

## Notes

- These skills are designed to be copied or linked into a Codex skills directory.
- Some skills may reference local projects or runtime paths and should be adjusted for other machines.
