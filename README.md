Startup Finder - Île-de-France
# Description
Startup Finder est une application de localisation qui aide les accélérateurs et incubateurs à identifier et visualiser les startups en Île-de-France. Notre outil offre une cartographie interactive des startups, permettant une recherche efficace par secteur, stade de développement, et localisation.

# Fonctionnalités
Carte Interactive : Visualisez les startups sur une carte avec des filtres par secteur et stade de développement.
Recherche Avancée : Trouvez des startups par nom, secteur d'activité, et localisation.
Détails de Startup : Accédez aux informations détaillées des startups, incluant l'année de création, les fondateurs, et les liens vers leur site web.
Filtres Dynamiques : Affinez votre recherche avec des filtres sur la taille de l'équipe, le financement, et plus encore.
Intégration avec des Services Externes : Exportez les données vers CSV ou intégrez avec des CRM populaires.

# Installation
## Prérequis 
Node.js (version 14.x ou supérieure) \n
npm (version 6.x ou supérieure) ou Yarn
MongoDB (ou un autre base de données compatible)

## Étapes d'Installation

Clonez le dépôt :
git clone https://github.com/sekheul/OSINT.git
cd startup-finder

Installez les dépendances :
npm install
yarn install

Configurez les variables d'environnement :
Créez un fichier .env à la racine du projet et ajoutez vos variables d'environnement :

MONGODB_URI=mongodb://localhost:27017/startup-finder
PORT=3000

Démarrez l'application :
npm start
yarn start
L'application sera accessible sur http://localhost:3000.

# Utilisation
## Accéder à la Carte Interactive
1. Rendez-vous sur la page d'accueil de l'application.
2. Utilisez la carte pour explorer les startups en Île-de-France.
3. Appliquez des filtres selon le secteur, stade de développement, ou d'autres critères.

## Recherche de Startups
1. Utilisez la barre de recherche pour entrer des mots-clés.
2. Visualisez les résultats directement sur la carte ou dans la liste de résultats.

## Accéder aux Détails
1. Cliquez sur une startup sur la carte pour voir un aperçu.
2. Cliquez sur le lien pour accéder à la page détaillée de la startup avec plus d'informations.

# Contribuer
Nous accueillons les contributions pour améliorer Startup Finder. Pour contribuer, veuillez suivre les étapes suivantes :

1. Fork le projet.
2. Créez une branche pour votre fonctionnalité ou correction (git checkout -b feature/ma-fonctionnalite).
3. Commitez vos modifications (git commit -am 'Ajoute une nouvelle fonctionnalité').
4. Poussez la branche (git push origin feature/ma-fonctionnalite).
5. Créez une Pull Request.

# Licence
Ce projet est sous license CC BY-NC-SA 4.0 

# Crédits
Développeurs : Baye Ibrahima NDIAYE
Design : [Nom du Designer]
Données : [Source de données]

# Contact
Pour toute question ou suggestion, contactez-nous à sekheul96@gmail.com.


