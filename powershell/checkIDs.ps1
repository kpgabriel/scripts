$clientId = 'dff9e1d7-f97c-4f2c-adbb-b0e8fbf1505c'
(Get-MsolServicePrincipalCredential -AppPrincipalId $clientId -ReturnKeyValues $true).EndDate.ToShortDateString() | select -first 1
