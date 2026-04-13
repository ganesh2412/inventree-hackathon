# UI Manual Test Cases – InvenTree Parts Module

## Scope
Parts module of InvenTree web application.

## References
- https://docs.inventree.org/en/stable/part/
- https://docs.inventree.org/en/stable/part/views/
- https://docs.inventree.org/en/latest/part/create/
- https://docs.inventree.org/en/stable/part/template/
- https://docs.inventree.org/en/stable/part/revision/

## Preconditions
- InvenTree application is up and accessible
- Test user can log in
- Required permissions are available unless otherwise stated
- Part categories exist
- Supporting master data exists where needed

---

## Part Creation

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_PC_001 | Verify New Part button is visible for authorized user | User has Part create permission; at least one category exists | 1. Login 2. Open Parts module 3. Open a category | New Part button is visible in category context actions | High |
| TC_UI_PC_002 | Verify New Part button is hidden for unauthorized user | User does not have Part create permission | 1. Login 2. Open Parts module 3. Open a category | New Part button is not shown | High |
| TC_UI_PC_003 | Open part creation form from category page | User has Part create permission | 1. Open a category 2. Click New Part | Part creation form opens successfully | High |
| TC_UI_PC_004 | Create part with valid mandatory data | User has Part create permission | 1. Open New Part form 2. Enter valid required fields 3. Submit | Part is created successfully and user is redirected to part detail page | High |
| TC_UI_PC_005 | Validate required field errors on empty submit | User has Part create permission | 1. Open New Part form 2. Leave required inputs blank 3. Click Submit | Inline validation errors are displayed and form is not submitted | High |
| TC_UI_PC_006 | Verify invalid field values block submission | User has Part create permission | 1. Open New Part form 2. Enter invalid values 3. Submit | Validation errors are shown and part is not created | High |
| TC_UI_PC_007 | Verify form retains values after validation error | User has Part create permission | 1. Open New Part form 2. Fill form partially 3. Trigger validation error | Previously entered valid values remain populated | Medium |
| TC_UI_PC_008 | Verify successful redirect after part creation | User has Part create permission | 1. Create a valid part 2. Submit form | Browser redirects to new part detail page | High |
| TC_UI_PC_009 | Verify created part appears under selected category | User has created a new part | 1. Return to category view 2. Search/browse created part | New part is listed under the selected category | High |
| TC_UI_PC_010 | Verify default units of measure for new part | User has Part create permission | 1. Open New Part form 2. Observe units field default | Default unit is populated as pcs unless changed | Medium |
| TC_UI_PC_011 | Verify optional fields accept valid input | User has Part create permission | 1. Open New Part form 2. Enter description, keywords, external link, revision 3. Submit | Part is created and optional values are saved | Medium |
| TC_UI_PC_012 | Verify external link field saves valid URL | User has Part create permission | 1. Enter valid URL in external link 2. Submit | Part is created and external link is stored correctly | Medium |
| TC_UI_PC_013 | Verify invalid external link handling | User has Part create permission | 1. Enter invalid URL format 2. Submit | Form shows validation error | Medium |
| TC_UI_PC_014 | Verify create initial stock section visibility when enabled | System setting Create Initial Stock is enabled | 1. Open New Part form | Extra section for initial stock is visible | High |
| TC_UI_PC_015 | Verify create initial stock section hidden when disabled | System setting Create Initial Stock is disabled | 1. Open New Part form | Initial stock section is not shown | Medium |
| TC_UI_PC_016 | Create part with initial stock enabled and valid values | Create Initial Stock setting enabled | 1. Open New Part form 2. Enter part data 3. Enable Create Initial Stock 4. Enter valid stock values 5. Submit | Part is created and initial stock record is created | High |
| TC_UI_PC_017 | Verify validation in initial stock subsection | Create Initial Stock setting enabled | 1. Enable Create Initial Stock 2. Enter invalid stock values 3. Submit | Validation errors shown and submission blocked | High |
| TC_UI_PC_018 | Verify supplier options shown for purchaseable part | User has Part create permission | 1. Open New Part form 2. Mark part as Purchaseable | Supplier/manufacturer options become available | High |
| TC_UI_PC_019 | Verify supplier options not shown for non-purchaseable part | User has Part create permission | 1. Open New Part form 2. Ensure part is not Purchaseable | Supplier/manufacturer options are not shown | Medium |
| TC_UI_PC_020 | Create purchaseable part with supplier data | Supplier data available | 1. Mark Purchaseable 2. Enable Add Supplier Data 3. Enter valid supplier info 4. Submit | Part created with linked supplier data | High |
| TC_UI_PC_021 | Validate supplier subsection required fields | Purchaseable part; Add Supplier Data enabled | 1. Enable Add Supplier Data 2. Leave required fields blank 3. Submit | Validation errors shown and submission blocked | High |
| TC_UI_PC_022 | Verify unique name/IPN rules during part creation | Existing part data available | 1. Create part with duplicate unique identifiers 2. Submit | System prevents duplicate and shows clear error | High |
| TC_UI_PC_023 | Verify part can be created with revision value | User has Part create permission | 1. Create part with revision field populated 2. Submit | Part created and revision value shown on detail page | Medium |
| TC_UI_PC_024 | Verify keywords improve findability after creation | Searchable UI available | 1. Create part with distinctive keywords 2. Search using keyword | Created part can be found using saved keywords | Medium |
| TC_UI_PC_025 | Verify cancel behavior on part creation form | User has opened creation form | 1. Enter some values 2. Cancel form | Form closes safely; no part is created | Medium |
| TC_UI_PC_026 | Verify browser back behavior during creation | User is on part creation form | 1. Enter data 2. Navigate back | No unintended duplicate part is created | Low |
| TC_UI_PC_027 | Verify import entry point is available | Import feature available | 1. Navigate to category actions 2. Look for import option | Import action is available | Medium |
| TC_UI_PC_028 | Verify part import with valid file | Import feature available; valid file prepared | 1. Start import 2. Upload valid data 3. Submit | Parts are imported and visible in UI | Medium |
| TC_UI_PC_029 | Verify part import validation for invalid file | Import feature available | 1. Start import 2. Upload invalid data | User receives import errors; invalid records not created | Medium |
| TC_UI_PC_030 | Verify duplicate-submit protection on creation | Valid form data entered | 1. Click Submit repeatedly | Only one part is created | Medium |
