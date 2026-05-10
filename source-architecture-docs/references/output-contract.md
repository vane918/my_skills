# Output Contract

Produce synchronized Markdown and HTML artifacts in the requested output directory.

## Recommended File Layout

```text
output/
├── architecture-report.md
├── architecture-artifact.html
└── assets/
    ├── architecture-overview.png
    ├── architecture-<subsystem>.png
    └── ...
```

Use the user's requested names if they provide them. Otherwise use the names above.

## Markdown Report Structure

`architecture-report.md` should include:

1. Title and scope
2. Executive architecture summary
3. Source inputs inspected
4. System context
5. Component inventory table
6. Whole-system architecture diagram image
7. Local architecture diagram images
8. Data/control flow summary
9. Core flowcharts as Mermaid
10. Core sequence diagrams as Mermaid
11. Interface catalog
12. Deployment/runtime notes
13. Risks, bottlenecks, and coupling points
14. Open questions / verification gaps
15. Appendix: Image Gen prompts and diagram source

Markdown should be AI-friendly:

- Include exact file paths for evidence.
- Keep diagrams as Markdown image links and Mermaid code blocks.
- Keep generated-image prompts in text.
- Prefer tables for components, interfaces, flows, and evidence.

## HTML Artifact Structure

`architecture-artifact.html` should be a self-contained presentation document except for local image assets.

Required sections:

- Overview header with project name, scope, and generation date.
- Navigation sidebar or top navigation.
- Architecture overview with generated image.
- Component map.
- Local subsystem sections with generated images.
- Core flowcharts rendered from Mermaid.
- Sequence diagrams rendered from Mermaid.
- Evidence and open questions section.

HTML design requirements:

- Use a clear technical presentation layout, not a marketing landing page.
- Keep diagrams large and readable.
- Use restrained colors and high contrast.
- Avoid nested cards and decorative backgrounds.
- Keep text concise enough for live explanation.
- Do not hide important evidence behind hover-only interactions.

## Synchronization Rules

- Every image in HTML must also be referenced in Markdown.
- Every Mermaid diagram in HTML must have the same logical source as Markdown.
- Every major claim in HTML should be traceable to the Markdown report evidence.
- If the HTML simplifies detail for readability, preserve the full detail in Markdown.

## Completion Criteria

The task is complete when:

- Markdown and HTML files exist.
- Generated architecture image assets exist.
- Flowchart and sequence Mermaid blocks exist.
- Referenced assets resolve from both Markdown and HTML.
- Validation script passes or any remaining validation limitation is reported.
