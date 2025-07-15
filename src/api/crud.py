import psycopg2.extras
from database import get_db_connection

def get_top_products(limit: int):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""
        SELECT product, mention_count
        FROM raw.fct_top_products
        ORDER BY mention_count DESC
        LIMIT %s
    """, (limit,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_channel_activity(channel_name: str):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""
        SELECT channel, post_count, avg_message_length
        FROM raw.fct_channel_activity
        WHERE channel = %s
    """, (channel_name,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def search_messages(query: str):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""
        SELECT message, channel, timestamp
        FROM raw.fct_message_search
        WHERE message ILIKE %s
        ORDER BY timestamp DESC
        LIMIT 50
    """, (f"%{query}%",))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
