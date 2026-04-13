# UI Automation

This folder contains UI automation scripts for the InvenTree Parts module.

## Framework
- Tool: Playwright (JavaScript/TypeScript)
- Coverage: Core Part CRUD flows, tab navigation, form validation

## Setup
```bash
npm install
npx playwright install
```

## Run Tests
```bash
npx playwright test
```

## Test Files
- `tests/part-creation.spec.ts` - Part creation UI flows
- `tests/part-detail.spec.ts` - Part detail tabs and views
- `tests/part-categories.spec.ts` - Category navigation

> Automation scripts will be added in the next phase of the hackathon.
