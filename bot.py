import random
import logging
import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define your bot token
BOT_TOKEN = '7339929733:AAHdD-YGmYF2Pu6XRyw1XBZfifjQq__Gt9Q'

# Define jokes and trivia
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Give a man a match, and he’ll be warm for a few hours. Set him on fire, and he’ll be warm for the rest of his life",
    "You don’t need a parachute to go skydiving. You need a parachute to go skydiving twice.",
    "My grandfather said my generation relies too much on the latest technology. I called him a hypocrite and unplugged his life support."
    "My senior relatives liked to tease me at weddings, saying things like, “You’ll be next!” But they stopped after I started saying that to them at funerals."
    "Today was the worst day of my life. My ex got hit by a school bus, and I lost my job as a bus driver.",
    "Why is it that if you donate one kidney, people love you, but if you donate five kidneys, they call the police?",
    "My mother told me, “One man’s trash is another man’s treasure.” Terrible way to learn I’m adopted.",
    "My wife told me she’ll slam my head into the keyboard if I don’t get off the computer. I’m not too worried. I think she’s jokinsdnbfjadskbngfsjkgbsafgfsgadfgdfgdfh.",
    "My boss said to me, 'You’re the worst train driver ever. How many have you derailed this year?' I replied, 'I’m not sure; it’s hard to keep track.'",
    
]

trivia_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome"],
        "correct_answer": "Paris",
    },
    {
        "question": "What galaxy do we live in?",
        "options": ["A) Earth", "B) The milky way", "C) Samsung galaxy s23 ultra"],
        "correct_answer": "The milky way",
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway"],
        "correct_answer": "Harper Lee",
    },
    {
        "question": "What are diamonds made of?",
        "options": ["A) Copper", "B) Gold", "C) Carbon"],
        "correct_answer": "Carbon",
    },
    {
        "question": "Who took all the limelight of boys in Stranger things",
        "options": ["A) Max Mayfield", "B) Eleven", "C) Nancy Wheeler"],
        "correct_answer": "Nancy",
    },
    {
        "question": "You need to enter a dark room and only have one match. What do you light first: an oil heater, an oil lamp or a candle?",
        "options": ["A) oil heater", "B) An oil lamp", "C) Candle"],
        "correct_answer": "Match first noobs XD",
    },
    {
        "question": "A bat and a ball cost a total of $1.10. The bat is more expensive than the ball by exactly $1. What's the price of the ball?",
        "options": ["A) 1$", "B) 0.05$", "C) 0.10$"],
        "correct_answer": "0.05$ (Think twice if you think the answer is incorrect)",
    },
    {
        "question": "A red house is made of red bricks, and a blue house is made of blue bricks. What's a greenhouse made of?",
        "options": ["A) Blue+yellow bricks", "B) White+blue bricks", "C) Green bricks" "D) None of the above"],
        "correct_answer": "None of the above - A greenhouse isn't usually made with any kind of bricks. It's made of glass, so the sun can get in.",
    },
    {
        "question": "Assume you're driving the bus from New York to Boston. Fifteen people get on the bus in New York, and only one person gets off the bus when you reach your destination in Boston. Whats the name of the bus driver?",
        "options": ["A) None of the above", "B) Noone", "C) heavy driver" "D) Sallu bhoi"],
        "correct_answer": "None of the above - u initially mentioned that I am driving the bus, so the name of the driver is my name",
    },


]

# Motivational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

# Define states for the conversation
QUIZ_QUESTION, QUIZ_ANSWER = range(2)

# Dictionary to store birthdays
birthdays = {
    'aashii_86': datetime.date(year=2006, month=6, day=8),
    'Nitanshu1824': datetime.date(year=2006, month=4, day=18),
    'khushii6350': datetime.date(year=2006, month=11, day=15),
    'shivam6350': datetime.date(year=2006, month=12, day=15)
}

# Command handlers
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am your dailylife bot created by someone special👀💕 . Type /joke to get a joke, /trivia for trivia, /quiz to start a quiz, /who to know about me.')

async def joke(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(random.choice(jokes))

async def trivia(update: Update, context: CallbackContext) -> None:
    question = random.choice(trivia_questions)
    trivia_message = f"{question['question']}\n" + "\n".join(question['options'])
    await update.message.reply_text(trivia_message)

async def start_quiz(update: Update, context: CallbackContext) -> int:
    question = random.choice(trivia_questions)
    context.user_data['current_question'] = question
    trivia_message = f"{question['question']}\n" + "\n".join(question['options'])
    await update.message.reply_text(trivia_message)
    return QUIZ_QUESTION

async def check_answer(update: Update, context: CallbackContext) -> int:
    user_answer = update.message.text.strip()
    current_question = context.user_data.get('current_question')
    correct_answer = current_question['correct_answer']

    if user_answer.lower() in correct_answer.lower():
        await update.message.reply_text('Correct!')
    else:
        await update.message.reply_text(f'Wrong! The correct answer was {correct_answer}.')

    return ConversationHandler.END

async def set_morning_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    context.job_queue.run_daily(send_morning_message, time=datetime.time(hour=6, minute=0, second=0), context=chat_id)
    await update.message.reply_text('Good morning message and motivational quote set to be sent daily at 6:00 AM!')

async def send_morning_message(context: CallbackContext) -> None:
    job = context.job
    chat_id = job.context

    # Send "Good morning" message
    await context.bot.send_message(chat_id, text="Good morning everyone!")

    # Send a random motivational quote
    quote = random.choice(quotes)
    await context.bot.send_message(chat_id, text=quote)

async def who(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("I am a bot created by @shivam6350 and khushi.")

async def days_until_birthday(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.username

    # Check if the username is mentioned along with the /WMB command
    mentioned_user = update.message.text.split()[-1].replace('@', '')
    if mentioned_user in birthdays:
        username = mentioned_user

    if username in birthdays:
        today = datetime.date.today()
        birthday = birthdays[username]
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)
        days_until = (next_birthday - today).days
        await update.message.reply_text(f"{username}'s birthday is in {days_until} days.")
    else:
        await update.message.reply_text("Sorry, I don't have the birthday information for that user.")

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Quiz cancelled.')
    return ConversationHandler.END

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    quiz_handler = ConversationHandler(
        entry_points=[CommandHandler('quiz', start_quiz)],
        states={
            QUIZ_QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("trivia", trivia))
    application.add_handler(CommandHandler("setmorningmessage", set_morning_message))
    application.add_handler(CommandHandler("who", who))
    application.add_handler(CommandHandler("WMB", days_until_birthday))
    application.add_handler(quiz_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
