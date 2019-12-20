cls
$regexPattern = "(?<id>[Ss]horts)"
$regexPatternDino = "(?<Dinosaur>[Bb]aby [Dd]ino.+)"


$regexHtmlFile = "(?<root>.+)(?<suffix>\.html)"
$regexAspFile = "(?<root>.+)(?<suffix>\.asp)"
$regexAspxFile = "(?<root>.+)(?<suffix>\.aspx)"
$regexTxtFile = "(?<root>.+)(?<suffix>\.txt)"

function Convert-MyFile($filepath, $outfile){
    'processing ' + $filepath
    'outfile ' + $outfile

    $now = Get-Date -Format "yyy-MM-dd HH:mm"
    "<!-- File converted $now -->" | Out-File -FilePath $outfile

    foreach ($line in Get-Content $filepath) 
    {
        if($line -match $regexPattern)
        {
            # "Match found $Matches" 
            $line = $line.Replace($Matches.id, "baby dinosaur")
            $line | Out-File -FilePath $outfile -Append
        }
        elseif ($line -match $regexPatternDino)
        {
            $line = $line.replace($Matches.Dinosaur, "shorts")
            $line | Out-File -FilePath $outfile -Append
        }
        else 
        {
            $line | Out-File -FilePath $outfile -Append
        }
    }
    return "True"
}

$sourceDir = Get-Location
$destDir = "$sourceDir Converted"
"Source Directory : $sourceDir"

# Createing a new dir if it is not there
if (-Not(Test-Path $destDir)){
    New-Item "$destDir\" -ItemType "directory"
}
else {
    # Else remove everything in it if it.
    Remove-Item -Path $destDir -Include *.* -Recurse
}

foreach($newDir in Get-ChildItem -Path $sourceDir)
{
    $AddOn = $newDir | Split-Path -Leaf
    if(-Not(Test-Path $destDir\$AddOn))
    {   if(-Not($AddOn.Contains('.')))
        {
            New-Item "$destDir\$AddOn" -ItemType "directory"
        }
    }
    else 
    {
        Remove-Item -Path "$destDir\$AddOn" -Include *.* -Recurse
    }
}

foreach ($dirPath in Get-ChildItem -Path $sourcedir){
    foreach($aa in Get-ChildItem -Path $dirPath.FullName ){
        $filepath = $aa.FullName
        if(($filepath -match $regexHtmlFile) -or ($filepath -match $regexAspFile) -or ($filepath -match $regexAspxFile) -or ($filepath -match $regexTxtFile))
        {
            # map to destination directory/filename 
            $outfile = $Matches.root.Replace($sourceDir,$destDir) + $Matches.suffix
            "Out file : $outfile"
            Convert-MyFile "$filepath" $outfile
        }
        else 
        {
         'not found'   
        }
    }
}

echo "Match count total : " $Matches.Count