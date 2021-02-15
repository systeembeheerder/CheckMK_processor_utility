## Check_MK standard uses \Processor(*)\% Processor Time
## We would like to use \Processor Information(*)\% Processor Utility
Write-Host "<<<processor_utility>>>"
$Counter = Get-Counter -Counter "\processor information(*,_total)\% processor utility"
$Counter.CounterSamples | ForEach-Object {
  Write-Host ($_.InstanceName.SubString(0,1)) $([math]::Round($_.CookedValue,0))
}
