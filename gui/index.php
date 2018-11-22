<html>
	<head>
		<script>
		
			<?php 
				//Ce code génère en php les affectations de variables en javascript qui correspondent aux proportions et aux légendes dans le graphique
				$content=file_get_contents("results.txt");                             //fonction native de php
				$charts=preg_split("/\|/",$content);                                   //on recupère graphe 1 et 2
				$_GET["step"]=min(intval($_GET["step"]),intval(count($charts))-1);     //n réaffecte une valeur à la variabe _GET["step"]
				$_GET["step"]=max(0,intval($_GET["step"]));
					
				$data=preg_split("/\-/",$charts[$_GET["step"]]);     //$_GET["step"] est un chiffre et $charts est un tableau, on recupere les diff parties des graphes
				$titles=preg_split("/\+/",$data[1]);                 //on recupère les parties des parties
				$L=preg_split("/\+/",$data[2]);                       //same
			
				$titles_txt="[";
				for($i=0;$i<count($titles)-1;$i++){
					$titles_txt=$titles_txt."'".$titles[$i]."',";
				}
				$titles_txt=$titles_txt."'".$titles[count($titles)-1]."']";
				
				$L_txt="[";
				for($i=0;$i<count($L)-1;$i++){
					$L_txt=$L_txt."".$L[$i].",";
				}
				$L_txt=$L_txt."".$L[count($L)-1]."]";

				echo "var title='".$data[0]."';\n";
				echo "var titles=".$titles_txt.";\n";
				echo "var L=".$L_txt.";\n";
				echo "var note='".addslashes($data[3])."';";


				//Ajout du code javascript
				echo file_get_contents("chart.js"); 
			?>
		
		</script>
		<meta charset="utf-8"/>
		
	</head>

	<!-- Code HTML de la page dont le canvas -->	
	<body style="position:flex;">
		<span style="font-size:30px;" id="title"></span>  <!-- boutons suivants et précédents -->
		<a style="text-decoration:none;" href="index.php?step=<?php echo intval($_GET["step"]-1);?>">&#8592; Précédent</a>&nbsp;
		<a style="text-decoration:none;" href="index.php?step=<?php echo intval($_GET["step"]+1);?>">Suivant &#8594;</a>
		<canvas style="top:50px;left:0;position:fixed;" id="canvas"></canvas>	
		<div style="color:white;" id="txt"></div>
	</body>













</html>
