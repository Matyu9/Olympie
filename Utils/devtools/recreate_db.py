def recreate_db(database):
    database.exec("DROP TABLE IF EXISTS cantina_administration.user", None)
    database.exec("""CREATE TABLE IF NOT EXISTS cantina_administration.user(id INT PRIMARY KEY AUTO_INCREMENT, 
    token TEXT, username TEXT, password TEXT, email TEXT, email_verified BOOL, email_verification_code TEXT, A2F BOOL, 
    A2F_secret TEXT, last_connection DATE, admin BOOL, desactivated BOOL DEFAULT FALSE)""", None)
