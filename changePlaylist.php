
<?php

$row = 1;
$update = "";
//on stocke en variable le séparateur de csv utilisé
$separator = ";";

//on crée deux variables contenant les index des colonnes à lire / modifier
$idx_ambiance = 0;
$idx_playlist = 1;

$ambiance = $_POST['ambiance'];
$playlist = $_POST['playlist'];
//on ouvre le fichier en écriture
if (($handle = fopen("Ambience.csv", "r")) !== FALSE)
{

        //on parcours le fichier ligne à ligne, en stockant dans un tableau les donnée
    while (($data = fgetcsv($handle, 1000, ";")) !== FALSE)
    {
        //on ne commande qu'à la deuxième ligne, su la première contient les entêtes de colonnes
        
       
                //on fait les tests sur le nom
                if ($data[$idx_ambiance] ==  $ambiance)
                {
                        $data[$idx_playlist] = $playlist;
                }

                $update .= implode($separator,$data)."\r\n";
                $row++;
    		   
	}
    fclose($handle);
}

//on ouvre le fichier en ecriture et on le met à jour
$ouvre=fopen("Ambience.csv","w");
fwrite($ouvre,$update);
fclose($ouvre);
?>
