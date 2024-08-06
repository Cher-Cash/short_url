CREATE TABLE IF NOT EXISTS urls (
    created_at TIMESTAMP,
    short_hash TEXT PRIMARY KEY,
    long_url TEXT
);


CREATE TABLE IF NOT EXISTS url_counters (
    short_hash TEXT,
    counter INTEGER,
    FOREIGN KEY (short_hash) REFERENCES urls(short_hash)
);
