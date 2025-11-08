<?php
$input = "php is great and php is Fun";
$lowering = strtolower($input);
$arrs = explode(" ", $lowering); 
$word_count = array_count_values($arrs);

foreach ($word_count as $word => $count) {
    echo "$word => $count <br>";
}
?>
