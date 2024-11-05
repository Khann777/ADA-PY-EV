import requests
from bs4 import BeautifulSoup as BS
import csv
from multiprocessing import Pool
from time import time

URL = 'https://www.mashina.kg/search/all/'

def get_html(url: str, page: int = 1) -> str:
    response = requests.get(url, params={'page': page})
    if response.status_code == 200:
        return response.text
    raise Exception('Произошла ошибка при загрузке страницы!')

def get_cars(html: str) -> list:
    soup = BS(html, 'lxml')
    return soup.find_all('div', class_='list-item list-label')

def parse_cars(cars: list) -> list:
    data = []
    for car in cars:
        car = car.find('a')
        try:
            title = car.find('div', class_='block title').find('h2', class_='name').text.strip() if car.find('div', class_='block title') else ''
            images = [img.get('src') for img in car.find('div', class_='thumb-item-carousel brazzers-daddy').find_all('div', class_='image-wrap')] if car.find('div', class_='thumb-item-carousel brazzers-daddy') else []
            price = car.find('div', class_='block price').find('p').text.strip() if car.find('div', class_='block price') else ''
            link = f'{URL}{car.get("href")}' if car.get('href') else ''
            description = (
                f"{car.find('div', class_='block info-wrapper item-info-wrapper').find('p', class_='year-miles').text.strip() if car.find('div', class_='block info-wrapper item-info-wrapper') else ''}\n"
                f"{car.find('div', class_='block info-wrapper item-info-wrapper').find('p', class_='body-type').text.strip() if car.find('div', class_='block info-wrapper item-info-wrapper') else ''}\n"
                f"{car.find('div', class_='block info-wrapper item-info-wrapper').find('p', class_='volume').text.strip() if car.find('div', class_='block info-wrapper item-info-wrapper') else ''}"
            )

            # Добавляем данные в список
            data.append({
                'title': title,
                'image': ', '.join(images),
                'price': price,
                'description': description,
                'link': link
            })
        except Exception as e:
            print(f"Ошибка при парсинге данных: {e}")
            continue
    return data

def write_csv(data):
    with open('cars.csv', 'a', newline='') as csv_file:
        fieldnames = ['title', 'price', 'image', 'description', 'link']
        writer = csv.DictWriter(csv_file, delimiter='|', fieldnames=fieldnames)
        writer.writeheader()  # Записываем заголовки только один раз
        writer.writerows(data)

def get_last_page(url: str) -> int:
    html = get_html(url)
    soup = BS(html, 'lxml')
    pagination = soup.find('nav').find('ul', class_='pagination')
    
    if pagination:
        pages = pagination.find_all('li')
        last_page = 1
        for page in pages:
            if 'data-page' in page.a.attrs:
                last_page = int(page.a.get('data-page'))
        return last_page
    else:
        print("Не удалось найти пагинацию.")
        return 1

def benchmark(func):
    def wrapper(*a, **k):
        start = time()
        result = func(*a, **k)
        finish = time()
        total_time = finish - start
        print(f'Время выполнения функции: {total_time:.2f} секунд')
        return result
    return wrapper

@benchmark
def main(url: str) -> None:
    last_page = get_last_page(url)
    print(f"Количество страниц: {last_page}")
    all_data = []
    
    for page in range(1, last_page + 1):
        html = get_html(url, page)
        cars = get_cars(html)
        all_data.extend(parse_cars(cars))
        print(f'Спарсил страницу - {page}')
    
    # Записываем все данные после завершения парсинга
    write_csv(all_data)

# main(URL)

def process_page(page: int) -> list:
    html = get_html(URL, page)
    cars = get_cars(html)
    return parse_cars(cars)

# Основная функция для запуска с использованием multiprocessing.Pool
@benchmark
def main():
    start_time = time()
    last_page = get_last_page(URL)
    
    with Pool(processes=8) as pool:  # Указываем количество процессов (8 процессов)
        results = pool.map(process_page, range(1, last_page + 1))  # Обрабатываем страницы параллельно
    
    # Объединяем результаты всех страниц и записываем в CSV один раз
    all_data = [car for result in results for car in result]
    write_csv(all_data)
    
    print(f"Время выполнения: {time() - start_time:.2f} секунд")

if __name__ == '__main__':
    main()
