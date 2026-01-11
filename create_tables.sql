-- Cleanup: Remove tables if they already exist to start fresh
DROP TABLE IF EXISTS long_term_tracking CASCADE;
DROP TABLE IF EXISTS weekly_tracking CASCADE;
DROP TABLE IF EXISTS daily_tracking CASCADE;
DROP TABLE IF EXISTS goals_catalog CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- 1. USERS: To handle personal accounts and secure access
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

-- 2. GOALS_CATALOG: The "Architect" table. 
-- Defines what you want to track and how often.
CREATE TABLE goals_catalog (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    category TEXT NOT NULL, 
    frequency TEXT NOT NULL, 
    description TEXT,
    created_at DATE DEFAULT CURRENT_DATE
);

-- 3. DAILY_TRACKING: For habits like "Drink 2L of water" or "Meditation"
CREATE TABLE daily_tracking (
    id SERIAL PRIMARY KEY,
    goal_id INTEGER REFERENCES goals_catalog(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    f_date DATE NOT NULL,
    status BOOLEAN DEFAULT TRUE
);

-- 4. WEEKLY_TRACKING: Uses ISO Week numbers (The Thursday Rule)
CREATE TABLE weekly_tracking (
    id SERIAL PRIMARY KEY,
    goal_id INTEGER REFERENCES goals_catalog(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    f_year INTEGER NOT NULL,
    f_week INTEGER NOT NULL,
    status BOOLEAN DEFAULT TRUE
);

-- 5. LONG_TERM_TRACKING: For Monthly, Quarterly, and Yearly reviews
-- We use a UNIQUE constraint to prevent duplicate entries for the same period.
CREATE TABLE long_term_tracking (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    goal_id INTEGER REFERENCES goals_catalog(id) ON DELETE CASCADE,
    f_year INTEGER NOT NULL,
    f_period_type TEXT NOT NULL, 
    f_period_value INTEGER NOT NULL, 
    status BOOLEAN DEFAULT TRUE,
    UNIQUE(user_id, goal_id, f_year, f_period_type, f_period_value)
);