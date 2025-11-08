<?php
function findMaxMin($arr) {
    $max = $arr[0];
    $min = $arr[0];

    foreach ($arr as $num) {
        if ($num > $max) $max = $num;
        if ($num < $min) $min = $num;
    }

    echo "Max: $max, Min: $min";
}

findMaxMin([10, 5, 25, 7, 15]);
?>
