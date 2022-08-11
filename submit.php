<?php
include 'functions.php';
$basedir = "/cita/d/www/home/jbraden/Jamboree/";
$datadir = "Data/";

//if ( !file_exists($datadir) ) {
//   echo "Making directory";
//   $worked = mkdir("Data",0744);
//   echo $worked;
//   file_put_contents($datadir.'test.txt','Hello, World');
//}

$name = trim($_POST["name"]); 
$title = $_POST["title"];
$abstract = $_POST["abstract"];
$email = $_POST["email"];
$type = $_POST["type"];
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
$obj->type=$type;
$obj->title=$title;
$obj->abstract=$abstract;
$obj->email=$email;
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
       echo "<h2>Error uploading slide.</h2>";
       echo "<b>Reason for error: </b>";
       switch ($_FILES['slide']['error']) { 
         case 1:
       	   echo "Slide size exceeds PHP server limit of 10MB.  ";
	   echo "Please reduce slide size and resubmit";
	   break;
	 case 2:
	   echo "Slide size exceeds 10MB.  ";
	   echo "Please reduce slide size and resubmit";
	   break;
	 case 3:    	  
	   echo "Upload was interupted";
	   break;
	 case 4:
	   echo "No slide was included.";
	   break;
      }
      echo "<br><br>Please upload your slide(s) by October 4th.<br>";
      echo "<br>The following information has been recorded."; 
      echo "<h3>Summary</h3>";
      echo "<b>Name</b>: $name<br>";	  
      echo "<b>Email</b>: $email<br>";
      echo "<b>Long Talk</b>: $type<br><br>";
      echo "<b>Title</b>: $title<br>";
      echo "<b>Abstract</b>:<br>";
      echo "$abstract<br>";
      return;
}

// Figure out why displayInfo doesn't work to replace this
echo "<h3>Summary</h3>";
echo "<b>Name</b>: $name<br>";
echo "<b>Email</b>: $email<br><br>";
echo "<b>Title</b>: $title<br>";
echo "<b>Abstract</b>:<br>";
echo "$abstract<br>";
echo "<a href='$newslide'>Preview Slide</a>";
?>
