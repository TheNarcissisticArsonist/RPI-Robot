<?php

$m1 = $_GET["m1"];
$m2 = $_GET["m2"];
$m3 = $_GET["m3"];
$m4 = $_GET["m4"];

$motorFile = fopen("motor_instructions.txt", "w");
$instructions = $m1." ".$m2." ".$m3." ".$m4;
fwrite($motorFile, $instructions);
fclose($motorFile);

echo("Received ".$m1." ".$m2." ".$m3." ".$m4);

?>
