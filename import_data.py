import csv
import sqlite3

def create_table(conn):
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS cves (
        id INTEGER PRIMARY KEY,
        cve_id TEXT NOT NULL,
        description TEXT,
        severity TEXT,
        cvss REAL,
        affected_packages TEXT,
        cwe_id TEXT
    );
    '''
    conn.execute(create_table_sql)

def import_data(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    create_table(conn)
    
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            conn.execute('''
            INSERT INTO cves (cve_id, description, severity, cvss, affected_packages, cwe_id)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (row['CVE-ID'], row['Description'], row['Severity'], row['CVSS'], row['Affected Packages'], row['CWE-ID']))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    import_data('CVE_DATABASE.csv', 'cve_database.db')
