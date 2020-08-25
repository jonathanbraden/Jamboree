<?php
include 'functions.php';

$name = trim($_POST["name"]);
//$name = preg_replace('!\s+!', ' ',$name);
//$newname = str_replace(' ','_',$name);
$newname = convertName($name);
if ($newname == '') {
   echo "<h2>Error.  Please enter your name and retry.</h2>";
   return;
}
$jsFile = "Data/".$newname.".json";
if (!is_readable($jsFile)){
   echo $name." has not yet submitted";
   return;
}
displayInfo($jsFile);
?>