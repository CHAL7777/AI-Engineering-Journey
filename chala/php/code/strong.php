<?php
$password = "Pass1234";

if (strlen($password) >= 8 && preg_match("/[A-Za-z]/", $password) && preg_match("/[0-9]/", $password)) {
    echo "Strong Password";
} else {
    echo "Weak Password";
}
?>
