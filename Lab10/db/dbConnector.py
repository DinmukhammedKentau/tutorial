import psycopg2
from Lab10.config.config import load_config
from Lab10.db.PhoneBook import PhoneBook



class DBConnector:
    def __init__(self):
        self.config = load_config()

    def createTable(self):
        sql = '''
         Create sequence if not exists s;
         Create table if not exists phone_nums(
         id INTEGER DEFAULT nextval('s') PRIMARY KEY,
         first_name VARCHAR(255) NOT NULL,
         last_name VARCHAR(255) NOT NULL,
         phone_number VARCHAR(11) NOT NULL);
         '''

        try:
         with psycopg2.connect(**self.config) as conn:
             with conn.cursor() as cur:
                 cur.execute(sql)
             conn.commit()
        except Exception as e:
            print("ERROR ON CREATING NEW TABLE",e)
    def add_phone(self,p1:PhoneBook):
        sql="Insert into phone_nums (first_name, last_name,phone) Values (%s,%s,%s)"

        try:
         with psycopg2.connect(**self.config) as conn:
             with conn.cursor() as cur:
                 cur.execute(sql,(p1.first_name,p1.last_name,p1.phone_number))
             conn.commit()
        except Exception as e:
            print("ERROR ON INSERTING NEW USER",e)
    def update_phone_by_phone(self,id,phone):
       sql='''
          UPDATE phone_nums 
          SET first_name=%s 
          WHERE id=%s 
          '''
       try:
           with psycopg2.connect(**self.config) as conn:
               with conn.cursor() as cur:
                   cur.execute(sql, (phone, id))
               conn.commit()
       except Exception as e:
           print("ERROR ON UPDATING NEW USER", e)
    def update_first_name(self,id,name):

            sql = '''
                 UPDATE phone_nums 
                 SET first_name=%s 
                 WHERE id=%s 
                 '''
            try:
                with psycopg2.connect(**self.config) as conn:
                    with conn.cursor() as cur:
                        cur.execute(sql, (name, id))
                    conn.commit()
            except Exception as e:
                print("ERROR ON UPDATING NEW USER", e)
    def delete_phone_by_id(self,id):
        sql='''
        DELETE 
        FROM phone_nums 
        WHERE id=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id))
                conn.commit()
        except Exception as e:
            print("ERROR ON DELETING NEW USER", e)
    def get_all_users(self):
        sql="SELECT * FROM phone_nums ORDER BY id ASC"

        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    rows = cur.fetchall()  #келген жолдарды устап алу ушин
                    return rows

        except Exception as e:
            print("ERROR ON LISTING ALL USERS ", e)
    def CreateTableForRace(self):
        sql = '''
                 Create sequence if not exists s;
                 Create table if not exists race_scores(
                 id INTEGER DEFAULT nextval('s') PRIMARY KEY,
                 user VARCHAR(255) NOT NULL,
                 level VARCHAR(11) NOT NULL; )
                 '''

        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
        except Exception as e:
            print("ERROR ON CREATING NEW SCORE RACE TABLE", e)