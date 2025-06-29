from openai import OpenAI
import json
import httpx
from travelai import settings

def generate_itinerary(destination, dates, interests):
    proxy_client = httpx.Client(
        proxies="http://43.199.163.10:3128",
        timeout=30.0
    )

    client = OpenAI(api_key=settings.OPENAI_API_KEY, http_client=proxy_client)

    prompt = f"""
    Создай маршрут для {destination} на {dates}. 
    Интересы: {interests}. Включи:
    1. Места с описанием (не более 3 в день)
    2. Время посещения
    3. Советы по транспорту
    Формат: JSON с временными слотами и координатами.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            timeout=30.0
        )
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        return {'error': str(e)}