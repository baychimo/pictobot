[![Screenshots of a conversation with the Pictobot](https://raw.githubusercontent.com/baychimo/pictobot/master/screenshots/sample_pictograms_sm.png "Screenshots of a conversation with the Pictobot")](https://raw.githubusercontent.com/baychimo/pictobot/master/screenshots/sample_pictograms_lg.png)

# Pictobot

A chatbot to use as a basic universal translator. If you can't say it, show it!

[![Screenshots of a conversation with the Pictobot](https://raw.githubusercontent.com/baychimo/pictobot/master/screenshots/screenshots_sm.png "Screenshots of a conversation with the Pictobot")](https://raw.githubusercontent.com/baychimo/pictobot/master/screenshots/screenshots_lg.png)

This bot is shown here as an example of a telegram bot written in python, which might be helpful to some. It is not a framework or a template, in my opinion. But it was enough IMHO to participate in the [Telegram BotPrize](https://telegram.org/blog/botprize), because I believe in the usefulness of this simple idea.
The contest was a good opportunity to learn about chatbots and pictograms.

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [Running the bot](#running-the-bot)
- [Running the tests](#running-the-tests)
- [Deployment](#deployment)
- [Built With](#built-with)
- [Docs](#docs)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for pointers on how to deploy the project on a live system.

### Prerequisites

If you want to follow these instructions to run the chatbot on your machine, you need:
- [python](https://www.python.org/) 3.6 or higher.
- [a bot TOKEN from Telegram](https://core.telegram.org/bots#6-botfather "Ask BotFather"). You should also toggle inline mode for your bot (`/setinline` command within BotFather). I recommend creating two bots if you want to get serious: one for dev/test and the other one for production.
- If you wish to run the integration tests, you'll also need to get API keys from Telegram: [follow instructions here](https://telethon.readthedocs.io/en/latest/extra/basic/creating-a-client.html).

These instructions are for running in dev/test mode on MacOS and Linux.

Copy this project's files where you want them:

```
$ cd /to/where/you/want/the/bot/to/live
$ git clone https://github.com/baychimo/pictobot
```
If you don't have [git](https://git-scm.com/downloads) installed, you can download the files by clicking the green "Clone or download" button at the top of the page.

### Installing

Create a virtual environment on your machine with:

```
$ python3 -m venv .virtualenvs/pictobot
```

Activate the environment and install the needed python packages:

```
$ source ~/.virtualenvs/pictobot/bin/activate && cd /to/where/you/want/the/bot/to/live
(pictobot)$ pip install --upgrade pip setuptools
(pictobot)$ pip install -r requirements.txt
```

Replace the fake `TOKEN` in the file `settings/local_sample.py` by yours and rename that file to `local.py`. If you wish to run the integration tests, also replace the values of `api_id` and `api_hash` with yours.

## Running the bot

If you followed the above instructions, to run the bot locally you just need to:

```
(pictobot)$ python pictobot/core.py
``` 

Now go to your telegram app (on your smartphone/desktop/browser) and contact your bot by its name (the one you chose earlier): `@YourBot`.

## Running the tests

If you wish to run the automated tests for this project, just run these commands from the root of the project.

For unit tests:

```
(pictobot)$ pytest -v --durations=0 --hypothesis-show-statistics tests/test_unit.py
```

For integration tests:

```
(pictobot)$ pytest -v --durations=0 --hypothesis-show-statistics tests/test_integration.py
```

The integration tests require patience. They are done through a [userbot](https://github.com/LonamiWebs/Telethon), and to avoid being (rightfully) blacklisted or rate-limited by Telegram, there is a 3 second wait between each test.

## Deployment

If you want to run it on a server, I can write instructions. [You just need to ask](https://github.com/baychimo/pictobot/issues/new).
For now, if you already have python experience, you should read the last lines of `core.py` and check the settings in `settings/production_sample.py` to get you started. I used nginx/uwsgi/letsencrypt/supervisor, but other combos are possible (check out [python-telegram-bot docs on the subject](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks)).
If you are in a hurry, start by the [great wiki of the Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki) framework.

## Built With

- [Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot) - The excellent Telegram Bot framework, making it very easy to get started with Telegram. Their docs are good and they are very helpful on their Telegram group too. Highly recommended!
- [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) - "Fuzzy string matching like a boss". That says it all.
- [The Noun Project](https://thenounproject.com/) - All the images used by the bot were downloaded from the noun project website before being adapted into pictograms with [inkscape](https://inkscape.org/), the credits are listed below.

## Docs

The docstring generated docs are in the gh-pages branch. They are published here: [baychimo.github.io/pictobot](https://baychimo.github.io/pictobot/)

## Contributing

I don't intend to maintain this project unless I have some new ideas that would make the process fun. But if you have any questions, need further instructions for your platform, feel free to [open an issue](https://github.com/baychimo/pictobot/issues/new). And feel free to fork it of course! That's why I put it here for.

Here are some ideas for improvments:
- Store data in a DB instead of dicts. To make things practical this should be accompanied by some UI to update the database and add images: a micro webapp?
- The bot is translatable, and translated in french for now. But there needs to be a way for users to switch languages which means storing at least minimal user data somewhere.
- Find a way to automate the creation and tagging of pictograms. Maybe a toolchain involving a [GAN](https://en.wikipedia.org/wiki/Generative_adversarial_network) and [imagemagick](https://www.imagemagick.org/)?

Have fun!

## Author

**Jonathan Guitton** - [Baychimo](https://github.com/baychimo).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Inspiration
    - Star Trek's universal translator: we have to start somewhere, right?
    - My own experience as a travelling introvert. Most people don't want to mimic/gesticulate that they need toilet paper. Or so I thought :-)
- Beautiful logo made by the great [Sebastien Lasserre](https://seblasserre.blogspot.com/).
- All images used by the pictobot are licensed under Public Domain, except for the following which are licensed under Creative Commons / Attribution 3.0 United States [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/):
    - By [Arthur Shlain](https://thenounproject.com/ArtZ91/):
        - [Shopping Cart](https://thenounproject.com/icon/139181/ "link to original image") | Retrieved on 2016-07-13.
        - [Toilet Paper](https://thenounproject.com/icon/79500/ "link to original image") | Retrieved on 2016-07-13.
        - [Band Aid](https://thenounproject.com/icon/79529/ "link to original image") | Retrieved on 2016-07-13.
        - [Toilet](https://thenounproject.com/icon/124048/ "link to original image") | Retrieved on 2016-07-13.
        - [Wrench](https://thenounproject.com/icon/144983/ "link to original image") | Retrieved on 2016-07-13.
    - By [Mikhail Iskandarov](https://thenounproject.com/iskmisha/): [Toilet Paper](https://thenounproject.com/icon/110942/ "link to original image") | Retrieved on 2016-07-13.
    - By [Vicons Design](https://thenounproject.com/ViconsDesign):
        - [ATM Withdrawal](https://thenounproject.com/icon/370580/ "link to original image") | Retrieved on 2016-07-13.
        - [Bank](https://thenounproject.com/icon/370631/ "link to original image") | Retrieved on 2016-07-13.
    - By [Greg Beck](https://thenounproject.com/gbeck419/): [Health Foods](https://thenounproject.com/icon/105409/ "link to original image") | Retrieved on 2016-07-13.
    - By [Martin Lebreton](https://thenounproject.com/Martin%20LEBRETON/): [Grocery Basket](https://thenounproject.com/icon/176841/ "link to original image") | Retrieved on 2016-07-13.
    - By [MD Delwar Hossain](https://thenounproject.com/delwar_ctgbd/):
        - [Hammer](https://thenounproject.com/icon/539512/ "link to original image") | Retrieved on 2016-07-16.
        - [Hammer](https://thenounproject.com/icon/539514/ "link to original image") | Retrieved on 2016-07-16.
        - [Screwdriver](https://thenounproject.com/icon/539515/ "link to original image") | Retrieved on 2016-07-16.
    - By [Ricardo Moreira](https://thenounproject.com/skatakila/): [Tools](https://thenounproject.com/icon/12635/ "link to original image") | Retrieved on 2016-07-16.
    - By [useiconic.com](https://thenounproject.com/useiconic.com/):
        - [Screwdriver](https://thenounproject.com/icon/45421/ "link to original image") | Retrieved on 2016-07-16.
        - [Pencil](https://thenounproject.com/icon/45487/ "link to original image") | Retrieved on 2016-07-16.
    - By [Stanislav Levin](https://thenounproject.com/brandcut/): [Umbrella](https://thenounproject.com/icon/173087/ "link to original image") | Retrieved on 2016-07-23.
    - By [Edward Boatman](https://thenounproject.com/edward/): [Umbrella](https://thenounproject.com/icon/142/ "link to original image") | Retrieved on 2016-07-23.
    - By [Eric Milet](https://thenounproject.com/ericmilet/): [Photographer](https://thenounproject.com/icon/17351/ "link to original image") | Retrieved on 2016-07-23.
    - By [Eva Verbeek](https://thenounproject.com/evaverbeek/): [Charger](https://thenounproject.com/icon/137625/ "link to original image") | Retrieved on 2016-07-23.
    - By [Anbileru Adaleru](https://thenounproject.com/pronoun/): [Charger](https://thenounproject.com/icon/101470/ "link to original image") | Retrieved on 2016-07-23.
    - By [Gregor Črešnar](https://thenounproject.com/grega.cresnar/): [Charger](https://thenounproject.com/icon/547534/ "link to original image") | Retrieved on 2016-07-23.
    - By [Clair Jones](https://thenounproject.com/hivernoir/): [Adapter](https://thenounproject.com/icon/36303/ "link to original image") | Retrieved on 2016-07-23.
    - By [Ed Harrison](https://thenounproject.com/edharrison89/): [Bunk Beds](https://thenounproject.com/icon/187619/ "link to original image") | Retrieved on 2016-07-23.
    - By [Krisada](https://thenounproject.com/Krisada/): [Museum](https://thenounproject.com/icon/78475/ "link to original image") | Retrieved on 2016-07-23.
    - By [Jakob Vogel](https://thenounproject.com/jakobvogel/): [Parachute](https://thenounproject.com/icon/28223/ "link to original image") | Retrieved on 2016-07-23.
    - By [Juan Pablo Bravo](https://thenounproject.com/bravo/): [Skydiving](https://thenounproject.com/icon/26955/ "link to original image") | Retrieved on 2016-07-23.
    - By [Creative Stall](https://thenounproject.com/creativestall/): [Waiter](https://thenounproject.com/icon/130519/ "link to original image") | Retrieved on 2016-07-23.
    - By [Pieter J. Smits](https://thenounproject.com/pjsmits/): [Lake](https://thenounproject.com/icon/16107/ "link to original image") | Retrieved on 2016-07-23.
    - By [Icon Island](https://thenounproject.com/iconisland/): [Sunglasses](https://thenounproject.com/icon/326819/ "link to original image") | Retrieved on 2016-07-24.
