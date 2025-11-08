<?php
function maskEmail($email) {
    $pos = strpos($email, "@");
    $username = substr($email, 0, $pos);
    $domain = substr($email, $pos);
    $masked = substr($username, 0, 3) . str_repeat("*", strlen($username) - 3);
    return $masked . $domain;
}

echo maskEmail("wwww.johncena@.com");
?>
