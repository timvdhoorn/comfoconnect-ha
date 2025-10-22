# ComfoConnect Home Assistant Custom Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

This custom component for Home Assistant provides support for Zehnder ComfoAir Q350/450/600 ventilation systems via the ComfoConnect LAN C bridge.

## Credits

This integration is based on the [official Home Assistant ComfoConnect integration](https://www.home-assistant.io/integrations/comfoconnect) by [@michaelarnauts](https://github.com/michaelarnauts) and the Home Assistant Core team. The original code uses the [pycomfoconnect](https://github.com/michaelarnauts/comfoconnect) library.

**Original authors:**
- Michiel Arnauts ([@michaelarnauts](https://github.com/michaelarnauts))
- Home Assistant Core Team

**Custom component modifications:**
- Tim van der Hoorn ([@timvdhoorn](https://github.com/timvdhoorn))

## Key Changes

This version is a modified variant of the standard Home Assistant ComfoConnect integration with the following improvements:

- **Device support**: All entities are now linked to a single device in Home Assistant
- **Modern config flow**: Easy configuration via the UI instead of YAML
- **All sensors available**: All 20+ sensors are automatically added (no manual configuration needed)

## Installation

### Via HACS (recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click on the three dots (⋮) in the top right corner
4. Select "Custom repositories"
5. Add the following:
   - **Repository**: `https://github.com/timvdhoorn/comfoconnect-ha`
   - **Category**: `Integration`
6. Click "Add"
7. Click "Install" on the Zehnder ComfoAir Q card that appears
8. Restart Home Assistant

### Manual installation

1. Download this repository
2. Copy the `comfoconnect` folder to your `custom_components` folder in your Home Assistant configuration directory
3. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click on **+ Add Integration**
3. Search for "Zehnder ComfoAir Q"
4. Enter the following information:
   - **IP address**: The IP address of your ComfoConnect LAN C bridge
   - **Name**: A friendly name for your device (default: ComfoAirQ)
   - **Token**: A unique 32-character hexadecimal string (default: 00000000000000000000000000000001)
   - **User Agent**: Name of the client (default: Home Assistant)
   - **PIN**: The PIN code if set on your bridge (default: 0)

## Available Entities

After configuration, the following entities are automatically added:

### Fan
- ComfoAir Q fan with speed control and auto mode

### Sensors
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

## Device Information

All entities are grouped under one device with the following information:
- **Manufacturer**: Zehnder
- **Model**: ComfoAir Q
- **Name**: Your chosen name

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## License

This component is licensed under the Apache License 2.0, the same license as Home Assistant Core.

The original code was developed by Michiel Arnauts and the Home Assistant Core team. This custom variant includes modifications to add device support and a modern configuration flow.

See the [LICENSE](LICENSE) file for more information.
