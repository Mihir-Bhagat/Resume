
Here's your requirement rewritten as clear, structured bullet points:

Monitoring Log Enhancements
1. Vertical Scrollable Section
Add a vertical scrollable element in the Monitoring Log screen to improve usability when handling large amounts of data.
2. New Section for In-Progress Process Chains
Add a new section for Process Chains that are currently In Progress.
If the Monitoring Team has already entered data for a Process Chain and the same Process Chain fails in a later extraction:
The system should identify the record using:
Process Chain Log ID
Meta Chain Log ID
The previously entered values should be automatically populated.
Users should be able to modify/update any prefilled values if required.
3. Running Since Logic
The Running Since value should be updated automatically based on the Process Chain status changes.
Example:
PC1 → Running → 1 Hour
PC1 → Completed → 2 Hours

The system should calculate and display the total runtime accurately.

4. Criticality Mapping Enhancement
Criticality should be fetched from the Master Data Excel file using the following columns:
Process Chain
Critical
Region
Frequency
Next Schedule Run
Process Type
Monitoring Member
RIC Assistance
Logic:
If the Process Chain exists in the Master Data:
Display the configured Criticality value.
If the Process Chain does not exist in Master Data:
Default Criticality = Not Critical.
Display High and Very High criticality values in Red Color for better visibility.
5. Housekeeping File Enhancement
Add an option in the Housekeeping functionality to allow users to select the storage location for housekeeping files.
The functionality should work similarly to the existing:
Archive
Extract
User should be able to specify the destination folder/path.
6. Incident Updated Flag
The Incident Updated option should be maintained at Process Chain level.
It should not be treated as a common/global field for all Process Chains.
7. Query Runtime Field
Add a new field:
Query Run Time
Applicable for Queries/Reports.
Display runtime information in the monitoring report.
8. PC Running for Last Field
Add a field:
PC Running for Last
Applicable only for Running Process Chains.
Requirements:
Auto-calculated.
Read-only.
Greyed out.
No manual editing allowed.
9. Shift Field Enhancement
Shift should be:
Auto-calculated.
Read-only.
Greyed out.
Derived based on configured shift timings.
10. Auto-Population of Previous Run Data
When a Process Chain with the same:
Process Chain Log ID
Meta Chain Log ID
appears again in subsequent extracts:
All previously entered monitoring values should be automatically populated.
Users should still be allowed to update the values if required.
Status Tracking Logic (Historical Status vs Current Status)

The system should maintain both:

Status at Extraction Time
Current Status
Scenario 1
Extract Date Status = Failed
Current Status = Failed
Display:
Extracted Status: Failed
Current Status: Failed
Scenario 2
First Extract:
Status = Failed
Later system refresh:
Status changes to Running
Display:
Extracted Status: Failed
Current Status: Running
Scenario 3
First Extract:
Status = Failed
Next Refresh:
Status = Running
Subsequent Refresh:
Status = Completed
Display:
Extracted Status: Failed
Current Status: Completed
11. Historical Status Preservation
The status captured during extraction should never be overwritten.
The system should always preserve:
Original Extracted Status
Current Live Status
This enables Monitoring Team members to understand:
What the status was when the record was extracted.
What the latest status is now.
12. Audit and Update Capability
All auto-populated data should remain editable.
Users should be able to revisit previous entries and update monitoring information whenever required.
Changes should be saved against the same Process Chain Log ID and Meta Chain Log ID combination.
