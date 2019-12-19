###
# 'run.ps1'
# This script will take a value in an input xslx file and store the 
# left cell as a list of server names 
# this list will then be used to update the right cell in the matching
# output xslx file
#
# Author/CopyRight: Gabriel, Kyle
# Last Edit Date: 12-18-2019
###

cls
### Variables
$xslx_object = New-Object -ComObject Excel.Application
$xslx_object.Visible = $false
$input_path = "C:\temp\input.xlsx"
$output_path = "C:\temp\output.xlsx"
$server_list = New-Object Collections.Generic.List[String]

# WorkBook stream
Write-Output "Opening IO Files"
$input_wb = $xslx_object.Workbooks.Open($input_path,$true) #opend in read-only mode
Write-Output "Opened Input: $input_path"
$output_wb = $xslx_object.Workbooks.Open($output_path)
Write-Output "Opened Output: $output_path"

# Sheet Object
Write-Output "Opening Sheets"
$input_sheet = $input_wb.Worksheets.Item("Sheet1")
Write-Output "Opening Input Sheet: Sheet1"
$output_sheet = $output_wb.Worksheets.Item("Server_VM List")
Write-Output "Opening Output Sheet: Server_VM List"

$input_row_max = ($input_sheet.UsedRange.Rows).count   
$output_row_max = ($output_sheet.UsedRange.Rows).count   
Write-Output "Max Rows Found In: $input_row_max"
Write-Output "Max Rows Found Out: $output_row_max"
$row_server_name,$col_server_name = 1,2
$row_status_in,$col_status_in = 1,30
$row_status_out,$col_status_out = 1,26

# Computation, check if colum s Success, if so capture sever name 
for ($i=1; $i -le $input_row_max-1; $i++) { 
		$status_found = $input_sheet.Cells.Item($row_status_in+$i,$col_status_in).text
		$server_name = $input_sheet.Cells.Item($row_server_name+$i,$col_server_name).text 
		# Write-Output "Checking $status_found"
		if ($status_found -eq "Successful") {
			# Write-Output "  Adding $server_name"
			$server_list.Add($server_name)
		}
}
Write-Output "Servers Added to List: " $server_list.Count

# # Computation, check if colum s Success, if so capture sever name 
for ($i=1; $i -le $output_row_max-1; $i++) {
	$server_found = $output_sheet.Cells.Item($row_server_name+$i,$col_server_name).text 
	if ( $server_list.Contains($server_found) ) {
		Write-Output "Found Matching $server_found"
		$output_sheet.Cells.Item($row_status_out+$i,$col_status_out) = "Yes";
	}
}

# cleanup
$ext=".xlsx"
$path="C:\temp\output_new$ext"
$output_wb.SaveAs($path) 
$process = ((get-process excel | select MainWindowTitle, ID, StartTime | Sort StartTime)[-1]).Id
Stop-Process -Id $process