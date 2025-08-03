import sqlite3

# SQL queries for the database
count_reqsets = "SELECT COUNT(*) FROM reqng_reqset"
list_reqsets = "SELECT * FROM reqng_reqset"
count_linkset = "SELECT COUNT(*) FROM reqng_artifact"
list_linkset = "SELECT * FROM reqng_artifact"

class DBconnection:
    """A simple class to manage a SQLite database connection"""
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query: str, params: tuple = ()):
        """Execute a SQL query"""
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self):
        """Fetch all results from the last executed query"""
        return self.cursor.fetchall()
    
    def close(self):
        """Close the database connection"""
        self.connection.close()
    
class DBAccess:
    """A class to access the database and perform operations"""
    
    def __init__(self, db_name: str):
        self.db = DBconnection(db_name)

    def close(self):
        """Close the database connection"""
        self.db.close()

    def count_reqsets(self)-> int:
        """Count the number of request sets in the database"""
        self.db.execute(count_reqsets)
        result = self.db.fetchall()
        return result[0][0] if result else 0

    def list_reqsets(self):
        """List all request sets in the database"""
        self.db.execute(list_reqsets)
        results = self.db.fetchall()
        reqsets = []
        for reqset in results:
            reqsets.append({
                "name": reqset[1],
                "description": reqset[12],
                "uuid": reqset[5],
            })
        return reqsets
        
    def count_linkset(self) -> int:
        """Count the number of link sets in the database"""
        self.db.execute(count_linkset)
        result = self.db.fetchall()
        return result[0][0] if result else 0
    
    def list_linkset(self):
        """List all link sets in the database"""
        self.db.execute(list_linkset)
        results = self.db.fetchall()
        linksets = []
        for linkset in results:
            name = linkset[4]
            name = name.replace(".", "~")
            name = name + ".slmx"
            linksets.append({
                "name": name,
                "description": linkset[6],
                "uuid": linkset[1],
            })
        return linksets
    

if __name__ == "__main__":
    # Example usage
    dbAccess = DBAccess("mwreqservices_default.db")
    print("Count of request sets:", dbAccess.count_linkset())   
    print("List of request sets:", dbAccess.list_reqsets())
    # Close the database connection
    dbAccess.close()