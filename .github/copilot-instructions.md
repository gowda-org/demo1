# Copilot instructions

## Repository overview

This is a small Node.js demonstration repository. There is currently no application source tree or build step; the repository is primarily package metadata, GitHub Actions workflows, and pull-request process configuration.

The Node tooling is defined in `package.json`:

- `npm run lint` runs ESLint against the repository (`eslint .`).
- `npm test` runs Jest (`jest`).
- There is no `build` script.

CI uses Node.js 18, installs dependencies with `npm install`, then runs lint and tests. Keep local validation aligned with that order:

```text
npm install
npm run lint
npm test
```

To run one Jest test file:

```text
npx jest path/to/example.test.js
```

To run one test by name:

```text
npx jest -t "test name"
```

## Architecture and automation

GitHub Actions is the main integration surface:

- `.github/workflows/env_test.yml` is manually dispatched and demonstrates a two-job plan/implement dependency using a job output.
- `.github/workflows/plan-gate.yml` runs for pull requests targeting `main` and verifies that `.github/pull_request_template.md` exists.
- `.github/workflows/success-criteria.yml` runs Jest for pull requests to `main` and also runs a CodeQL initialization/analysis job.
- `.github/workflows/azure-webapps-node.yml` is an issue-close workflow; it is not the application deployment workflow despite its filename.
- `.github/workflows/daily-activity-report.md` contains workflow-related documentation/content, while the matching `.lock.yml` file is marked generated in `.gitattributes`.

When changing CI behavior, check all workflows triggered by pull requests to `main`, because validation is split across separate workflows rather than a single pipeline. Preserve explicit workflow triggers and job dependencies, and avoid treating manually dispatched workflows as ordinary PR validation.

## Repository-specific conventions

- Pull requests use `.github/pull_request_template.md`; retain its checklist expectations around contributing guidance, duplicate PRs, tests, linting, and explanations for core-feature changes.
- Workflow files use GitHub-hosted `ubuntu-latest` runners and pinned major versions for actions (for example, checkout `@v4` and setup-node `@v4`).
- The PR validation workflow uploads `results/` as a test-results artifact even when preceding steps fail and posts a status comment; changes to test reporting should preserve those failure-path behaviors.
- Do not hand-edit files matched by `.github/workflows/*.lock.yml linguist-generated=true` unless the task explicitly targets generated workflow output.
- Keep project-specific metadata in `package.json`; use the existing ESLint and Jest scripts rather than introducing alternate commands.
