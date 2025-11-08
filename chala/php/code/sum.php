<?php
function sumArray($arr) {
    $sum = 0;
    foreach ($arr as $num) {
        $sum += $num;
    }
    return $sum;
}

$data = [10, 20, 30, 40];
echo "Sum: " . sumArray($data);
?>
