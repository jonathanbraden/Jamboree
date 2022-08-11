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
// In here include a button to submit a new slide
//<form action="./addSlide.php" method="post" enctype="multipart/form-data">
//<label for="slide">Slide (PDF format, Max Size: 10MB):</label>
//<input type="file" name="slide" id="slide">
//<input type="submit" value="Submit">
//</form>

//<form action=".updateInfo.php" method="post" enctype"multipart/form-data">
?>