import requests # this library is used to make HTTP requests, like GET or POST.
from bs4 import BeautifulSoup # used to parse HTML,XML documents and navigating through parse tress.

# Funciton get_html takes a URL and sends a request to the URL to get the webpage, It then returns the HTML of the webpage as a string.
def get_html(url):
    # headers is a dictionary, which contains HTTP requests that provides info about HTTP client to server, this header is sent along the HTTP request.
   headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en-US,en;q=0.5',
   }
   response = requests.get(url, headers=headers)
   return response.text




# main function to get the station code from mapsofindia.com

def get_station_code (station_name):
    url = f"https://www.mapsofindia.com/railways/station-code/{station_name}.html"
    
    # getting the html data from station page.
    html_data = get_html(url)
    
    soup = BeautifulSoup(html_data,'html.parser')
    # extract station code from html data
    station_code = soup.find("table", class_="extrtable").find_all('b')[-1].get_text()
    return station_code


    
    

    
    
    
