import sqlite3
from datetime import datetime

DB_NAME = "brain_game.db"

class DatabaseManager:
    def __init__(self):
        """Initialize connection to the SQLite database."""
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the scores table if it doesn't exist."""
        # Added 'is_correct' column to track win/loss ratio
        query = """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            score INTEGER,
            difficulty_level INTEGER,
            is_correct INTEGER, 
            timestamp DATETIME
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def save_score(self, player_name, score, difficulty, is_correct):
        """
        Insert a new game record into the database.
        
        Args:
            player_name (str): The name of the player.
            score (int): The score achieved.
            difficulty (int): The number of digits (3, 5, or 7).
            is_correct (bool): True if the answer was correct, False otherwise.
        """
        query = """
        INSERT INTO scores (player_name, score, difficulty_level, is_correct, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """
        # Convert boolean is_correct to integer (1 for True, 0 for False)
        self.cursor.execute(query, (player_name, score, difficulty, 1 if is_correct else 0, datetime.now()))
        self.conn.commit()

    def get_highscore(self):
        """Get the absolute highest score across all players."""
        query = "SELECT MAX(score) FROM scores"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0

    def get_player_stats(self, player_name):
        """
        Retrieve detailed statistics for a specific player.
        Returns a dictionary containing highscore, total games, accuracy, etc.
        """
        stats = {}
        
        # 1. Get player's personal high score
        self.cursor.execute("SELECT MAX(score) FROM scores WHERE player_name = ?", (player_name,))
        result = self.cursor.fetchone()
        stats['highscore'] = result[0] if result[0] is not None else 0

        # 2. Get total number of games played by this player
        self.cursor.execute("SELECT COUNT(*) FROM scores WHERE player_name = ?", (player_name,))
        stats['total_games'] = self.cursor.fetchone()[0]

        # 3. Get number of correct answers (Wins)
        self.cursor.execute("SELECT COUNT(*) FROM scores WHERE player_name = ? AND is_correct = 1", (player_name,))
        stats['correct_answers'] = self.cursor.fetchone()[0]

        # 4. Get breakdown of games per difficulty level
        # This groups the results by difficulty (3, 5, 7) and counts them
        self.cursor.execute("""
            SELECT difficulty_level, COUNT(*) 
            FROM scores 
            WHERE player_name = ? 
            GROUP BY difficulty_level
        """, (player_name,))
        
        # Initialize dictionary with 0s
        difficulty_counts = {3: 0, 5: 0, 7: 0}
        for row in self.cursor.fetchall():
            # row[0] is difficulty, row[1] is count
            difficulty_counts[row[0]] = row[1]
        
        stats['difficulty_breakdown'] = difficulty_counts

        return stats

    def close(self):
        """Close the database connection."""
        self.conn.close()