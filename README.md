# Lunar Landing Site Navigator

Projet pour le **NASA Space Apps Challenge 2026** — défi « Lunar Landing Site Navigator ».

Outil web pour comparer rapidement deux sites d'atterrissage lunaires : position du **Soleil** et de la **Terre** par rapport à l'horizon, potentiel d'**énergie solaire** et de **communication directe avec la Terre**, sur une période de 30 jours.

**Démo en ligne :** _(colle ici ton lien GitHub Pages)_

## Fonctionnalités
- Comparaison côte à côte de deux sites (17 sites : Apollo, Chang'e, Chandrayaan-3, SLIM, pôle sud / Artemis…).
- Choix de la date et décalage rapide (−1, +1, +3, +7 jours) pour simuler un retard d'atterrissage.
- Vue « ciel » (Soleil et Terre vs horizon) et courbes d'élévation sur 30 jours.
- Verdicts simples : énergie (bonne / moyenne / faible) et communications (continues / par fenêtres / très limitées).
- Temps restant avant le prochain coucher ou lever du Soleil et de la Terre.
- Site personnalisé (latitude / longitude) avec un modèle simplifié, **indicatif seulement**.

## Données
Les positions du Soleil et de la Terre viennent du système **JPL Horizons**, interrogé par `fetch_horizons.py` (pas de 2 h, 120 jours à partir du 15/11/2026) et enregistrées dans `data.json`.

Régénérer les données :
```
python fetch_horizons.py 2026-11-15 120
```

## Fichiers
- `index.html` : l'application (une seule page, aucune dépendance)
- `data.json` : données précalculées
- `fetch_horizons.py` : script de récupération des données

## Limites
- Horizon supposé **plat** : le relief réel (données LOLA) n'est pas pris en compte. Les fonds de cratères en ombre permanente ne sont donc pas représentés correctement.
- Les coordonnées de certains sites sont arrondies.
- Hors des dates couvertes par `data.json`, et pour un site personnalisé, l'appli utilise un modèle simplifié approximatif.

## Pistes d'amélioration
Intégrer le relief LOLA pour calculer l'horizon réel, ajouter des sites, calculer les éphémérides pour des coordonnées libres.

## Sources et crédits
- [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) (NASA/JPL)
- [Quickmap](https://quickmap.lroc.asu.edu/) (ASU / LROC) et [Moon Trek](https://trek.nasa.gov/moon/) (NASA) pour l'exploration du terrain
- [Agence spatiale canadienne](https://www.asc-csa.gc.ca/eng/astronomy/moon-exploration/)

Ce projet est indépendant : il n'est ni approuvé ni endossé par la NASA, qui n'est pas responsable de son contenu. Les données restent soumises aux conditions d'utilisation de chaque source.
