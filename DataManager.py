import pymysql

class DataManager:

	connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Garden',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
	
	@staticmethod
	def getLatestMoisture():
	
		result = ""
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT zone1, zone2, zone3, zone4 FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        			
		finally:
    			connection.close()
    			return [result["zone1"], result["zone2"], result["zone3"], result["zone4"]]

	@staticmethod
	def getLatestRainfall():
	
		result = ""
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT rain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        			
		finally:
    			connection.close()
    			return result["rain"]
    			
    @staticmethod
	def getPredictedRainfall():
	
		result = ""
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT pchance, prain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        		
		finally:
    			connection.close()
    			return [result["pchance"], result["prain"]]
    			
    @staticmethod
	def getPreviousWateringTimes():
	
		result = ""
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT record, water1, water2, water3, water4 FROM observed where record BETWEEN (NOW() - INTERVAL 2 DAY) AND NOW() order by record desc"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			for row in result:
        				if row[1] > 0 or row[2] > 0 or row[3] > 0 or row[4] > 0;
        					return row
        			return ["2000-01-01 01:00:00", 0, 0, 0, 0]
    			
    @staticmethod
	def getSprinklerWaterRate():
	
		result = ""
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT gpm FROM calibration"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			return [result[0], result[1], result[2], result[3]]
    			
    @staticmethod
	def getTargetCapacity():

		result = ""
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT capcity FROM calibration"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			return result
    			
    			
    			
    			
    			
    			
    			
    			
    			