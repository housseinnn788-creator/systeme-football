#!/bin/bash

FILE="players.txt"

touch $FILE

while true
do

echo "=============================="
echo "CLUB MANAGEMENT "
echo "=============================="

echo "1. Ajouter un joueur"
echo "2. Afficher les joueurs"
echo "3. Supprimer un joueur"
echo "4. Rechercher un joueur"
echo "5. Quitter"

read -p "Choix : " choix

case $choix in

1)

read -p "Nom du joueur : " nom

read -p "Age : " age

read -p "Position : " position

read -p "Nombre de buts : " buts

echo "$nom | $age | $position | $buts" >> $FILE

echo "Joueur ajouté avec succès."

;;

2)

echo "===== LISTE DES JOUEURS ====="

cat $FILE

;;

3)

read -p "Nom du joueur à supprimer : " nom

grep -v "^$nom" $FILE > temp.txt

mv temp.txt $FILE

echo "Joueur supprimé."

;;

4)

read -p "Nom du joueur : " nom

grep "$nom" $FILE

;;

5)

echo "Au revoir."

exit

;;

*)

echo "Choix invalide."

;;

esac

echo ""

done