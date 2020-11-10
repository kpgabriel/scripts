$clientId = 'eaccfc4e-fe1e-49d7-9882-8cc505c72733'

$bytes = New-Object Byte[] 32
$rand = [System.Security.Cryptography.RandomNumberGenerator]::Create()
$rand.GetBytes($bytes)
$rand.Dispose()
$newClientSecret = [System.Convert]::ToBase64String($bytes)
New-MsolServicePrincipalCredential -AppPrincipalId $clientId -Type Symmetric -Usage Sign -Value $newClientSecret -StartDate (Get-Date) -EndDate (Get-Date).AddYears(3)
New-MsolServicePrincipalCredential -AppPrincipalId $clientId -Type Symmetric -Usage Verify -Value $newClientSecret -StartDate (Get-Date) -EndDate (Get-Date).AddYears(3)
New-MsolServicePrincipalCredential -AppPrincipalId $clientId -Type Password -Usage Verify -Value $newClientSecret -StartDate (Get-Date) -EndDate (Get-Date).AddYears(3)
$newClientSecret