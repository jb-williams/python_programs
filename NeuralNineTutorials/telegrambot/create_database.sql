CREATE TABLE user (
    id INTERGER PRIMARY KEY
);

CREATE TABLE birthday_reminder (
    id INTERGER PRIMARY KEY,
    date DATE NOT NULL,
    name TEXT NOT NULL,
    reminded INTERGER
);

ALTER TABLE birthday_reminder
ADD COLUMN user_id INTERGER REFERENCES user(id);