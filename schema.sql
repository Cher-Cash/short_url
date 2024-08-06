CREATE TABLE IF NOT EXISTS urls (
    created_at TIMESTAMP,
    short_hash TEXT PRIMARY KEY,
    long_url TEXT,
    counter INTEGER
);
