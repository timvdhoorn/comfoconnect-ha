"""Support to control a Zehnder ComfoAir Q350/450/600 ventilation unit."""

from __future__ import annotations

import logging
from typing import Any

from pycomfoconnect import Bridge, ComfoConnect

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_PIN,
    CONF_TOKEN,
    EVENT_HOMEASSISTANT_STOP,
    Platform,
)
from homeassistant.core import Event, HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.dispatcher import dispatcher_send

_LOGGER = logging.getLogger(__name__)

DOMAIN = "comfoconnect"

SIGNAL_COMFOCONNECT_UPDATE_RECEIVED = "comfoconnect_update_received_{}"

CONF_USER_AGENT = "user_agent"

DEFAULT_NAME = "ComfoAirQ"
DEFAULT_PIN = 0
DEFAULT_TOKEN = "00000000000000000000000000000001"
DEFAULT_USER_AGENT = "Home Assistant"

PLATFORMS = [Platform.FAN, Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up ComfoConnect from a config entry."""
    host = entry.data[CONF_HOST]
    name = entry.data.get(CONF_NAME, DEFAULT_NAME)
    token = entry.data.get(CONF_TOKEN, DEFAULT_TOKEN)
    user_agent = entry.data.get(CONF_USER_AGENT, DEFAULT_USER_AGENT)
    pin = entry.data.get(CONF_PIN, DEFAULT_PIN)

    # Run discovery on the configured ip
    bridges = await hass.async_add_executor_job(Bridge.discover, host)
    if not bridges:
        _LOGGER.error("Could not connect to ComfoConnect bridge on %s", host)
        return False
    bridge = bridges[0]
    _LOGGER.debug("Bridge found: %s (%s)", bridge.uuid.hex(), bridge.host)

    # Setup ComfoConnect Bridge
    ccb = ComfoConnectBridge(hass, bridge, name, token, user_agent, pin)
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = ccb

    # Register device
    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, ccb.unique_id)},
        manufacturer="Zehnder",
        model="ComfoAir Q",
        name=name,
        sw_version=None,
    )

    # Start connection with bridge
    await hass.async_add_executor_job(ccb.connect)

    # Schedule disconnect on shutdown
    async def _shutdown(_event: Event) -> None:
        await hass.async_add_executor_job(ccb.disconnect)

    entry.async_on_unload(hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, _shutdown))

    # Load platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        ccb: ComfoConnectBridge = hass.data[DOMAIN][entry.entry_id]
        await hass.async_add_executor_job(ccb.disconnect)
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class ComfoConnectBridge:
    """Representation of a ComfoConnect bridge."""

    def __init__(
        self,
        hass: HomeAssistant,
        bridge: Bridge,
        name: str,
        token: str,
        friendly_name: str,
        pin: int,
    ) -> None:
        """Initialize the ComfoConnect bridge."""
        self.name = name
        self.hass = hass
        self.unique_id = bridge.uuid.hex()

        self.comfoconnect = ComfoConnect(
            bridge=bridge,
            local_uuid=bytes.fromhex(token),
            local_devicename=friendly_name,
            pin=pin,
        )
        self.comfoconnect.callback_sensor = self.sensor_callback

    def connect(self) -> None:
        """Connect with the bridge."""
        _LOGGER.debug("Connecting with bridge")
        self.comfoconnect.connect(True)

    def disconnect(self) -> None:
        """Disconnect from the bridge."""
        _LOGGER.debug("Disconnecting from bridge")
        self.comfoconnect.disconnect()

    def sensor_callback(self, var: str, value: Any) -> None:
        """Notify listeners that we have received an update."""
        _LOGGER.debug("Received update for %s: %s", var, value)
        dispatcher_send(
            self.hass, SIGNAL_COMFOCONNECT_UPDATE_RECEIVED.format(var), value
        )
