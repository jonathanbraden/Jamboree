<!DOCTYPE html>
<html>
<body>

<?php
//if (ini_get('file_uploads') == 1)
//{ echo 'HTTP upload enabled'; }
//else
//{ echo 'HTTP upload disabled'; }
?>

<h1>CITA Jamboree Slide Submission</h1>
Contact either Jonathan (jbraden@cita.utoronto.ca) or Almog (ayalin@cita.utoronto.ca) if you have problems.<br><br>

<form action="./submit.php" method="post" enctype="multipart/form-data">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name" size="50"><br>
  <label for="title">Title:</label><br>
  <input type="text" id="title" name="title" size="75"><br>
  <label for="abstract">Abstract:</label><br>
  <textarea id="abstract" name="abstract" placeholder="Enter your abstract" style="height:200px" cols="65" rows="25"></textarea><br>

  <input type="hidden" name="MAX_FILE_SIZE" value="10485760">
  <label for="slide">Slide (PDF format, Max Size: 10MB):</label> 
  <input type="file" name="slide" id="slide">
  <br>
  <input type="submit" value="Submit">
</form>

<br><br>
<h4>You can check your existing submission here</h4>
<form action="./check.php" method="post">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name" size="50"><br>
  <input type="submit" value="Check Submission">
</form>

</body>
</html>
