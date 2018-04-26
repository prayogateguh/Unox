<?php

function api($email,$pass)
{
   if(isset($email) && isset($pass)) {
      $ch = curl_init('http://wordai.com/users/account-api.php');
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
      curl_setopt ($ch, CURLOPT_POST, 1);
      curl_setopt ($ch, CURLOPT_POSTFIELDS, "email=$email&pass=$pass");
      $result = curl_exec($ch);
      curl_close ($ch);
      return $result;
   } else {
      return 'Error: Not All Variables Set!';
   }
}

echo api('info@vindtspecialist.nl','Gr3at3st01');
echo PHP_EOL;
