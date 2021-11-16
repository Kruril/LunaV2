# Luna
![Moon](/assets/luna.ico)

Le projet a pour but d'ajouter dans un calendrier les phases lunaire.
Pour ce faire, il va rechercher les informations via l'API : https://www.icalendar37.net/lunar/api/ .


L'application est déployé sur les services d'Amazon Web Services
### Services AWS utilisés
- AWS CloudFormation
- AWS Lambda
- AWS CloudWatch
- AWS EventBridge
- AWS S3


L'application utilise les services de Google concernant la connection à l'agenda.
Il faut alors ajouter un fichier credentials.json dans un bucket d'AWS S3

### le fichier credentials.json contient :
- token
- refresh_token
- token_uri
- client_id
- client_secret
- scopes
- expiry
