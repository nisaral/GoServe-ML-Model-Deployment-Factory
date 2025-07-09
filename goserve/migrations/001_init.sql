CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE experiments (
    id SERIAL PRIMARY KEY,
    run_id UUID DEFAULT uuid_generate_v4() UNIQUE,
    params JSONB,
    metrics JSONB,
    timestamp VARCHAR(50),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP
);

CREATE TABLE models (
    id SERIAL PRIMARY KEY,
    name UUID DEFAULT uuid_generate_v4() UNIQUE,
    version VARCHAR(50),
    path VARCHAR(255),
    metrics JSONB,
    stage VARCHAR(50),
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    deleted_at TIMESTAMP
);