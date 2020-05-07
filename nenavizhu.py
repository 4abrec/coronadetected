import telebot

import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot('1073182631:AAFTL9J6n5Z1C7antJ8ocYhZ-0Bf4Ncc9tg')
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Russia', 'World')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("Back", "Info country")
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row("Back", "Refresh")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Этот бот показывает актуальную информацию по короновирусу',reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'russia':
        CoronaRussia = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        PageRussia = requests.get(CoronaRussia, headers=headers)
        SoupRussia = BeautifulSoup(PageRussia.content, 'html.parser')
        InfoRussia = SoupRussia.findAll("div", {"class": "cv-countdown__item-value"})
        data = SoupRussia.findAll("div", {"class": "cv-banner__description"})
        data = data[0].text
        infected_russia = InfoRussia[1].text
        last_day_russia = InfoRussia[2].text
        recovered_russia = InfoRussia[3].text
        death_russia = InfoRussia[4].text
        str_rus = data + '\n\n' + 'Заражено: ' + infected_russia + '\n' + 'За последние сутки: ' + last_day_russia + '\n' + 'Умерло: ' + death_russia + '\n' + 'Выздоровело: ' + recovered_russia
        bot.send_message(message.chat.id, str_rus, reply_markup=keyboard)
    elif message.text.lower() == 'world':
        CoronaWorld = 'https://www.worldometers.info/coronavirus/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        PageWorld = requests.get(CoronaWorld, headers=headers)
        SoupWorld = BeautifulSoup(PageWorld.content, 'html.parser')
        Info1World = SoupWorld.findAll("div", {"class": "maincounter-number"})
        Info2World = SoupWorld.findAll("div",
                                       {"style": "font-size:13px; color:#999; margin-top:5px; text-align:center"})
        data = Info2World[0].text
        data = data[14:39]
        infected_world = Info1World[0].text
        death_world = Info1World[1].text
        recovered_world = Info1World[2].text
        infected_world = infected_world.strip(" \t\n")
        death_world = death_world.strip(" \t\n")
        recovered_world = recovered_world.strip(" \t\n")
        str_world = data + '\n\n' + 'Infected: ' + infected_world + '\n' + 'Death: ' + death_world + '\n' + 'Recovered: ' + recovered_world
        bot.send_message(message.chat.id, str_world, reply_markup=keyboard1)
    elif message.text.lower() == 'back':
        bot.send_message(message.chat.id, "Выберите нужную кнопку", reply_markup=keyboard)
    elif message.text.lower() == 'info country':
        CoronaWorld = 'https://www.worldometers.info/coronavirus/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        PageWorld = requests.get(CoronaWorld, headers=headers)
        SoupWorld = BeautifulSoup(PageWorld.content, 'html.parser')
        InfoCountry = SoupWorld.findAll("td", {"style": "font-weight: bold; text-align:right"})
        infected_usa = InfoCountry[0].text
        infected_spain = InfoCountry[7].text
        infected_italy = InfoCountry[14].text
        infected_germany = InfoCountry[21].text
        infected_france = InfoCountry[28].text
        str_country = "Топ зараженных стран☣" + '\n' + "🇺🇸Америка: " + infected_usa + '\n' + "🇪🇸Испания: " + infected_spain + '\n' + "🇮🇹Италия: " + infected_italy + '\n' + "🇩🇪Германия: " + infected_germany + '\n' + "🇫🇷Франция: " + infected_france
        bot.send_message(message.chat.id, str_country, reply_markup=keyboard2)
    elif message.text.lower() == 'refresh':
        str_country = Country_stat()
        bot.send_message(message.chat.id, str_country, reply_markup=keyboard2)
    else:
        bot.send_message(message.chat.id, 'Такой команды нет, дружок', reply_markup=keyboard)


@bot.message_handler(content_types=['document and audio'])
def send_gif(message):
    bot.send_document(message.chat.id, 'CgACAgQAAxkBAANFXoKO98R2gPzLJhW16duPR9juWEkAAiwAA0RADFITndGw_1JN0BgE',reply_markup=keyboard)

bot.polling()