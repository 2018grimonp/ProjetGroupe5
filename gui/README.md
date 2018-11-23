Il s'agit d'une interface web qui permet de traduire les données obtenues à l'aide du programme en python.
Il affiche des diagrammes circulaires en utilisant du javascript sur un canvas et du php côté back-end.

Le programme en python3 doit générer le fichier results.txt qui contient les données du diagramme.
Demander à geoffroy pour la documentation.

Voici un exemple de results.txt :

	
	Graphique1-DescriptionDuGraphique1-pourcentage1+pourcentage2+pourcentage3+pourcentage4-10+20+30-124-|Graphique2-DescriptionDuGraphique2-pourcentage 1+pourcentage 2+pourcentage 3+pourcentage 4-20+20+20- Note 9/10 -


Les graphiques sont séparés par |. Leur nombre est infini. Graphique 1 et 2 sont les titres des graphiques. pourcentage[...] sont les légendes des différentes proportions représentées par les pourcentages 10,20,30. (Le pourcentage 4 est omis puisqu'il doit s'agir du reste)
124 et Note 9/10 sont des légendes à côté des graphiques qui peuvent représenter, entre autres, des notes associées aux graphiques.

Le tiret achevant chacun des graphiques est important pour éviter d'ajouter des \n
