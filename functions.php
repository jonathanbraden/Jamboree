<?php
  function convertName($name){
    $na = trim($name);
    $na = preg_replace('!\s+!',' ',$na);
    $na = str_replace(' ','_',$na);
    return $na;
  }

  function makeJSON($jsFile,$name,$title,$abstract){
    $obj->name=$name;
    $obj->title=$title;
    $obj->abstract=$abstract;
    $obj->slide=$slide;
    file_put_contents($jsFile,json_encode($obj));
  }  

  function displayInfo($jsFile){ // Display user information in JSON object
    $data = json_decode(file_get_contents($jsFile));
    echo "<h3>Summary</h3>";
    echo "Name: $data->name<br>";
    echo "Title: $data->title<br>";
    echo "Abstract<br>";
    echo "$data->abstract<br>";
    echo "<a href='$data->slide'>Preview Slide</a>";
  }	
?>