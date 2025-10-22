# ComfoConnect Home Assistant Custom Component

Deze custom component voor Home Assistant biedt ondersteuning voor de Zehnder ComfoAir Q350/450/600 ventilatiesystemen via de ComfoConnect LAN C bridge.

## Credits

Deze integratie is gebaseerd op de [officiële Home Assistant ComfoConnect integratie](https://www.home-assistant.io/integrations/comfoconnect) door [@michaelarnauts](https://github.com/michaelarnauts) en het Home Assistant Core team. De originele code maakt gebruik van de [pycomfoconnect](https://github.com/michaelarnauts/comfoconnect) library.

**Originele auteurs:**
- Michiel Arnauts ([@michaelarnauts](https://github.com/michaelarnauts))
- Home Assistant Core Team

**Custom component aanpassingen:**
- Tim van der Hoorn ([@timvdhoorn](https://github.com/timvdhoorn))

## Belangrijkste wijzigingen

Deze versie is een aangepaste variant van de standaard Home Assistant ComfoConnect integratie met de volgende verbeteringen:

- **Device ondersteuning**: Alle entiteiten worden nu gekoppeld aan één apparaat in Home Assistant
- **Modern config flow**: Eenvoudige configuratie via de UI in plaats van YAML
- **Alle sensoren beschikbaar**: Alle 20+ sensoren worden automatisch toegevoegd (geen handmatige configuratie meer nodig)

## Installatie

### Via HACS (aanbevolen)

1. Open HACS in Home Assistant
2. Ga naar "Integrations"
3. Klik op de drie puntjes rechtsboven en selecteer "Custom repositories"
4. Voeg deze repository toe met categorie "Integration"
5. Zoek naar "Zehnder ComfoAir Q" en installeer
6. Herstart Home Assistant

### Handmatige installatie

1. Download deze repository
2. Kopieer de map `comfoconnect` naar je `custom_components` map in je Home Assistant configuratiemap
3. Herstart Home Assistant

## Configuratie

1. Ga naar **Instellingen** → **Apparaten & Services**
2. Klik op **+ Integratie toevoegen**
3. Zoek naar "Zehnder ComfoAir Q"
4. Voer de volgende gegevens in:
   - **IP-adres**: Het IP-adres van je ComfoConnect LAN C bridge
   - **Naam**: Een vriendelijke naam voor je apparaat (standaard: ComfoAirQ)
   - **Token**: Een unieke 32-karakter hexadecimale string (standaard: 00000000000000000000000000000001)
   - **User Agent**: Naam van de client (standaard: Home Assistant)
   - **PIN**: De PIN-code indien ingesteld op je bridge (standaard: 0)

## Beschikbare entiteiten

Na configuratie worden de volgende entiteiten automatisch toegevoegd:

### Fan
- ComfoAir Q ventilator met snelheidsregeling en auto-modus

### Sensoren
- Inside temperature
- Inside humidity
- Current RMOT
- Outside temperature
- Outside humidity
- Supply temperature
- Supply humidity
- Supply fan speed
- Supply fan duty
- Exhaust fan speed
- Exhaust fan duty
- Exhaust temperature
- Exhaust humidity
- Supply airflow
- Exhaust airflow
- Bypass state
- Days to replace filter
- Power usage
- Energy total
- Preheater power usage
- Preheater energy total

## Apparaatinformatie

Alle entiteiten worden gegroepeerd onder één apparaat met de volgende informatie:
- **Fabrikant**: Zehnder
- **Model**: ComfoAir Q
- **Naam**: De door jou gekozen naam

## Ondersteuning

Voor problemen, vragen of suggesties, open een issue op GitHub.

## Licentie

Deze component is gelicenseerd onder de Apache License 2.0, dezelfde licentie als Home Assistant Core.

De originele code is ontwikkeld door Michiel Arnauts en het Home Assistant Core team. Deze custom variant bevat aanpassingen om device support en een moderne configuratie flow toe te voegen.

Zie het [LICENSE](LICENSE) bestand voor meer informatie.
