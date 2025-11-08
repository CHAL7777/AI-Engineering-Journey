<?php
$numbers = [4, 1, 7, 4, 2, 1];

$unique = array_unique($numbers);
sort($unique);

echo "Sorted Unique Array: [" . implode(", ", $unique) . "]<br>";
echo "Count: " . count($unique);
?>
