# Agility Game Database

PostgreSQL database configuration for the Agility Game application.

## Overview

This directory contains the PostgreSQL database setup and configuration files for both development and production environments.

## Directory Structure

```
database/
├── Dockerfile.dev              # Development Docker configuration
├── postgresql.conf.dev         # PostgreSQL development configuration
├── postgresql.conf.prod        # PostgreSQL production configuration
├── README.md                   # This file
└── sample.env                  # Sample environment variables
```

## Configuration Files

- `postgresql.conf.dev`: Development-specific PostgreSQL settings
- `postgresql.conf.prod`: Production-specific PostgreSQL settings

## Environment Variables

Copy `sample.env` to `.env` and adjust the values:

```env
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=agility_game
```

## Development Setup

1. Build the development container:
```bash
docker compose build database
```

2. Start the database:
```bash
docker compose up database
```

## Production Deployment

1. Use the production configuration:
```bash
cp postgresql.conf.prod postgresql.conf
```

2. Build and run with production settings:
```bash
docker compose -f docker-compose.prod.yml up database
```

The database is now ready to be used by your application. You can connect to it using:

Host: localhost
Port: 5432
Database: agility_game_db

1. Read-only access:
- User: game_reader
- Password: readonly_game_password

2. Read/Write access:
- User: game_writer
- Password: writeaccess_game_password

## Database Maintenance

### Backup
```bash
docker exec agility-game-db pg_dump -U postgres agility_game > backup.sql
```

### Restore
```bash
docker exec -i agility-game-db psql -U postgres agility_game < backup.sql
```

## Example SQL

-- Sort by priority ascending
SELECT * FROM app_data.search_games(
    p_sort_by := 'priority',
    p_sort_direction := 'asc'
);

-- Sort by title descending
SELECT * FROM app_data.search_games(
    p_sort_by := 'title',
    p_sort_direction := 'desc'
);

-- Combine sorting with other filters
SELECT * FROM app_data.search_games(
    p_search_text := 'game',
    p_sort_by := 'priority',
    p_sort_direction := 'desc',
    p_limit := 5,
    p_offset := 0
);

-- Get overall statistics
SELECT * FROM app_data.get_game_stats();

-- Get statistics for today
SELECT * FROM app_data.get_game_stats(
    p_start_date := CURRENT_DATE,
    p_end_date := CURRENT_DATE + INTERVAL '1 day'
);

-- Archive games from a specific month
SELECT * FROM app_data.archive_games(
    p_start_date := '2024-01-01'::TIMESTAMP WITH TIME ZONE,
    p_end_date := '2024-02-01'::TIMESTAMP WITH TIME ZONE
);

-- Check when our games were created
SELECT created_on, title, priority 
FROM app_data.games 
ORDER BY created_on;

-- Archive games from today
SELECT * FROM app_data.archive_games(
    p_start_date := CURRENT_DATE::TIMESTAMP WITH TIME ZONE,
    p_end_date := (CURRENT_DATE + INTERVAL '1 day')::TIMESTAMP WITH TIME ZONE
);

-- Verify the archive
SELECT * FROM app_data.games_archive;

-- Verify original games table
SELECT * FROM app_data.games;

## Security Notes

- Always use strong passwords in production
- Keep your PostgreSQL version updated
- Regularly backup your database
- Use SSL in production

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

MIT License - see the main project LICENSE file for details
