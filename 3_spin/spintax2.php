<?php

# program ini digunakan untuk menghasilkan artikel final dari spintax wordai
# silakan ubah input dan output

$raw = explode("\n", file_get_contents('50.csv')); # input
 
/**
 * @name SpinTax
 * @var str Text containing our {spintax|spuntext}
 * @return str Text with random spintax selections
 */
function SpinTax($s) {
    preg_match('#{(.+?)}#is',$s,$m);
    if(empty($m)) return $s;
 
    $t = $m[1];
 
    if(strpos($t,'{')!==false){
            $t = substr($t, strrpos($t,'{') + 1);
    }
 
    $parts = explode("|", $t);
    $s = preg_replace("+{".preg_quote($t)."}+is", $parts[array_rand($parts)], $s, 1);
 
    return SpinTax($s);
}

$articles = [];
foreach ($raw as $article) {
    array_push($articles, SpinTax($article));
}

$file = fopen("50_spintax.csv","a+") or exit("Unable to open file!"); # output
foreach($articles as $article) {
    if (isset($article)) {
        fwrite($file, $article);
    }
}

echo "Program Selesai".PHP_EOL;
