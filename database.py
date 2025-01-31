import sqlite3

def init_db():
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, author TEXT, quote TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

    

    og_quotes = [
        ("The only way to do great work is to love what you do.", "Steve Jobs"),
        ("Success is not the key to happiness. Happiness is the key to success", "Albert Schweitzer"),
        ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
        ("Your limitation - it's only your imagination", "Unknown"),
        ("Push yourself, because no one else is going to do it for you", "Unknown"),
        ("Great things never come from comfort zones.", "Unknown"),
        ("Dream it. Wish it. Do it", "Unknown"),
        ("Success doesn't just find you. You have to go out and get it.", "Unknown"),
        ("The harder you work for something, the greater you'll feel when you achieve it.", "Unknown"),
        ("Dream bigger. Do bigger.", "Unknown"),
        ("Don't stop when you're tired. Stop when you're done.", "Unknown"),
        ("Wake up with determination. Go to bed with satisfaction", "Unknown"),
        ("Do something today that your future self will thank you for.", "Unknown"),
        ("Little things make big days.", "Unknown"),
        ("It's going to be hard, but hard does not mean impossible.", "Unknown"),
        ("Don't way for opportunity. Create it.", "George Bernard Shaw"),
        ("Sometimes we're tested not to show our weaknesses, but to discover our strengths", "Unknown"),
        ("The key to success is to focus on goals, not obstacles.", "Unknown"),
        ("Dream it. Believe it. Build it.", "Unknown"),
        ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
        ("You are never too old to set another goal or to dream a new dream", "C.S. Lewis"),
        ("If you want to achieve greatness stop asking for permission.", "Unknown"),
        ("The only limit to our realization of tomorrow will be our doubts of today.", "Franklin D. Roosevelt"),
        ("Act as if what you do makes a difference. It does.", "William James"),
        ("Success is not how high you have climbed, but how you make a positive difference to the world.", "Roy T. Bennett"),
        ("What lies behind us and what lies before us are tiny matters compared to what lies within us.", "Ralph Waldo Emerson"),
        ("You don't have to be great to start, but you have to start to be great.", "Zig Ziglar"),
        ("The only person you are destined to become is the person you decide to be.", "Ralph Waldo Emerson"),
        ("Your passion is waiting for your courage to catch up.", "Isabelle Lafleche"),
        ("Magic happens outside your comfort zone.", "Unknown"),
        ("Success usually comes to those who are too busy to be looking for it.", "Henry David Thoreau"),
        ("Opportunities don't happen. You create them", "Chris Grosser"),
        ("Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.", "Roy T. Bennett"),
        ("The way to get started is to quit talking and begin doing.", "Walt Disney")
        ]
    
    users = [
        ("username", "password")
    ]
    
    for (quote, author) in og_quotes:
        c.execute('INSERT INTO quotes(quote, author) VALUES (?, ?)', (quote, author))

    for (username, password) in users:
        c.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_db()