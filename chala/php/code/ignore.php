<?php
function countChars($str) {
    $str = str_replace(" ", "", strtolower($str));
    $chars = str_split($str);
    $count = array_count_values($chars);

    foreach ($count as $char => $num) {
        echo "$char → $num <br>";
    }
}

countChars("hello");
?>
