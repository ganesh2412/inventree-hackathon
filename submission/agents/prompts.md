# Agent Prompts & Configuration

## Overview
This document captures all AI agent prompts, system instructions, and configurations used during this hackathon to generate test cases and automation scripts for the InvenTree Parts module.

## Tool Used
- AI Assistant: Comet (Perplexity)
- Purpose: Generate UI manual test cases, API test cases, and automation scripts from InvenTree documentation

---

## Prompt 1 – UI Manual Test Cases: Part Creation

**Objective:** Generate comprehensive UI manual test cases for the InvenTree Parts module – Part Creation flow.

**Prompt:**
```
Generate comprehensive UI manual test cases for the InvenTree Parts Module.
Focus on Part Creation including:
- New Part button visibility based on permissions
- Part creation form validation (required fields, invalid data)
- Successful part creation and redirect
- Optional fields (description, keywords, external link, revision)
- Initial stock section (when enabled/disabled via settings)
- Supplier data section (for purchaseable parts)
- Import flow
- Negative and boundary scenarios
Format output as a markdown table with columns: TC ID, Title, Preconditions, Steps, Expected Result, Priority.
Base test cases on InvenTree documentation: https://docs.inventree.org/en/latest/part/create/
```

---

## Prompt 2 – UI Manual Test Cases: Part Detail Tabs

**Objective:** Generate test cases for all tabs on the InvenTree Part Detail page.

**Prompt:**
```
Generate UI manual test cases for the InvenTree Part Detail View page.
Cover all tabs:
- Stock, BOM, Allocated, Build Orders, Parameters, Variants, Revisions, Attachments, Related Parts, Test Templates
Also cover:
- Show/Hide part details panel toggle
- Part image display
- Tab navigation behavior
- Inactive part indicator
Format as markdown table: TC ID, Title, Preconditions, Steps, Expected Result, Priority.
Reference: https://docs.inventree.org/en/stable/part/views/
```

---

## Prompt 3 – UI Manual Test Cases: Categories, Attributes, UoM, Revisions, Negative Cases

**Objective:** Generate remaining UI test cases for Part Categories, Part Attributes, Units of Measure, Revisions, and Negative/Boundary scenarios.

**Prompt:**
```
Generate UI manual test cases for InvenTree Parts module covering:
1. Part Categories - hierarchy, subcategories, parametric filtering, breadcrumbs, search
2. Part Attributes - Virtual, Template, Assembly, Component, Trackable, Purchaseable, Salable, Active/Inactive, Testable
3. Units of Measure - default unit, custom units, unit display in stock/BOM, supplier units
4. Part Revisions - create revision, revision code validation, duplicate code rejection, revision-of-revision prevention
5. Negative and Boundary Cases - max length, XSS, duplicate IPN, invalid ID, permission checks, deletion blocked by relations
Format as markdown table: TC ID, Title, Preconditions, Steps, Expected Result, Priority.
```

---

## Prompt 4 – API Manual Test Cases

**Objective:** Generate manual API test cases for the InvenTree Parts API.

**Prompt:**
```
Generate comprehensive API manual test cases for InvenTree Parts API.
Cover the following endpoints:
- GET /api/part/ - list parts with filtering, pagination, search
- POST /api/part/ - create part with valid and invalid data
- GET /api/part/{id}/ - retrieve specific part
- PATCH /api/part/{id}/ - update part fields
- DELETE /api/part/{id}/ - delete part
- GET /api/part/category/ - list categories
- POST /api/part/category/ - create category
For each: include positive, negative, boundary, and authorization test cases.
Format as markdown table: TC ID, Endpoint, Method, Description, Request Data, Expected Status, Expected Response.
```

---

## System Instructions

- Always reference official InvenTree documentation as source of truth
- Generate test cases in markdown table format for GitHub rendering
- Use consistent TC ID naming convention: TC_UI_[SECTION]_[NNN] for UI, TC_API_[NNN] for API
- Cover High, Medium, and Low priority test cases
- Include both positive and negative scenarios for every feature area
- Base automation scripts on the manual test cases generated
