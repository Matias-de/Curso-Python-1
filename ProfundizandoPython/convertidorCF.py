class ConvertidorTemperatura:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def convertirCelsiusAFahr(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura °C demasiado alta: {celsius}')

        return celsius * 9 / 5 + 32

    @classmethod
    def convertirFahrACelsius(cls, fahr):
        if fahr > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura °F demasiado alta: {fahr}')

        return (fahr - 32) * 5 / 9


if __name__ == '__main__':
    resultado = ConvertidorTemperatura.convertirCelsiusAFahr(15)
    print(f'15° a °F: {resultado:.2f}')
    resultado = ConvertidorTemperatura.convertirFahrACelsius(71)
    print(f'71°F a °C: {resultado:.2f}')
