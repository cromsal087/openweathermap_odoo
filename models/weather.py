from odoo import models, fields
from odoo.exceptions import UserError
import requests
import logging

# Configurar el logger
_logger = logging.getLogger(__name__)
class WeatherInfo(models.Model):
    _name = 'weather.info'
    _description = 'Weather Information'
    _rec_name = 'city'
    city = fields.Char(string='City', required=True)
    api_key = fields.Char(string='API Key', required=True)
    temperature = fields.Float(string='Temperature', readonly=True)
    description = fields.Char(string='Description', readonly=True)

    def get_weather_data(self):
        # Construir la URL para hacer la solicitud a la API de OpenWeatherMap
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}
        &appid={self.api_key}&units=metric&lang=es"
        try:
            # Hacer la solicitud GET a la API
            response = requests.get(api_url)
            # Comprobar si la solicitud fue exitosa
            if response.status_code == 200:
                data = response.json()
                # Actualizar los campos del registro con los datos obtenidos de la API
                self.temperature = data['main']['temp']
                self.description = data['weather'][0]['description']
            else:
            # Si hay un error con la solicitud, lanzar una excepción
                raise UserError("Error al obtener los datos del clima. Código de respuesta: %d"
                % response.status_code)
                except requests.exceptions.RequestException as e:
                # Manejar las excepciones de la solicitud HTTP
                _logger.error("Error al intentar obtener los datos del clima: %s", str(e))
                raise UserError(f"Hubo un error al conectarse a la API" )