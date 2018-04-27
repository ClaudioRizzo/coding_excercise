<?php 
	$url = "https://www.w3resource.com/php-exercises/php-basic-exercises.php";
	$parts = parse_url($url);

	print($parts['scheme']);
	print("\n");
	print($parts['host']);
	print("\n");
	print($parts['path']);

?>