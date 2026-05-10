---
name: source-architecture-docs
description: Generate architecture documentation from project source code and user-provided Markdown project files. Use when Codex needs to inspect a codebase, README/spec/design docs, ROS 2 packages, Android/Kotlin/JNI modules, CMake/Gradle/build files, launch/config files, APIs, message definitions, or similar project artifacts, then produce an AI-readable Markdown architecture report and a human-facing HTML artifact with Image Gen architecture diagrams, Mermaid flowcharts, and Mermaid sequence diagrams.
---

# Source Architecture Docs

## Overview

Use this skill to turn source code plus project Markdown into two synchronized deliverables:

- `architecture-report.md`: evidence-based Markdown for AI agents and future maintainers.
- `architecture-artifact.html`: presentation-quality HTML for humans, with generated architecture imagery and rendered Mermaid diagrams.

Generate architecture overview and local relationship diagrams with Image Gen. Generate core flowcharts and sequence diagrams as Mermaid text so they remain editable, reviewable, and renderable in both Markdown and HTML.

## Workflow

1. Clarify inputs and scope only when missing.
   - Required: source directory or file list, project Markdown docs, and output directory.
   - Ask before excluding large important areas such as `src/`, `app/`, `packages/`, `launch/`, `config/`, `msg/`, `srv/`, `proto/`, or build/deployment files.
   - If the project is ROS 2, Android, JNI/NDK, or multi-board robotics, preserve runtime boundaries such as board, process, node, topic, service, action, transport, and hardware interface.

2. Build an evidence map before drawing.
   - Read project docs first for intended architecture and vocabulary.
   - Inspect source structure with `rg --files`, then read entry points, build manifests, launch/config files, public interfaces, message schemas, and core modules.
   - Record evidence as file paths and short facts. Do not claim relationships that are not supported by code, docs, config, or explicit inference.
   - Separate confirmed facts from inferred behavior.

3. Identify diagram set.
   - Produce one whole-system architecture diagram.
   - Produce local architecture diagrams for subsystems with meaningful internal relationships.
   - Produce core flowcharts for the main business or runtime workflows.
   - Produce sequence diagrams for important cross-component interactions, especially async calls, IPC, ROS 2 communication, network calls, JNI calls, callbacks, and hardware loops.

4. Generate architecture images with Image Gen.
   - Use the prompt contract in `references/diagram-standards.md`.
   - Prefer clean software architecture diagrams over decorative illustrations.
   - Include module boundaries, direction of data/control flow, deployment/runtime grouping, and key protocols.
   - Save generated images under `assets/` and reference them from both Markdown and HTML.

5. Write Mermaid diagrams for flows and sequences.
   - Use `flowchart LR` or `flowchart TD` for core flows.
   - Use `sequenceDiagram` for interaction timing.
   - Keep labels short and domain-specific.
   - Include failure, timeout, retry, fallback, or cancellation paths when the source shows them.

6. Produce final artifacts.
   - Follow `references/output-contract.md` for required sections and file naming.
   - Use `assets/artifact-template.html` as the HTML starting point when no project-specific template exists.
   - Embed Mermaid source in the HTML artifact and load Mermaid from CDN unless the user requires offline-only output.
   - Keep Markdown and HTML logically synchronized: the HTML is the presentation version of the Markdown, not a different analysis.

7. Validate before finishing.
   - Run `scripts/validate_artifacts.py <architecture-report.md> <architecture-artifact.html>` when both files exist.
   - Check that image files referenced by Markdown/HTML exist.
   - Check that Mermaid diagrams are present and that no placeholder tokens remain.
   - If browser tooling is available, open the HTML and inspect at least desktop layout. For visual-heavy outputs, screenshot the artifact and fix obvious overlap or unreadable text.

## Reference Files

- `references/source-analysis.md`: source-reading checklist and evidence model.
- `references/diagram-standards.md`: Image Gen prompt contract plus architecture, flowchart, and sequence diagram standards.
- `references/output-contract.md`: exact Markdown/HTML deliverable structure.

Read only the reference files needed for the current task. For most full architecture-documentation requests, read all three.

## Output Rules

- Prefer exact component names from code and docs over invented names.
- Use file references in the Markdown report for important claims.
- Mark inferred relationships with "Inferred" or "Likely" and explain the evidence.
- Do not use Image Gen for flowcharts or sequence diagrams unless the user explicitly asks; use Mermaid for those.
- Do not create a marketing landing page. The HTML artifact should be a direct architecture presentation with navigation, diagrams, and concise explanatory text.
- Do not omit uncertainty. Include an "Open Questions / Verification Gaps" section when source evidence is incomplete.
