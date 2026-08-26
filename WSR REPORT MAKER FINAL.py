Complete Detailed Prompt — SAP BW Monitoring Tracker GUI Changes
Modify the existing SAP BW Monitoring Tracker automation script GUI to implement the following changes. This specification covers all field changes, new fields, renames, validations, visual indicators, button behaviors, section merges, dropdown logic, and reporting changes. Manager's requirements take priority in all cases. Additional items from the transcript discussion are included where they add value without conflicting with the manager's direction.

1. Mandatory Field Label Formatting
All mandatory/required field labels must be displayed in RED text throughout the entire GUI.

This is a universal rule — any field marked as mandatory must have its label rendered in RED to provide a clear visual indicator to operators.

The following fields must have RED labels:
Chain Status
Error Steps
Infopackage Technical Name
Failure Reason
Recovery Process
Fix Applied
Owner
Alert Email Received
ABA for TBA (from transcript — confirm with manager if needed)

When new mandatory fields are added in the future, they must also automatically receive RED labels.

RED should be a clearly visible shade (e.g., #CC0000 or #E11D48) that contrasts against the form background.

2. Read-Only / Greyed Out Fields
The following fields must be converted to read-only with a greyed-out background. Users must not be able to click into, type in, or modify these fields in any way. The values must be populated automatically by the system.

2.1 Completion Date and Time
Current state: Editable field

Required change: Make completely read-only and greyed out

Auto-update rule: Value must be populated only upon job completion — when the process chain finishes successfully

Failed job rule: If the job status is "Failed", this field must remain empty/blank — a failed job cannot have a completion timestamp. Do not show any value, placeholder, or default date

Visual: Grey background (#E0E0E0 or similar), no cursor, non-clickable

2.2 Failure Date and Time
(from transcript)

Current state: May be editable

Required change: Make read-only and greyed out

Auto-populate rule: Value must be auto-populated from the SAP BW system when a failure is detected — not entered manually

Visual: Same grey background as other read-only fields

2.3 Shift
Current state: Editable field

Required change: Make read-only, greyed out, and auto-calculated

Calculation rule: Shift must be automatically determined based on the failure time:
Define shift boundaries (e.g., Morning: 06:00–14:00, Afternoon: 14:00–22:00, Night: 22:00–06:00 — adjust to your organization's shift schedule)
When a failure occurs, the system reads the failure timestamp and auto-assigns the correct shift

Visual: Grey background, non-editable

2.4 Process Chain Runtime (Renamed from "Run time")
Current state: Field labeled "Run time", may be editable

Required changes:
Rename the field label from "Run time" to "Process Chain Runtime"
Make the field read-only and greyed out
Auto-calculate using the formula: Runtime = End Time − Start Time
Show only for completed PCs — if the process chain has not completed, this field must remain empty/blank
Do NOT calculate runtime for failed or still-running process chains

2.5 PC Running for Last
(New Field)

Current state: Field does not exist — must be created

Purpose: Show how long a process chain has been running when it has not yet completed (still in progress)

Required behavior:
Add a new field labeled "PC Running for Last"
Field must be read-only, greyed out, and auto-calculated
Calculation: Current Time − Start Time — showing elapsed running duration
Applicable only for PCs that are not yet completed (still running)
Once the PC completes, this field should clear/hide and the "Process Chain Runtime" field should populate instead
The value should update automatically at regular intervals (e.g., every minute or on refresh)

Placement: Near the runtime fields, adjacent to Process Chain Runtime

2.6 Query Run Time
(New Field)

Current state: Field does not exist — must be created

Purpose: Display the query execution time (added by Dhanashree to the query)

Required behavior:
Add a new field labeled "Query Run Time"
Include this value in the query output / report
Field should be read-only and greyed out

Placement: In the query/report output area

2.7 Global Read-Only Rule
Any field that is automatically updated must NEVER be manually editable by the user

All auto-calculated fields must have:
Grey background color
No text cursor on hover
No click/focus response
No keyboard input accepted

This applies to: Completion Date/Time, Failure Date/Time, Shift, Process Chain Runtime, PC Running for Last, Query Run Time

3. Field Renames
The following field labels and button labels must be renamed throughout the GUI. Update all occurrences — labels, tooltips, headers, error messages, and any references in reports.

#	Current Label	New Label	Type
3.1	Run time	
Process Chain Runtime

Field label
3.2	#of restart	
#of repeat

Field label
3.3	OK	
Save

Button label
3.4	Generate Report Preview	
Preview Hourly Report

Button label
3.5	Copy as Table (Paste into Teams)	
Copy Hourly Report to Clipboard

Button label
3.6	Hourly Report / Monitoring Log
(section header)

Monitoring Log Updates

Section header
Ensure all renames are consistent across the entire application — no instances of the old names should remain anywhere.

4. New Fields to Add
The following fields must be newly created and added to the GUI. They do not currently exist in the application.

4.1 Owner Related Comments
Type: Text area (multi-line free text)

Mandatory: No

Editable: Yes

Placement: Positioned next to or directly below the Owner field in the main window

Purpose: Allows operators to add context or comments related to the assigned owner

4.2 Meta Chain Identifier
Type: Text / ID field

Mandatory: No

Editable: Yes

Placement: Near chain identification fields (e.g., near Process Chain name, Technical Name)

Purpose: Provides a unique identifier for each Meta Chain

4.3 Previous Status
Type: Dropdown

Mandatory: No (but recommended to fill)

Editable: Yes

Dropdown values: Failed, Fixed, Regarding, Completed

Placement: Near status tracking fields, paired with Current Status

Purpose: Records what the process chain's status was before the latest update

4.4 Current Status
Type: Dropdown

Mandatory: No (but recommended to fill)

Editable: Yes

Dropdown values: Failed, Fixed, Regarding, Completed

Placement: Directly next to or below Previous Status

Purpose: Records what the process chain's status is now

Combined behavior: Previous Status + Current Status together track state transitions:
Example: Previous = "Failed" → Current = "Fixed" means the chain was fixed after a failure
This pair provides a clear audit trail of status changes

Storage: To be discussed with Prashant regarding where and how these values are stored and retrieved

4.5 Average Runtime
(from transcript)

Type: Duration field

Mandatory: No

Editable: No (read-only, greyed out)

Placement: Near runtime fields (Process Chain Runtime, PC Running for Last)

Purpose: Stores the expected/average runtime for each process chain — used as a reference value for comparison

Escalation behavior: If actual runtime (or PC Running for Last) exceeds this threshold, the system should trigger a visual alarm — see Section 9.5

5. Fields to Remove from GUI
5.1 Duplicate BW Recovery Notes
Issue: There are multiple instances of the "BW Recovery Notes" field in the GUI

Action: Keep only ONE BW Recovery Notes field. Remove all duplicate/extra instances

Which to keep: Retain the primary instance in the main form section

5.2 Duplicate ABAP / ABAP Step
Issue: Both "ABAP" and "ABAP Step" fields exist — they capture the same information

Action: Retain only one of the two fields. Remove the other completely

Recommendation: Keep "ABAP Step" as it is more descriptive. Remove the generic "ABAP" field. (Confirm with team which to keep)

5.3 Separate "Green" Section
(from transcript)

Issue: A separate section (visually styled in green) exists that duplicates fields from the main section

Action: Remove the green section entirely. All data entry should happen in the primary section (visually styled in blue)

Post-removal: Ensure no data is lost — any unique fields from the green section should be incorporated into the primary section before removal

6. Dropdown Field Changes
6.1 Failure Reason
Current state: Unknown input method

Required change: Implement dropdown selection WITH free-text typing option
The field must support BOTH:
Selecting a predefined reason from a dropdown list
Typing a custom reason as free text
This is a combo box / editable dropdown behavior — the user can either pick from the list or type their own value
The dropdown list should contain all common/standard failure reasons
Manager's decision: Both dropdown and free-text are allowed (not restricted to dropdown-only)

6.2 SME Field
(from transcript)

Current state: May allow free-text typing

Required change: Convert to selection-only dropdown — no free-text input allowed
Users must pick from a predefined list of SMEs
Keyboard input should be blocked — selection from list only
The dropdown must contain at least 2 valid SME names for testing
Purpose: Prevent junk/inconsistent data entry

6.3 Area Field
(from transcript)

Current state: May be combined with SME or may not exist

Required change: Create a separate standalone dropdown for Area
Area and SME must be two distinct, independent fields — not combined
Area dropdown should contain all valid processing areas

6.4 Area → SME Auto-Population
(from transcript)

Required behavior: When an operator selects an Area from the Area dropdown, the SME dropdown must automatically populate with the SME(s) mapped to that area
Example: Selecting "RB" (Retail Business) → SME dropdown auto-shows "Ludovic"
Example: Selecting "Finance" → SME dropdown shows "Sarah, Mike" (multiple options)
The mapping must be driven by a master mapping sheet that links Processing Area ↔ SME(s)
Support one area mapping to multiple SMEs — in this case, show all valid SMEs in the dropdown and let the operator choose

6.5 Fix Applied — Validation Constraint
(from transcript)

Current state: No constraint on selections

Required change: Add validation logic to block simultaneous selection of "first and last"
When "first" is selected, "last" should be disabled/greyed out (and vice versa)
These two options are mutually exclusive — they cannot both be active at the same time

6.6 Previous Status — New Dropdown
Type: New dropdown field

Values: Failed, Fixed, Regarding, Completed

See Section 4.3 for full specification

6.7 Current Status — New Dropdown
Type: New dropdown field

Values: Failed, Fixed, Regarding, Completed

See Section 4.4 for full specification

6.8 Alert Email Received
(from transcript)

Current state: Unknown input type

Required change: Implement as an explicit Yes/No toggle or dropdown
Only two valid values: "Yes" or "No"
This field is mandatory — the operator must select one

7. Window / Section / Layout Changes
7.1 Merge Reports into One Section
Current state: The GUI has two separate sections:
"Hourly Report" section
"Monitoring Log" section

Required change: Merge both sections into ONE unified section

New section name: "Monitoring Log Updates"

Rules:
Remove all duplicate fields that existed across both sections
Consolidate all unique fields into the single merged section
Operators should only need to fill in data once in one place
The merged section should contain all fields from both former sections without redundancy

7.2 Remove Separate "Green" Section
(from transcript)

Current state: A visually distinct section (green-styled) exists separately

Required change: Remove the green section entirely

Users fill only the primary (blue-styled) section

Any unique fields from the green section must be moved to the primary section before removal

7.3 Auto-Populate Merged Fields
(from transcript)

When sections are merged, any field that would duplicate information already captured in another part of the form must:
Auto-populate with the value from the primary entry point
Be greyed out and read-only to prevent the operator from entering the same data twice

This ensures the no-duplication principle — capture once, display everywhere needed

7.4 Owner Field Repositioning
Current state: Owner field may be in a sub-section or non-primary location

Required change: Move the Owner field to the main window

Exact position (per manager): Below "Other Team" and beside "BW Recovery Notes"

Include the new "Owner Related Comments" field adjacent to the Owner field

Both fields should be clearly visible and accessible in the main form without scrolling or expanding sections

7.5 Add Close/Exit Button on Popups
(from transcript)

Current state: Popup windows may lack a clear way to close them

Required change: Add a clearly visible "X" button (or "Close" button) on ALL popup windows throughout the application

Placement: Top-right corner of each popup (standard UI convention)

Behavior: Clicking "X" or "Close" dismisses the popup without saving. If the user has unsaved changes, optionally show a confirmation dialog

8. Button Changes
8.1 Save Button (was "OK")
Current label: "OK"

New label: "Save"

Behavior on click:
Validate all mandatory fields — if any are empty, show RED borders around empty fields + error message. Do NOT save.
If all mandatory fields are filled, update the Monitoring Log automatically with all entered values
The saved record must appear in the Monitoring Log with all fields pre-populated — no manual re-entry into the log
Show a brief success confirmation (e.g., "Record saved successfully" toast/message)

8.2 Preview Hourly Report (was "Generate Report Preview")
Current label: "Generate Report Preview"

New label: "Preview Hourly Report"

State logic (from transcript):
DISABLED (greyed out, non-clickable) when any mandatory field is still empty
ENABLED (active, clickable) only when ALL mandatory fields have been completed
When disabled, show a tooltip on hover: "Complete all required fields to preview"
When enabled, clicking generates a preview of the hourly report

8.3 Copy Hourly Report to Clipboard (was "Copy as Table")
Current label: "Copy as Table (Paste into Teams)"

New label: "Copy Hourly Report to Clipboard"

Behavior: Copies the current hourly report content to the system clipboard in a table format suitable for pasting into Microsoft Teams or email

8.4 Archive Today
(from transcript)

Current state: May be always enabled

Required change: The "Archive today" button must be enabled ONLY on the 24th hourly run/upload of the day

All other times (runs 1 through 23): The button must be disabled (greyed out, non-clickable)

Logic: Track the current run number for the day. Enable the archive button only when run_number == 24

8.5 Close/X on Popups
(from transcript)

Add a close/exit button ("X" or "Close") to every popup window in the application

See Section 7.5 for full specification

9. Visual / Color Indicators
9.1 Mandatory Field Labels — RED
All mandatory field labels must be rendered in RED text

See Section 1 for the complete list of mandatory fields

RED color should be consistent across the entire application

9.2 Failed/Unresolved Records — YELLOW Highlight
(from transcript)

Current state: Failed records appear in normal/default styling

Required change: Any record (row) representing a failed process chain that has NOT been updated/resolved must be highlighted in YELLOW

Highlight behavior:
YELLOW background applied to the entire row
The highlight remains until the operator updates the record with resolution details
Once the record is properly updated (all required fields filled, status changed to Fixed/Completed), the YELLOW highlight is removed and the row returns to normal styling

Purpose: Operators can instantly see which failures still need attention

9.3 Completed PC Indicator
Current state: No visual distinction for completed process chains

Required change: Create a visual flag/indicator for process chains already marked as completed

Options (choose one):
✅ Green checkmark icon next to the chain name
🟢 Green badge/dot in the status column
Green background tint on the row
"COMPLETED" text badge in a distinct color

Purpose: Operators can quickly identify which PCs have finished successfully

9.4 Read-Only Fields — Grey Background
(from transcript)

All read-only/auto-calculated fields must have a visually distinct grey background

This creates a clear visual separation between:
Editable fields: White/light background, active cursor on click
Read-only fields: Grey background, no cursor, non-clickable

Apply consistently to: Completion Date/Time, Failure Date/Time, Shift, Process Chain Runtime, PC Running for Last, Query Run Time, Average Runtime

9.5 Runtime Alarm — Visual Alert
(from transcript)

Trigger: When a process chain's actual runtime (or "PC Running for Last" value) exceeds the Average Runtime threshold

Visual response: Display a visual alarm on the affected record:
Red highlight on the runtime cell/field
Warning icon (⚠️) next to the runtime value
Optional: Flashing indicator for critical overruns (e.g., 2x average runtime)

Purpose: Proactively catch process chains running far beyond expected duration

Example: A PO chain that normally takes ~2 hours has been running for 20+ hours — the alarm must trigger automatically so operators notice immediately, especially on weekends

10. Input Validation Rules
10.1 Count of Records — Numeric Only
Field: Count of Records

Validation: Accept numeric values only

Behavior:
Reject non-numeric keystrokes in real-time (letters, special characters)
Allow only digits (0-9)
If the user somehow enters non-numeric content, show an error: "This field accepts numbers only"

10.2 #of repeat — Numeric Only
(from transcript)

Field: #of repeat (renamed from #of restart)

Validation: Accept numeric values only

Behavior: Same as Count of Records (10.1)

10.3 Mandatory Field Validation on Save
(from transcript)

Trigger: When the operator clicks "Save"

Validation:
Check all mandatory fields (Chain Status, Error Steps, Infopackage Technical Name, Failure Reason, Recovery Process, Fix Applied, Owner, Alert Email Received)
If any mandatory field is empty:
Apply a RED border around the empty field(s)
Display an error message: "Please fill in all required fields before saving"
Do NOT save the record — keep the form open
If all mandatory fields are filled:
Proceed with save
Update the Monitoring Log
Show success confirmation

10.4 Fix Applied — Mutual Exclusion
(from transcript)

Field: Fix Applied dropdown

Validation: The options "first" and "last" are mutually exclusive — they cannot both be selected

Behavior:
When "first" is selected → "last" becomes disabled/greyed in the dropdown
When "last" is selected → "first" becomes disabled/greyed in the dropdown
When neither is selected → both remain available

10.5 SME Dropdown — No Free Text
(from transcript)

Field: SME

Validation: Input is blocked — the user can only select from the predefined list

Behavior:
Keyboard typing in the SME field is disabled
Only mouse click / selection from dropdown list is allowed
The dropdown auto-populates based on the selected Area (see Section 6.4)

10.6 Preview Button — Conditional Enable
(from transcript)

Button: "Preview Hourly Report"

Validation: The button is disabled by default and only becomes enabled when all mandatory fields have values

Behavior when disabled:
Button appears greyed out / non-clickable
On hover, show a tooltip: "Complete all required fields to preview"

Behavior when enabled:
Button appears in active/primary color (e.g., blue)
Clicking generates the report preview

11. Reporting Changes
11.1 Report Preview Button
Rename "Generate Report Preview" to "Preview Hourly Report"

See Section 8.2 for full behavior specification

11.2 Copy Function Button
Rename "Copy as Table (Paste into Teams)" to "Copy Hourly Report to Clipboard"

See Section 8.3 for full behavior specification

11.3 Previous Report Run History
Requirement: Maintain and display entries from the previous report run

Operators should be able to see what was reported in the last hourly cycle

Implementation details: To be discussed with Prashant

This enables:
Continuity between shifts
Verification that nothing was missed
Correct time range derivation for daily/night reports

11.4 Report Consistency
(from transcript)

Hourly and daily reports must contain identical content — same updates, same wording, no discrepancies

Both reports must be generated from the same standardized source (PB1)

There must be no conflicting wording across report types — if a failure is described one way in the hourly report, the daily report must use the exact same description

12. Business Logic — Status Tracking
12.1 Previous + Current Status Storage
The system must store and manage paired status values for each process chain:
Previous Status: What the status was before the latest update
Current Status: What the status is now

Valid status values: Failed, Fixed, Regarding, Completed

Transition tracking examples:
Previous: Failed → Current: Fixed (failure was resolved)
Previous: Failed → Current: Regarding (under investigation)
Previous: Regarding → Current: Completed (investigation led to completion)

Storage mechanism: To be discussed with Prashant — determine where these values are persisted and how they are retrieved

12.2 No-Assumptions Principle
(from transcript)

The system must log only what is actually known and confirmed

Do NOT infer, assume, or auto-fill status or data that has not been explicitly entered/confirmed by the operator

If information is unknown or pending, leave the field empty rather than guessing

All logged entries must have the correct associated time context — the timestamp of when the update actually occurred

13. Pending Discussion Items
#	Item	Owner	What Needs to Be Decided
1	
Previous Report Run History

Prashant	How to store, retrieve, and display entries from the previous report run
2	
Status Tracking Storage

Prashant	Where and how Previous Status / Current Status values are persisted
3	
Query Run Time Specifications

Dhanashree	Exact source, format, and placement of the new Query Run Time field
4	
Which ABAP field to keep

Team	Keep "ABAP" or "ABAP Step"? Remove the other
5	
Shift time boundaries

Team	Define exact shift start/end times for auto-calculation
6	
Average Runtime values

Team	Where do baseline average runtimes come from? Manual entry or historical calculation?
7	
Runtime alarm threshold

Team	What percentage over average triggers the alarm? (e.g., 150%? 200%?)
14. Complete Change Summary
Change Type	Count	Details
Fields to make
read-only / greyed out

7	Completion Date/Time, Failure Date/Time, Shift, Process Chain Runtime, PC Running for Last, Query Run Time, Average Runtime
Fields to
rename

6	Run time, #of restart, OK button, Generate Report Preview, Copy as Table, Section header
Fields to
add

(new)	8	PC Running for Last, Query Run Time, Owner Related Comments, Meta Chain Identifier, Previous Status, Current Status, Average Runtime, Owner Related Comments
Fields to
remove

3	Duplicate BW Recovery Notes, ABAP/ABAP Step duplicate, Green section
Dropdown

changes	8	Failure Reason combo, SME selection-only, Area standalone, Area→SME auto-populate, Fix Applied constraint, Previous Status, Current Status, Alert Email Yes/No
Window/section

changes	5	Merge reports, remove green section, auto-populate merged fields, add popup close buttons, reposition Owner
Button

changes	5	Save rename, Preview rename + conditional enable, Copy rename, Archive today 24th-run logic, Popup close buttons
Visual indicators

5	RED mandatory labels, YELLOW failed highlights, Completed PC flag, Grey read-only backgrounds, Runtime alarm
Input validation

rules	6	Numeric-only counts, mandatory validation on Save, Fix Applied mutual exclusion, SME no-free-text, Preview conditional enable, Tooltip on disabled preview
TOTAL GUI CHANGES

53

15. Implementation Priority
Priority	Changes	Reason
🔴
P1 — Critical

Merge sections into Monitoring Log Updates, remove duplicate fields, rename all buttons, mandatory RED labels, Save button behavior with validation	Core structural changes — everything else depends on these being done first
🔴
P1 — Critical

Add Previous/Current Status dropdowns, status tracking logic	Essential for monitoring log state tracking — core business requirement
🔴
P1 — Critical

Read-only fields (Completion Date/Time, Shift, Process Chain Runtime) with auto-calculation	Data integrity — prevents manual errors in calculated fields
🟠
P2 — High

New fields (PC Running for Last, Query Run Time, Meta Chain ID, Owner Related Comments)	Feature additions that provide new monitoring capabilities
🟠
P2 — High

SME dropdown (selection-only), Area→SME auto-populate, Failure Reason combo box	Data quality enforcement — prevents junk data
🟠
P2 — High

YELLOW highlight for failed records, Completed PC indicator, runtime alarm	Visual enhancements that improve operator situational awareness
🟠
P2 — High

Input validation (numeric-only, mandatory field validation on Save, RED borders)	Data quality and error prevention at point of entry
🟡
P3 — Medium

Owner field repositioning + Owner Related Comments	Layout improvement — functional but not blocking
🟡
P3 — Medium

Previous Report Run History, report consistency rules	Reporting improvements — discuss with Prashant first
🟢
P4 — Low

Archive today button logic (24th run only), close/exit buttons on popups	Edge case logic and UX polish — implement last
16. Design Principles (Must Follow Throughout)
#	Principle	Description
P1

Single source of truth

PB1 drives all reporting. Master mapping sheet drives all SME data. No secondary/shadow data sources
P2

No duplicate data entry

Capture information once, reuse everywhere. Merge sections, remove duplicate fields, auto-populate where possible
P3

No assumptions

Log only verified/known data. Never infer status, timestamps, or field values. Leave unknown fields empty
P4

Auto-calculate where possible

Shift, Completion Date/Time, Failure Date/Time, Process Chain Runtime, PC Running for Last — all auto-derived, never manual
P5

Enforce data quality

Dropdowns preferred over free-text (except Failure Reason per manager), mandatory fields marked in RED, numeric constraints on count fields, selection-only SME field
P6

Consistent outputs

Hourly report = daily report in content and wording. No conflicting descriptions across report types
P7

Clear state tracking

Previous Status + Current Status with correct time context. Four defined states: Failed, Fixed, Regarding, Completed
P8

Proactive escalation

Runtime thresholds trigger visual alarms automatically. No reliance on manual detection of overruns
P9

Manager's direction takes priority

Where transcript discussion conflicts with manager's requirements, follow the manager's specification
