<?php
include 'functions.php';
$basedir = "/cita/d/www/home/~jbraden/jamboree/";
$datadir = "Data/";

$name = trim($_POST["name"]); 
$title = $_POST["title"];
$abstract = $_POST["abstract"];
$slide = $_FILES["slide"]["tmp_name"];
$slide_type = $_FILES["slide"]["type"];
$slide_name = chop($_FILES["slide"]["name"]);

// Figure out why I can't call convertName
$name = preg_replace('!\s+!', ' ',$name);
$newname = str_replace(' ','_',$name);
if ($newname == '') {
   echo "<h2>Error.  Please enter your name and resubmit.</h2>";
   return;
}

$base=$datadir.$newname;
$newslide = $base."-slide.pdf";
unlink($newslide);
unlink($base."-abstract.txt");
unlink($base."-title.txt");
unlink($base.".json");
file_put_contents($base."-abstract.txt",$abstract);
file_put_contents($base."-title.txt",$title);

$jsFile = $base.".json";
$obj->name=$name;
$obj->title=$title;
$obj->abstract=$abstract;
$obj->slide=$newslide;
file_put_contents($jsFile,json_encode($obj));

//makeJSON($jsFile,$name,$title,$abstract);

if ( is_uploaded_file($slide) ) {
   if (strtolower(substr($slide_name,-4))!='.pdf'){
     echo "<h2>Error uploading file.  Please resubmit.</h2>";
     echo "File isn't a PDF";
     return;	  
     }	  
   move_uploaded_file($slide,$newslide);
   echo "<h2>Submission Successful!</h2>";
} 
else {
       echo "<h2>Error uploading file.  Please resubmit.</h2>";
       switch ($_FILES['slide']['error']) { 
         case 1:
       	   echo "Slide size exceeds 10MB";
	 case 2:
	   echo "Slide size exceeds 10MB";
	 case 3:    	  
	   echo "Upload was interupted";
	 case 4:
	   echo "No slide was uploaded";   
      }
      return;
}

// Figure out why displayInfo doesn't work to replace this
echo "<h3>Summary</h3>";
echo "Name: $name<br>";
echo "Title: $title<br>";
echo "Abstract:<br>";
echo "$abstract<br>";
echo "<a href='$newslide'>Preview Slide</a>";
?>
