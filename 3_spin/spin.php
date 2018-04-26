<?php

# program ini digunakan untuk spin artikel
# akan menghasilkan output yang masih spintax, nanti harus
# dijalankan program spintax
# silakan ubah input dan output

$articles = [];

function api($text,$quality,$email,$pass)
{
   if(isset($text) && isset($quality) && isset($email) && isset($pass))
   {
      $text = urlencode($text);
      $ch = curl_init('http://wordai.com/users/turing-api.php');
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
      curl_setopt ($ch, CURLOPT_POST, 1);
      curl_setopt ($ch, CURLOPT_POSTFIELDS, "s=$text&quality=$quality&email=$email&pass=$pass&output=plaintext");
      $result = curl_exec($ch);
      curl_close ($ch);
      return $result;
   }
   else
   {
      return 'Error: Not All Variables Set!';
   }
}

function ubahQuote($teks)
{
    $teks = explode('";"', $teks);
    $article = [];
    array_push($article,
        $teks[0].'"',
        '"'.$teks[1].'"',
        '"'.$teks[2].'"',
        '"'.$teks[3]
    );
    $teks = $article;
    $teks[0] = str_replace("‘", "'", $teks[0]);
    $teks[0] = str_replace("’", "'", $teks[0]);
    $teks[0] = str_replace("“", '"', $teks[0]);
    $teks[0] = str_replace("”", '"', $teks[0]);
    $teks[1] = str_replace("‘", "'", $teks[1]);
    $teks[1] = str_replace("’", "'", $teks[1]);
    $teks[1] = str_replace("“", '"', $teks[1]);
    $teks[1] = str_replace("”", '"', $teks[1]);
    $teks[2] = str_replace("‘", "'", $teks[2]);
    $teks[2] = str_replace("’", "'", $teks[2]);
    $teks[2] = str_replace("“", '"', $teks[2]);
    $teks[2] = str_replace("”", '"', $teks[2]);
    $teks[3] = str_replace("‘", "'", $teks[3]);
    $teks[3] = str_replace("’", "'", $teks[3]);
    $teks[3] = str_replace("“", '"', $teks[3]);
    $teks[3] = str_replace("”", '"', $teks[3]);

    $art = implode(';', $teks);
    return $art;
}

function bukaFile()
{
    $raw = explode("\n", file_get_contents('500.txt')); # input
    $raw = array_filter($raw);

    foreach($raw as $key=>$a) {
        echo "processing..."."$key".PHP_EOL;
        
        $article = [];
        if (strpos($a, '<No Title>') !== false) {
            continue;
        } else {
            echo "spining...".PHP_EOL;
            if ($a != NULL) {
                $a = ubahQuote($a);
                $hasilSpin = api($a,'Regular','info@vindtspecialist.nl','Gr3at3st01');
                array_push($article, $hasilSpin);
            }
            array_push($GLOBALS['articles'], $article);
        }
    }
}

function simpanTxt()
{
    $file = fopen("500.csv","a+") or exit("Unable to open file!"); # output

    foreach($GLOBALS['articles'] as $article) {
        if (isset($article[0])) {
            fwrite($file, $article[0]);
        }
    }

    fclose($file);
}

bukaFile();
simpanTxt();

echo "Program selesai";
echo PHP_EOL;

