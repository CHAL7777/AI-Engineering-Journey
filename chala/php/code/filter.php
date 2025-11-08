<?php
function filterAboveAverage($arr) {
    $sum = array_sum($arr);
    $avg = $sum / count($arr);

    $above = [];
    foreach ($arr as $num) {
        if ($num > $avg) {
            $above[] = $num;
        }
    }

    echo "Average = $avg<br>";
    echo "Above Average: [" . implode(", ", $above) . "]";
}

filterAboveAverage([10, 20, 30, 40, 50]);
?>
