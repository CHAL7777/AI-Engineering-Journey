<?php
$length = 8; 
$chars = 'abcdefghijklmKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()';

$shuffled = str_shuffle($chars);
$password = substr($shuffled, 0, $length);

echo "Random Password: $password";
?>
