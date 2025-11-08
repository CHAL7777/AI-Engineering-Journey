<?php
$a = 25;
$b = 40;
$c = 15;

if ($a >= $b && $a >= $c) {
    $largest = $a;
} elseif ($b >= $a && $b >= $c) {
    $largest = $b;
} else {
    $largest = $c;
}

echo "Numbers: $a, $b, $c <br>";
echo "Largest: $largest";
?>
