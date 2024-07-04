from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'cve_database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/cve/<cve_id>', methods=['GET'])
def get_cve(cve_id):
    conn = get_db_connection()
    cve = conn.execute('SELECT * FROM cves WHERE cve_id = ?', (cve_id,)).fetchone()
    conn.close()
    if cve is None:
        return jsonify({'error': 'CVE not found'}), 404
    return jsonify(dict(cve))

@app.route('/cve/all', methods=['GET'])
def get_all_cves():
    conn = get_db_connection()
    cves = conn.execute('SELECT * FROM cves').fetchall()
    conn.close()
    return jsonify([dict(cve) for cve in cves])

@app.route('/cve/addCVE', methods=['POST'])
def add_cve():
    new_cve = request.get_json()
    conn = get_db_connection()
    conn.execute('''
    INSERT INTO cves (cve_id, description, severity, cvss, affected_packages, cwe_id)
    VALUES (?, ?, ?, ?, ?, ?)''',
    (new_cve['cve_id'], new_cve['description'], new_cve['severity'], new_cve['cvss'], new_cve['affected_packages'], new_cve['cwe_id']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'CVE added successfully'}), 201

@app.route('/cve/<cve_id>', methods=['DELETE'])
def delete_cve(cve_id):
    conn = get_db_connection()
    cve = conn.execute('SELECT * FROM cves WHERE cve_id = ?', (cve_id,)).fetchone()
    if cve is None:
        conn.close()
        return jsonify({'error': 'CVE not found'}), 404
    conn.execute('DELETE FROM cves WHERE cve_id = ?', (cve_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'CVE deleted successfully'}), 200

@app.route('/cve/<cve_id>', methods=['PUT'])
def update_cve(cve_id):
    updated_cve = request.get_json()
    conn = get_db_connection()
    cve = conn.execute('SELECT * FROM cves WHERE cve_id = ?', (cve_id,)).fetchone()
    if cve is None:
        conn.close()
        return jsonify({'error': 'CVE not found'}), 404
    conn.execute('''
    UPDATE cves
    SET description = ?, severity = ?, cvss = ?, affected_packages = ?, cwe_id = ?
    WHERE cve_id = ?''',
    (updated_cve['description'], updated_cve['severity'], updated_cve['cvss'], updated_cve['affected_packages'], updated_cve['cwe_id'], cve_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'CVE updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
