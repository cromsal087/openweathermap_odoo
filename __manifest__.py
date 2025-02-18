{
    'name': 'OpenWeatherMap Integration',
    'version': '1.0',
    'summary': 'Integración con la API de OpenWeatherMap',
    'description': 'Obtención de datos meteorológicos en tiempo real.',
    'author': 'Cloe Romero Salguero',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv', 
    'views/weather_view.xml', 
    ], 
    'icon': '/openweathermap_odoo/static/description/icon57.png',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}