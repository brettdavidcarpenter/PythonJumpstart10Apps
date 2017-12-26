
import requests
import bs4
import collections


weatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')
zip = ''

def main():
    print_header()

    code = input('What zipcode do you want to lookup? ')

    #get html from web
    html = get_html_from_web(code)
    report = get_weather_from_html(html)

    print ('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond,
    ))

    get_weather_from_html(html)

    #parse the html
    #Display the forecast


def print_header():
    print('-----------------------')
    print('      WEATHER APP')
    print('-----------------------')


def get_html_from_web (zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    #print (response.status_code)
    #print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    #cityCss ='.region-content-header h1'
    #weatherScaleCss = '.wu-unit-temperature.wu-lable'
    #weatherTempCass = '.wu-unit-temperature.wu-value'
    #weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_ ='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    #print(condition, temp, scale, loc)
    #return (condition, temp, scale, loc)
    report = weatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_and_state_from_location(loc : str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text : str):
    if not text:
        return text
    text = text.strip()
    return text

def parse_html():
    pass


def display_forecast():
    pass



if __name__== '__main__':
    main()