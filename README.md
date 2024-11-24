
# NFI Assessment

Deze repository bouwt voort op de oorspronkelijke applicatie door de toevoeging van tests, een CI-pipeline, automatische code-formattering met **Black**, een API met JSON-ondersteuning, en een Docker-container voor eenvoudig deployen.

---

## Gebruik

1. **Installeren van afhankelijkheden**  
   Installeer de benodigde pakketten met:  
   ```bash
   pip install -r requirements.txt
   ```  
   Gebruik een virtual environment om conflicten te voorkomen.

2. **Oude code uitvoeren**  
   Voer de oorspronkelijke code uit met:  
   ```bash
   python code/main.py
   ```

3. **Tests uitvoeren**  
   De tests zijn gebaseerd op **pytest** en kunnen worden uitgevoerd met:  
   ```bash
   pytest
   ```

---

## API

De API is gebouwd met **FastAPI** en maakt gebruik van **Uvicorn** als server.  

### Starten van de API
Start de applicatie met:  
```bash
uvicorn api.api:app --reload
```

### Voorbeeldinvoer
Om data naar de API te sturen, gebruik een JSON-bestand met het volgende formaat:  

```json
{
  "spoor": "ACG",
  "profielen": ["ACG", "ACT"]
}
```

Een voorbeeldbestand is beschikbaar in:  
```plaintext
tests/test.json
```

### Aanroepen van de API
Stuur data naar de API met behulp van **cURL**:  
```bash
curl -X POST "http://127.0.0.1:8000/process" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@tests/test.json"
```

---

## Docker Container

Bij elke **push** bouwt GitHub Actions automatisch een nieuwe Docker-image als artefact.  

### Container draaien
Start de container met:  
```bash
docker run -p 8000:8000 nfi-app
```

### API gebruik binnen Docker
De API kan vervolgens op dezelfde manier worden aangeroepen als hierboven beschreven.

---

## Toelichting
### Keuze voor tools
Voor deze applicatie heb ik zoveel mogelijk standaardtools gebruikt, zoals uvicorn, FastAPI en black. Deze zijn makkelijk in het gebruik en zorgen voor code die snel te deployen is. 

### Uitdagingen
Het lastigste gedeelte van de opdracht is dat de oorspronkelijke code gebruikt wordt in een ```if __name__ == "__main__"``` statement. Hierdoor is de belangrijkste functionaliteit niet te importeren als een functie. Ook geeft de code niet standaard ouput, door het gebruik van print statements in plaats van return statements. Hoewel hiermee te werken is, maakt het de code erg gevoelig voor veranderingen. Zowel de tests als de utilities voor de API vertrouwen erop dat de print statements niet veranderen. Zodra de Nederlandse tekst verandert, breekt de applicatie. Hier was niet omheen te werken zonder de code te veranderen. In de praktijk was ik graag in gesprek gegaan met de schrijver van de code, om te kijken of deze manier van gebruiken noodzakelijk is. Nu heb ik de aanname gemaakt dat dat noodzakelijk is voor het gebruik van de app en heb ik dit gerespecteerd waar mogelijk. 

### Performance
Voor de performance testing heb ik een simpel script geschreven dat als parameters de lengte van de sequenties, het aantal sporen en het aantal herhalingen heeft. Hierdoor kan de test een realistisch beeld geven van de performance zodra we meer weten over hoe een gemiddelde API call eruit ziet. 

Verder heb ik nog gepoogd om de docker container licht te houden door het scheiden van de requirements in ```requirements.txt``` en ```requirements-dev.txt``` en het uitsluiten van niet noodzakelijke onderdelen zoals de tests en de markdown bestanden. 

### Uitbreidingen
Als uitbreiding op wat ik heb gebouwd zou ik de volgende dingen meenemen:
- Het refactoren van de oorspronkelijke code.
- Een multistage build voor de docker file.
- Het uploaden van de dockerfile naar de Docker Hub, zodat het makkelijk toegankelijk is bij de toevoeging van Continuous Deployment voor de volledige CI/CD pipeline.
- Documentatie van de applicatie. 

