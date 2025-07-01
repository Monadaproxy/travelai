from travelai import settings
from mistralai import Mistral

def generate_itinerary(destination, dates, interests):
    model = 'mistral-large-latest'
    client = Mistral(api_key=settings.MISTRAL_API_KEY)

    prompt = f"""
    Создай подробный маршрут по городу {destination} на {dates}. 
    Интересы: {interests}. Включи:
    1. Места с описанием (не более 3 в день)
    2. Время посещения
    3. Советы по транспорту
    4. Ссылку на отель, где можно переночевать
    Опиши подробно каждое место
    Формат вывода: JSON с временными слотами и координатами.
    Верни только JSON строку.
    """ + 'Вот пример названия переменных: {"2025-11-06": {"morning": {"time": "10:00 - 12:00", "place": "Театр Шатле", "transport": "Метро: линия 1, станция Châtelet", "coordinates": {"latitude": 48.861, "longitude": 2.3385}, "description": "Исторический театр, предлагающий разнообразные постановки, от классических пьес до современных произведений."}, "afternoon": {"time": "14:00 - 16:00", "place": "Лувр", "transport": "Метро: линия 1, станция Palais Royal Musée du Louvre", "coordinates": {"latitude": 48.8606, "longitude": 2.3376}, "description": "Один из самых известных музеев мира, где можно увидеть такие шедевры, как Мона Лиза и Ника Самофракийская. Музей охватывает несколько тысячелетий истории и искусства."}, "evening": {"time": "20:00 - 22:00", "place": "Музей Орсе", "transport": "Метро: линия 12, станция Solférino", "coordinates": {"latitude": 48.8597, "longitude": 2.3262}, "description": "Музей, посвященный искусству XIX века, включая импрессионизм и постимпрессионизм. Здесь можно увидеть работы таких художников, как Ван Гог, Моне и Дега."}}, "2025-11-07": {"morning": {"time": "10:00 - 12:00", "place": "Театр де ля Вилль", "transport": "Метро: линия 11, станция Rambuteau", "coordinates": {"latitude": 48.8592, "longitude": 2.3618}, "description": "Театр, известный своими современными постановками и инновационными сценическими решениями."}, "afternoon": {"time": "14:00 - 16:00", "place": "Центр Помпиду", "transport": "Метро: линия 11, станция Rambuteau", "coordinates": {"latitude": 48.8609, "longitude": 2.3522}, "description": "Музей современного искусства с уникальной архитектурой. Здесь можно увидеть работы таких художников, как Пикассо и Кандинский."}, "evening": {"time": "20:00 - 22:00", "place": "Кинотеатр «Гран-Рекс»", "transport": "Метро: линия 8, станция Grand Boulevards", "coordinates": {"latitude": 48.8742, "longitude": 2.3397}, "description": "Один из самых известных кинотеатров Парижа, известный своей великолепной архитектурой и показом крупных премьер."}}, "2025-11-08": {"morning": {"time": "10:00 - 12:00", "place": "Театр Одеон", "transport": "Метро: линия 4, станция Odéon", "coordinates": {"latitude": 48.8491, "longitude": 2.34}, "description": "Один из старейших театров Парижа, известный своими классическими постановками и великолепной архитектурой."}, "afternoon": {"time": "14:00 - 16:00", "place": "Музей Родена", "transport": "Метро: линия 13, станция Varenne", "coordinates": {"latitude": 48.8479, "longitude": 2.326}, "description": "Музей, посвященный работам великого скульптора Огюста Родена. Здесь можно увидеть такие знаменитые произведения, как «Мыслитель» и «Поцелуй»."}, "evening": {"time": "20:00 - 22:00", "place": "Кинотеатр «Le Champo»", "transport": "Метро: линия 4, станция Saint-Michel", "coordinates": {"latitude": 48.8473, "longitude": 2.3371}, "description": "Кинотеатр, известный показом артхаусных и независимых фильмов. Отличное место для любителей кино."}}, "2025-11-09": {"morning": {"time": "10:00 - 12:00", "place": "Театр де Шатле", "transport": "Метро: линия 1, станция Châtelet", "coordinates": {"latitude": 48.8555, "longitude": 2.3505}, "description": "Мультидисциплинарный театр, предлагающий широкий спектр постановок, от танцевальных шоу до музыкальных концертов."}, "afternoon": {"time": "14:00 - 16:00", "place": "Музей Пикассо", "transport": "Метро: линия 1, станция Saint-Paul", "coordinates": {"latitude": 48.8562, "longitude": 2.3634}, "description": "Музей, посвященный работам Пабло Пикассо. Здесь можно увидеть широкий спектр его творчества, включая картины, скульптуры и керамику."}, "evening": {"time": "20:00 - 22:00", "place": "Кинотеатр «Le Grand Action»", "transport": "Метро: линия 7, станция Maubert - Mutualité", "coordinates": {"latitude": 48.8479, "longitude": 2.3506}, "description": "Кинотеатр, известный показом классических и ретро фильмов. Отличное место для любителей киноклассики."}}, "hotel": "http://..."}'


    try:
        response = client.chat.complete(
            model = model,
            messages = [{'role': 'user', 'content': prompt}]
        )
        return response.choices[0].message.content[7:-3]

    except Exception as e:
        return {'error': str(e)}

