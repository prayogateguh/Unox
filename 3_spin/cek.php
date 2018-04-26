<?php

# file ini digunakan untuk mengecek apakah $raw1 sama dengan $raw2
# ditest untuk mengetahui apakah hasil dari spintax itu unik atau tidak

$raw1 = explode("\n", file_get_contents('single_spintax.csv'));
$raw2 = explode("\n", file_get_contents('single_spintax2.csv'));

if ($raw1 == $raw2) {
    echo "Yes".PHP_EOL;
} else {
    echo "No".PHP_EOL;
}
