<?php
$f_num = $_GET['fnum'];
$s_num = $_GET['snum'];
$operator = $_GET['operator'];
    
      
$cal = 0;

switch($operator) {
    case '+':
        $cal = $f_num + $s_num;
        break;
}

echo 'TOTAL IS ', $cal;
?>
