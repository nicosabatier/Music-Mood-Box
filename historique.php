<?php
$row = 0;
$play = $_POST["playlist"];

echo "Historique des dernières écoutes de la playlist $play :<br>";
if (($handle = fopen("historique.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
        if($data[0] == $play){
        echo "$data[1]<br>";
        }
        $row++;
    }
    fclose($handle);
}
?>

