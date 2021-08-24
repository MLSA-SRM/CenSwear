# CenSwear <img src="https://i.ibb.co/LpTqC8H/censwear.png" align="right">
CenSwear is a Python based profanity filter API. CenSwear is a simple, free, and reliable language understanding API designed to recognize and remove profanity, obscenity, and other unwanted text. It’s a technology you can swear by!<br><br>
Check out the live site - [**CenSwear**](https://censwear.msclubsrm.in/)

![](https://img.shields.io/github/forks/MLSA-SRM/CenSwear?color=green&style=for-the-badge)
![](https://img.shields.io/github/stars/MLSA-SRM/CenSwear?color=silver&style=for-the-badge)
![](https://img.shields.io/github/license/MLSA-SRM/CenSwear?color=yellow&style=for-the-badge)

## How it works
<img src="https://i.imgur.com/YYiEfI4.gif" align="center">

## How to use
* Python <br>
  <img src="https://i.imgur.com/r8Pmn50.png" width="700">

## Built With:
| Software/ Language | Version |
|----------|---------|
| Python | 3.8 |
| Flask | 2.0.0 |

## Features:
* ### Profanity detection and filtering from texts 
  * The API detects and censors swear words and profanities from chat and text messages based on an internal profanity list.

* ### Bilingual
  * We’ve designed CenSwear in a way that it detetcts profanities in both Hindi and English
  
* ### Real-time censoring of expletives
  * The web service also provides real-time redaction of swear words while emails and documents are being typed.
  
* ### Fast, accurate, reliable
  * CenSwear ensures that not one single offensive message slips through its filters, creating a safe and productive environment for the users.
  

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── requirements.txt   <- The requirements file for reproducing the environment
    │
    ├── test
    │  └── app_test.py     <- The python script for testing the app
    │
    ├── LICENSE
    │
    ├── Procfile           <- for heroku deployment
    │
    └── src
        ├── __init__.py 
        ├── app.py         <- Main python file containig the flask app
        ├── templates
        │   ├── base.html
        │   └── home.html
        └── static
            ├── assets     <- contains svg images and backgrounds 
            └── css        <- The css files for the web app



## How to get started
To use this project, follow these steps:

* Make a `.env` file having same structure as `.env.sample` inside the `src` folder
* Fill in the `FILTER_WORDLIST_URL` and `CLEAN_WORDLIST_URL` variables
* Clone this repository 
```
git clone https://github.com/MLSA-SRM/CenSwear.git
```
* Install dependencies 
```
pip install -r requirements.txt
```
* Go to the app root folder 
```
cd src
```
* Run the App  `python app.py` or `flask run`

## Contributors:
<table>
<td><p align="center">    Ayush Mishra  <br><br><img src = "https://avatars.githubusercontent.com/u/36323763?v=4"  height="120" alt="Logeek"></p><p align="center"><a href = "https://github.com/sudo-logic"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="github-logo"/></a><a href = "https://www.linkedin.com/in/ayush-mishra-srm/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="linkedin-logo" /></a></p></td>
  
<td><p align="center"> Shreyas <br><br><img src = "https://avatars.githubusercontent.com/u/81923486?v=4"  height="120" alt="Shreyas"></p><p align="center"><a href = "https://github.com/ShreyasDatta"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="github-logo"/></a><a href = "https://www.linkedin.com/in/shreyas-datta-32bb041a1/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="linkedin-logo" /></a></p></td>
  
<td><p align="center">Manu<br> <br><img src = "https://avatars.githubusercontent.com/u/46190721?v=4"  height="120" alt="Manu"></p><p align="center"><a href = "https://github.com/manushyaaa"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="github-logo"/></a><a href = "https://www.linkedin.com/in/manu-sunil-8356b51b9/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="linkedin-logo" /></a></p></td>
  
<td><p align="center">Pallavi Pandey<br> <br><img src = "https://media-exp1.licdn.com/dms/image/C4D03AQGVXvb8JHZUqw/profile-displayphoto-shrink_400_400/0/1602692630506?e=1632960000&v=beta&t=5XEL0YSmOvE0o9AzHNIGi-bs8kY9Fj7yNqV91I_sQ1E"  height="120" alt="pallavi-pandey"></p><p align="center"><a href = "https://www.linkedin.com/in/pallavi-pandey-27b4b71b8/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="linkedin-logo" /></a></p></td>
  
<td><p align="center">Priyanshi David<br> <br><img src = "https://media-exp1.licdn.com/dms/image/C5603AQE0xGrfOyBVFA/profile-displayphoto-shrink_400_400/0/1606122219889?e=1632960000&v=beta&t=_CwiZdOeFQtEkOblJz9g8-4BLsLrIfppM-QJb5rdxyU"  height="120" alt="priyanshi-david"></p><p align="center"><a href = "https://www.linkedin.com/in/priyanshi-david-28910b200/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="linkedin-logo" /></a></p></td>
  
<td><p align="center">     Sahil<br> <br><img src = "https://avatars.githubusercontent.com/u/68604369?v=4"  height="120" alt="Sahil"></p><p align="center"><a href = "https://github.com/sahiljena"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="github-logo"/></a><a href = "https://www.linkedin.com/in/sahil-jena/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="linkedin-logo" /></a></p></td>
  </table>
