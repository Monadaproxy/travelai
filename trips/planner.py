from travelai import settings
from mistralai import Mistral

def generate_itinerary(destination, dates, interests):
    api_key = settings.MISTRAL_API_KEY
    model = 'mistral-large-latest'
    client = Mistral(api_key=api_key)

    prompt = f"""
    Создай подробный маршрут по городу {destination} на {dates}. 
    Интересы: {interests}. Включи:
    1. Места с описанием (не более 3 в день)
    2. Время посещения
    3. Советы по транспорту
    Опиши подробно каждое место
    Формат вывода: JSON с временными слотами и координатами.
    Верни только JSON строку.
    """

    try:
        response = client.chat.complete(
            model = model,
            messages = [{'role': 'user', 'content': prompt}]
        )
        return response.choices[0].message.content[7:-3]

    except Exception as e:
        return {'error': str(e)}

