## Zehnder ComfoAir Q Custom Component

This custom component provides enhanced support for Zehnder ComfoAir Q350/450/600 ventilation systems in Home Assistant.

### Advantages over the standard integration

- **Device Support**: All entities are linked to a single device
- **UI Configuration**: No YAML configuration required
- **All Sensors**: Automatically includes all 20+ sensors

### Requirements

- ComfoConnect LAN C bridge
- IP address of your bridge
- Optional: 32-character token (default is used if not set)

### Configuration

After installation:
1. Go to **Settings** → **Devices & Services**
2. Click on **+ Add Integration**
3. Search for "Zehnder ComfoAir Q"
4. Enter the IP address of your bridge
5. Done!

### Available Entities

#### Fan
- Fan control with speed settings
- Auto mode support

#### Sensors (automatically added)
- Temperatures (inside, outside, supply, exhaust)
- Humidity (inside, outside, supply, exhaust)
- Fan speeds and duty cycles
- Airflows
- Bypass status
- Filter maintenance (days to replacement)
- Energy consumption

### Credits

Based on the official Home Assistant ComfoConnect integration by Michiel Arnauts.
