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
| TC_UI_PC_030 | Verify duplicate-submit protection on creation | Valid form data entered | 1. Click Submit repeatedly | 

---

## Part Detail View & Tabs

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_DT_001 | Verify part detail page loads successfully | Existing part available | 1. Click on any part | Part detail page loads without errors | High |
| TC_UI_DT_002 | Verify all tabs are visible on part detail page | Existing part with full data | 1. Open part detail page 2. Observe available tabs | All relevant tabs are visible: Stock, BOM, Allocated, Build Orders, Parameters, Variants, Revisions, Attachments, Related Parts, Test Templates | High |
| TC_UI_DT_003 | Verify Stock tab shows correct stock data | Part with stock items | 1. Open part detail 2. Click Stock tab | Stock items for the part are displayed correctly | High |
| TC_UI_DT_004 | Verify BOM tab loads for assembly part | Assembly part with BOM configured | 1. Open assembly part 2. Click BOM tab | BOM items are listed correctly | High |
| TC_UI_DT_005 | Verify BOM tab is empty for non-assembly part | Non-assembly part | 1. Open non-assembly part 2. Click BOM tab | BOM tab shows empty or appropriate message | Medium |
| TC_UI_DT_006 | Verify Allocated tab shows allocations | Part with active allocations | 1. Open part detail 2. Click Allocated tab | Active allocations are displayed correctly | High |
| TC_UI_DT_007 | Verify Build Orders tab shows linked build orders | Part linked to build orders | 1. Open part detail 2. Click Build Orders tab | Linked build orders are listed | High |
| TC_UI_DT_008 | Verify Parameters tab displays configured parameters | Part with parameters set | 1. Open part detail 2. Click Parameters tab | All configured parameters with values are shown | High |
| TC_UI_DT_009 | Verify Parameters tab is empty when no parameters set | Part with no parameters | 1. Open part detail 2. Click Parameters tab | Empty state is shown appropriately | Medium |
| TC_UI_DT_010 | Verify Variants tab shows variants for template part | Template part with variants | 1. Open template part 2. Click Variants tab | All variants are listed | High |
| TC_UI_DT_011 | Verify Variants tab hidden/empty for non-template part | Non-template part | 1. Open non-template part 2. Click Variants tab | No variants listed or tab not shown | Medium |
| TC_UI_DT_012 | Verify Revisions tab shows revisions | Part with revisions | 1. Open part detail 2. Click Revisions tab | All revisions are listed with correct revision codes | High |
| TC_UI_DT_013 | Verify Attachments tab allows viewing attachments | Part with attachments | 1. Open part detail 2. Click Attachments tab | Attachments are listed with names and types | High |
| TC_UI_DT_014 | Verify Related Parts tab shows related parts | Part with related parts configured | 1. Open part detail 2. Click Related Parts tab | Related parts are displayed | Medium |
| TC_UI_DT_015 | Verify Test Templates tab shows templates for testable part | Testable part with test templates | 1. Open testable part 2. Click Test Templates tab | Test templates are listed | High |
| TC_UI_DT_016 | Verify Show/Hide Part Details panel toggle | Any part detail page | 1. Open part detail 2. Toggle part details panel | Panel expands and collapses correctly | Medium |
| TC_UI_DT_017 | Verify part image is displayed if uploaded | Part with image | 1. Open part detail page | Part thumbnail/image is shown in header area | Medium |
| TC_UI_DT_018 | Verify part detail page shows correct part name and IPN | Known part | 1. Open part detail page | Part name and IPN match expected values | High |
| TC_UI_DT_019 | Verify navigation between tabs does not reload page | Any part detail | 1. Click through multiple tabs quickly | Tab switching is smooth with no full page reload | Low |
| TC_UI_DT_020 | Verify inactive part shows inactive status indicator | Inactive part | 1. Open inactive part detail page | Inactive status is visually indicated | Medium |

---

## Part Categories

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_CAT_001 | Verify part categories are listed in parts module | Categories exist | 1. Open Parts module | Category list/tree is visible | High |
| TC_UI_CAT_002 | Verify subcategories are shown under parent category | Nested categories exist | 1. Open parent category | Subcategories are listed correctly | High |
| TC_UI_CAT_003 | Verify all parts under category including subcategories are listed | Multi-level categories with parts | 1. Open parent category 2. View parts list | Parts from sub-categories are also listed | High |
| TC_UI_CAT_004 | Verify category detail shows category parameters | Category with parameters configured | 1. Open category 2. View Part Parameters tab | Category-level parameters are shown | Medium |
| TC_UI_CAT_005 | Verify parametric table filters parts by parameter values | Category with parametric data | 1. Open category 2. View parametric table 3. Apply filter | Parts filtered correctly by parameter values | Medium |
| TC_UI_CAT_006 | Verify category breadcrumb navigation works | Nested category open | 1. View breadcrumb at top of category | Breadcrumb shows correct hierarchy and links work | Medium |
| TC_UI_CAT_007 | Verify search within category filters results | Category with multiple parts | 1. Open category 2. Use search box | Only matching parts are shown | High |
| TC_UI_CAT_008 | Verify empty category shows appropriate message | Empty category | 1. Open category with no parts | Empty state is shown clearly | Low |

---

## Part Attributes

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_ATTR_001 | Verify Virtual attribute is displayed correctly | Part marked as Virtual | 1. Open part detail | Virtual flag is shown in attributes | High |
| TC_UI_ATTR_002 | Verify Template attribute is displayed correctly | Part marked as Template | 1. Open part detail | Template flag is shown in attributes | High |
| TC_UI_ATTR_003 | Verify Assembly attribute is displayed correctly | Part marked as Assembly | 1. Open part detail | Assembly flag is shown; BOM tab is active | High |
| TC_UI_ATTR_004 | Verify Component attribute is displayed correctly | Part marked as Component | 1. Open part detail | Component flag is shown | High |
| TC_UI_ATTR_005 | Verify Trackable attribute enables serial number tracking | Part marked as Trackable | 1. Open part 2. Add stock with serial number | Serial number field is available for stock entry | High |
| TC_UI_ATTR_006 | Verify Purchaseable attribute shows supplier options | Part marked as Purchaseable | 1. Open part detail | Suppliers tab/section is visible | High |
| TC_UI_ATTR_007 | Verify Salable attribute is reflected correctly | Part marked as Salable | 1. Open part detail | Salable flag is shown in attributes | Medium |
| TC_UI_ATTR_008 | Verify Active/Inactive toggle changes part status | Any part | 1. Toggle Active status 2. Save | Part status changes and is visually reflected | High |
| TC_UI_ATTR_009 | Verify inactive part cannot be used in new transactions | Inactive part | 1. Attempt to use inactive part in new BOM or order | System prevents or warns about using inactive part | High |
| TC_UI_ATTR_010 | Verify Testable attribute enables test templates tab | Part marked as Testable | 1. Open testable part | Test Templates tab is visible and accessible | High |

---

## Units of Measure

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_UOM_001 | Verify default unit pcs is available for new part | InvenTree default config | 1. Open New Part form 2. Check units field | pcs is available as default unit option | High |
| TC_UI_UOM_002 | Verify custom physical units are available in unit selector | Custom units configured in settings | 1. Open New Part form 2. Open units dropdown | Custom configured units are listed | High |
| TC_UI_UOM_003 | Verify unit is displayed on part detail page | Part with unit assigned | 1. Open part detail | Correct unit is shown on part detail | Medium |
| TC_UI_UOM_004 | Verify unit is shown in stock and BOM views | Part with unit used in stock/BOM | 1. View stock and BOM tabs | Unit is consistently shown across tabs | Medium |
| TC_UI_UOM_005 | Verify supplier part units can differ from part units | Purchaseable part with supplier | 1. Open supplier part 2. Check units | Supplier part can have its own unit (pack size) | Medium |

---

## Part Revisions

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_REV_001 | Verify revision can be created from existing part | Existing part; revision feature enabled | 1. Open part 2. Create new revision 3. Set Revision Of field 4. Enter revision code 5. Submit | Revision is created and linked to original part | High |
| TC_UI_REV_002 | Verify revision code is required | Revision creation form open | 1. Leave revision code blank 2. Submit | Validation error shown for missing revision code | High |
| TC_UI_REV_003 | Verify duplicate revision code is rejected | Part with existing revision | 1. Create revision with same code as existing 2. Submit | Error shown; duplicate revision code rejected | High |
| TC_UI_REV_004 | Verify revision-of-revision is prevented | Existing revision part | 1. Try to create a revision of a revision | System blocks or warns against revision chaining | High |
| TC_UI_REV_005 | Verify revisions are listed in Revisions tab | Part with multiple revisions | 1. Open original part 2. Click Revisions tab | All revisions listed with their revision codes | High |
| TC_UI_REV_006 | Verify navigating to a revision shows its own detail | Part with revision | 1. Click on a revision from Revisions tab | Revision part detail page opens correctly | Medium |
| TC_UI_REV_007 | Verify Revision Of field links back to original part | Revision part open | 1. View revision detail page | Revision Of field shows link to original part | Medium |
| TC_UI_REV_008 | Verify revision parts inherit template attributes where applicable | Template part with revision | 1. Open revision of a template part | Variant/template relationship is maintained | Medium |

---

## Negative and Boundary Cases

| TC ID | Title | Preconditions | Steps | Expected Result | Priority |
|---|---|---|---|---|---|
| TC_UI_NEG_001 | Verify part name with maximum character length | Part creation form | 1. Enter max allowed characters in name field 2. Submit | Part is created successfully at boundary | High |
| TC_UI_NEG_002 | Verify part name exceeding max character limit is rejected | Part creation form | 1. Enter characters exceeding max limit 2. Submit | Validation error shown; part not created | High |
| TC_UI_NEG_003 | Verify XSS input in part name is sanitized | Part creation form | 1. Enter script tag in name field 2. Submit | Input is sanitized; no script executes | High |
| TC_UI_NEG_004 | Verify special characters in part name are handled | Part creation form | 1. Enter special characters in name 2. Submit | Part is created or clear error shown | Medium |
| TC_UI_NEG_005 | Verify duplicate part name handling when uniqueness enforced | Existing part | 1. Create part with same name 2. Submit | Error shown if uniqueness is enforced | High |
| TC_UI_NEG_006 | Verify duplicate IPN is rejected when uniqueness enforced | Existing part with IPN | 1. Create part with same IPN 2. Submit | System rejects duplicate IPN and shows error | High |
| TC_UI_NEG_007 | Verify accessing part detail with invalid ID shows error | No valid part for ID | 1. Navigate to /part/99999/ (non-existent) | 404 or appropriate error page shown | Medium |
| TC_UI_NEG_008 | Verify user without view permission cannot see part detail | User without view permission | 1. Navigate to part detail URL directly | Access denied or redirect to login | High |
| TC_UI_NEG_009 | Verify inactive part is excluded from active parts list | Inactive part exists | 1. View active parts list/filter | Inactive part does not appear in active list | High |
| TC_UI_NEG_010 | Verify part with zero stock shows correct zero value | Part with no stock | 1. Open part detail 2. View stock tab | Stock count shows 0, not blank or error | Medium |
| TC_UI_NEG_011 | Verify part cannot be deleted if linked to active stock | Part with active stock | 1. Attempt to delete part | System blocks deletion and shows reason | High |
| TC_UI_NEG_012 | Verify part cannot be deleted if linked to active BOM | Part used in BOM | 1. Attempt to delete part | System blocks deletion and shows reason | High |
| TC_UI_NEG_013 | Verify revision code with only spaces is rejected | Revision creation form | 1. Enter only spaces as revision code 2. Submit | Validation error shown | Medium |
| TC_UI_NEG_014 | Verify concurrent edit conflict handling | Two sessions editing same part | 1. Edit same part in two browser tabs 2. Save both | Second save shows conflict warning or overwrites gracefully | Low |
| TC_UI_NEG_015 | Verify empty search returns all parts in category | Category with parts | 1. Open category 2. Submit empty search | All parts in category are returned | Medium |Only one part is created | Medium |
