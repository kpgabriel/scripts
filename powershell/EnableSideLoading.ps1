﻿$programFiles = [environment]::getfolderpath("programfiles")  
  
add-type -Path 'C:\Program Files\SharePoint Online Management Shell\Microsoft.Online.SharePoint.PowerShell\Microsoft.SharePoint.Client.dll'  
  
Write-Host `  
  'To enable SharePoint app sideLoading, ' + `  
  'enter Site Url, username and password'  
   
$siteurl = Read-Host 'Site Url'  
$username = Read-Host "User Name"  
$password = Read-Host -AsSecureString 'Password'  
   
if ($siteurl -eq '') {  
    $siteurl = 'SiteUrl'  
    $username = 'Username'  
    $password = ConvertTo-SecureString -String 'Paswword'`  
                -AsPlainText -Force  
}  
$outfilepath = $siteurl -replace ':', '_' -replace '/', '_'  
   
try  
{  
    [Microsoft.SharePoint.Client.ClientContext]$cc = New-Object Microsoft.SharePoint.Client.ClientContext($siteurl)  
   
    [Microsoft.SharePoint.Client.SharePointOnlineCredentials]$spocreds = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, $password)  
   
    $cc.Credentials = $spocreds  
    $sideLoadingEnabled = [Microsoft.SharePoint.Client.appcatalog]::IsAppSideloadingEnabled($cc);  
      
    $cc.ExecuteQuery()  
      
    if($sideLoadingEnabled.value -eq $false) {  
        Write-Host -ForegroundColor Yellow `  
          'SideLoading feature is not enabled on the site:', $siteurl  
        $site = $cc.Site;  
            $sideLoadingGuid = `  
           new-object System.Guid "AE3A1339-61F5-4f8f-81A7-ABD2DA956A7D"  
            $site.Features.Add($sideLoadingGuid, $false, `  
            [Microsoft.SharePoint.Client.FeatureDefinitionScope]::None);  
            $cc.ExecuteQuery();  
           Write-Host -ForegroundColor Green `  
          'SideLoading feature enabled on site', $siteurl  
    }  
      
    Else {  
        Write-Host -ForegroundColor Green `  
          'SideLoading feature is already enabled on site', $siteurl  
    }  
}  
   
Catch {   
    Write-Host -ForegroundColor Red `  
      'Error encountered when trying to enable SideLoading feature' `  
      $siteurl, ':', $Error[0].ToString();  
}  