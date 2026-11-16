# Repository Continuity project brief

> **Continuity role:** durable intent
> **Status:** current
> **Last verified:** 2026-07-15
> **Owns:** purpose, users, scope, non-goals, constraints, and success
> **Update when:** project direction changes, not when implementation merely advances

## Purpose

Repository Continuity gives AI coding agents a reusable protocol for preserving
a software project's usable state across sessions, collaborators, and periods
of dormancy. It connects durable documentation with explicit authorization,
repeatable transition workflows, and appropriately scoped executable checks.

## Intended users and consumers

- Individual developers using Codex across multiple repositories.
- Maintainers returning to dormant or unfamiliar projects.
- Teams adapting the generic protocol to their own local documentation control
  plane.

## Goals

- Make a repository resumable without conversational memory.
- Prevent discussion or planning from silently becoming implementation.
- Reconcile code, state, integrations, contracts, and operations when facts change.
- Detect cheap structured drift mechanically without pretending prose is fully testable.
- Allow lessons from failures to improve shared workflows without overwriting local truth.

## Non-goals

- Generate exhaustive documentation from source code.
- Define one universal software architecture or document filename layout.
- Replace project-owned semantic, privacy, integration, or conformance tests.
- Automatically rewrite local documents when shared templates evolve.
- Publish any user's private project registry, audit history, or local policy.

## Repository boundary

This repository owns the generic `manage-project-docs` Codex skill, its
workflow references, reusable output templates, deterministic structural
checks, and sanitized validation fixtures. User-specific control planes and
project documents consume or adapt these assets but remain separately owned.

## Current phase

The initial phase must prove that one compact skill can route six continuity
operations, carry templates without loading them into routine context, and run
a dependency-free structural checker against both healthy and drifted fixtures.

## Success

- A cold Codex session can select the correct workflow without private context.
- Resume and audit remain read-only unless the user separately authorizes edits.
- Templates give every kind of truth one clear owner.
- The checker reports known fixture drift and accepts a healthy fixture.
- Skill structure passes the official validator.

## Constraints

- Keep runtime skill context concise through progressive disclosure.
- Use no runtime dependencies beyond the Python standard library in the first release.
- Preserve human approval for consequential project transitions.
- Keep public artifacts generic and free of personal or repository-specific data.
