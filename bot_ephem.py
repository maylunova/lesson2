from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log')


GREETING = 'Call the /planet command and find out which constellations the planets are in!'


def greet_user(bot, update):    
    update.message.reply_text(GREETING)

def talk_to_me(bot, update, user_data):
    question_asked = user_data.get('asked', False)
    
    if question_asked:
        planet_name = update.message.text 
        today = datetime.datetime.now()
        # planet_name = 'Mars' 
        # getattr(ephem, planet_name)(<date>) == ephem.Mars(<date>)
        try:
            planet = getattr(ephem, planet_name)(today.strftime('%Y/%m/%d'))
            ephem_answer = ephem.constellation(planet)
            logging.info(planet_name)
            update.message.reply_text(ephem_answer[1])
        except AttributeError:
             update.message.reply_text("I don't know {} planet.".format(planet_name,) + '\n' + GREETING)


        user_data['asked'] = False

    else:
        update.message.reply_text(GREETING)

def astronomy(bot, update, user_data):
    text = 'What planet are you interested in?'
    user_data['asked'] = True
    update.message.reply_text(text)


def main():
    updater = Updater('467895224:AAF110ARNylzxt_CVZkcp3rAbdtSktjBquM')

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', astronomy, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    updater.start_polling()
    updater.idle()


main()
