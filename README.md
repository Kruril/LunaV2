# Luna
![Moon](/assets/luna.ico)

Le projet a pour but d'ajouter dans un calendrier les phases lunaire.
Pour ce faire, il a va rechercher les informations via l'API : https://www.icalendar37.net/lunar/api/ .


L'application est déployé sur les services d'Amazon Web Services
## Services AWS utilisés
- AWS CloudFormation
- AWS Lambda
- AWS CloudWatch


L'application utilise les services de Google concernant la connection à l'agenda.
Il faut alors ajouter un fichier credentials.json dans le dossier [lambdas/create_event](https://github.com/Kruril/LunaV2/lambdas/create_event)
