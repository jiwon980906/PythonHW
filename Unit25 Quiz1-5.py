terrestrial_planet = {
    'Earth': {
        'physical_characteristics': {
            'mean_radius': 6371.0,
            'mass': 5.97219E+24
        },
        'orbital_characteristics': {
            'orbital_period': 365.25641,
            'satellites': 1
        }
    },
    'Mars': {
        'physical_characteristics': {
            'mean_radius': 3389.5,
            'mass': 6.4185E+23
        },
        'orbital_characteristics': {
            'orbital_period': 686.9600,
            'satellites': 2
        }
    }
}
print(terrestrial_planet['Earth']['orbital_characteristics']['satellites'])