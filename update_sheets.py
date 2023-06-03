import gspread

def write_sheet(spreadsheet_key, template_sheet_id, findings, today):
    gc = gspread.service_account()
    spreadsheet = gc.open_by_key(spreadsheet_key)
    sheet = spreadsheet.duplicate_sheet(template_sheet_id, new_sheet_name=today)
    values = [finding.cells() for finding in findings]
    sheet.append_rows(values, value_input_option="USER_ENTERED")