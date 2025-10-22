## Zehnder ComfoAir Q Custom Component

Deze custom component biedt verbeterde ondersteuning voor Zehnder ComfoAir Q350/450/600 ventilatiesystemen in Home Assistant.

### Voordelen ten opzichte van standaard integratie

- **Device Support**: Alle entiteiten worden gekoppeld aan één apparaat
- **UI Configuratie**: Geen YAML configuratie meer nodig
- **Alle Sensoren**: Automatisch alle 20+ sensoren beschikbaar

### Vereisten

- ComfoConnect LAN C bridge
- IP-adres van je bridge
- Optioneel: 32-karakter token (standaard wordt gebruikt indien niet ingesteld)

### Configuratie

Na installatie:
1. Ga naar **Instellingen** → **Apparaten & Services**
2. Klik op **+ Integratie toevoegen**
3. Zoek naar "Zehnder ComfoAir Q"
4. Voer het IP-adres van je bridge in
5. Klaar!

### Beschikbare Entiteiten

#### Fan
- Ventilator bediening met snelheidsregeling
- Auto modus support

#### Sensoren (automatisch toegevoegd)
- Temperaturen (binnen, buiten, toevoer, afvoer)
- Luchtvochtigheid (binnen, buiten, toevoer, afvoer)
- Ventilator snelheden en duty cycles
- Luchtstromen
- Bypass status
- Filteronderhoud (dagen tot vervanging)
- Energieverbruik

### Credits

Gebaseerd op de officiële Home Assistant ComfoConnect integratie door Michiel Arnauts.
