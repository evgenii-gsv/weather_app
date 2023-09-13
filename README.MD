Weather console application
==============================

What Is This?
-------------

This is a simple Python application for showing weather in your console. It is using Nominatim software to get the precise coordinates of the location and OpenWeather API to receive information about weather. It prints in console only necessary information: location, temperature, desciption of weather, sunrise and sunset time.   


How To Use This
---------------

1. Clone this repository:
```bash
git clone https://github.com/evgenii-gsv/weather_app.git
```
2. You need an API key of OpenWeather to use this app. You can obtain it by signing up [here](https://home.openweathermap.org/users/sign_up).
3. In the root folder open the file `.env.example` and paste you OpenWeather API key there. Change other settings if you need to. Then you need to save this file as `.env`.
4. Create virtual envirenment by running the following commands in the root directory of the project and activate it. 

```bash
python3 -m venv env
source env/bin/activate
```
5. Install dependencies by running `pip install -r requirements.txt`.
6. To run the program use `python3 weather "<address>"` or `python3 weather` to see the weather in default location. If your location consists of one word without spaces, you can write it without quotation marks. If it contains spaces, you need to use quotation marks.
7. OPTIONAL. On Linux you can add a link to a folder in your $PATH variable, this way you can use the program from anywhere just by typing `weather`. This way you also don't need to activate virtual environment in the future. To do so you need to run this command from the root folder of the project:
```bash
sudo ln -s $(pwd)/weather /usr/local/bin/
```

