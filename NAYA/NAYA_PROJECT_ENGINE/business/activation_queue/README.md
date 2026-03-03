# Project First Execute

## Rôle

Ce dossier contient les projets à exécuter en priorité
après l’activation universelle de Naya,
une fois que Naya est considérée comme **READY**.

Ces projets constituent les premières créations
et les premières actions stratégiques de Naya,
sélectionnées intentionnellement.

## Principe d’exécution

- Aucun projet dans ce dossier ne s’exécute automatiquement
- Aucun point d’entrée global n’est présent
- Les projets sont appelables uniquement via orchestration
- L’ordre d’exécution est décidé par l’orchestrateur,
  après validation de l’état READY de Naya

## Contenu

Chaque sous-dossier correspond à un projet indépendant.

Exemples :
- SERVICE_1_ALIBABA
- SERVICE_2_SAMSUNG
- SERVICE_3_SAP_ARIBA

Chaque projet contient :
- une définition de service (`service_definition.py`)
- un manifeste (`manifest.json`)
- une documentation propre (`README.md`)
- des dépendances locales si nécessaires (`requirements.txt`)

## Positionnement architectural

Ce dossier est :
- post-activation
- pré-orchestration globale
- prioritaire mais non automatique

Il ne constitue pas un point d’activation.
Il est lu et exploité par l’orchestration de Naya.
