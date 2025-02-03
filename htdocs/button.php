<?php
   
   var_dump($_GET);
   for($i=0; $i<$_GET['bcount']; $i++) {
      echo "<button>".$i."</button>";
   }
    

   ?>