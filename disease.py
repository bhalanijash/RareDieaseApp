from db import get_db_connection

def get_all_diseases():
    """Fetch all diseases from MySQL."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rare_diseases")
    diseases = cursor.fetchall()
    conn.close()
    return diseases

def add_disease(name, description):
    """Insert a new disease into MySQL."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rare_diseases (name, description) VALUES (%s, %s)", (name, description))
    conn.commit()
    conn.close()

def get_disease_by_id(disease_id):
    """Retrieve a disease by ID."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rare_diseases WHERE id = %s", (disease_id,))
    disease = cursor.fetchone()
    conn.close()
    return disease

def update_disease(disease_id, name, description):
    """Update a disease entry."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE rare_diseases SET name = %s, description = %s WHERE id = %s", (name, description, disease_id))
    conn.commit()
    conn.close()

def delete_disease(disease_id):
    """Delete a disease from MySQL."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rare_diseases WHERE id = %s", (disease_id,))
    conn.commit()
    conn.close()
