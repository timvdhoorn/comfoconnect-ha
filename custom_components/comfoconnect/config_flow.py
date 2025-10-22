"""Config flow for Zehnder ComfoAir Q integration."""

from __future__ import annotations

import logging
from typing import Any

from pycomfoconnect import Bridge
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PIN, CONF_TOKEN
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError

from . import CONF_USER_AGENT, DEFAULT_NAME, DEFAULT_PIN, DEFAULT_TOKEN, DEFAULT_USER_AGENT
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): str,
        vol.Optional(CONF_TOKEN, default=DEFAULT_TOKEN): str,
        vol.Optional(CONF_USER_AGENT, default=DEFAULT_USER_AGENT): str,
        vol.Optional(CONF_PIN, default=DEFAULT_PIN): int,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    host = data[CONF_HOST]

    # Validate token length
    token = data.get(CONF_TOKEN, DEFAULT_TOKEN)
    if len(token) != 32:
        raise InvalidToken

    # Try to discover the bridge
    bridges = await hass.async_add_executor_job(Bridge.discover, host)
    if not bridges:
        raise CannotConnect

    bridge = bridges[0]
    unique_id = bridge.uuid.hex()

    # Return info that you want to store in the config entry.
    return {
        "title": data.get(CONF_NAME, DEFAULT_NAME),
        "unique_id": unique_id,
    }


class ComfoConnectConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Zehnder ComfoAir Q."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidToken:
                errors["token"] = "invalid_token"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                # Set unique ID to prevent duplicate entries
                await self.async_set_unique_id(info["unique_id"])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(title=info["title"], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA, errors=errors
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidToken(HomeAssistantError):
    """Error to indicate the token is invalid."""
