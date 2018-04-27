<!DOCTYPE html>
<html>
<head>

</head>
<body>
	<title>A simple Form</title>
	<form method='GET'>
		<input type='text' name='name'>
		<input type='submit' name='submit'>
	</form>
	
	<?php 
		$name = strip_tags($_GET['name']); 
		echo "<h3> hello $name </h3>";
	?>
</body>
</html>

