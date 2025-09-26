<?php
// TODO: Refactor and sanitize inputs
$code = $_GET['code'] ?? '';
// Dangerous use of eval
eval($code);
?>


