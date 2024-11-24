import random  
import sqlite3  
import time  
 
# Rent A Car Tracking System by:  
# Alp Dogu Akis,  
# Doga Bengu Kotan,  
# Cisem Gure,  
# Yigitcan Teke  
 
# The function for creating the table if not exists  
def create():  
    # Creatinng the Branches table  
    cursor.execute("CREATE TABLE IF NOT EXISTS Branches "  
                   "(branchId INT PRIMARY KEY, "  
                   "branchName varchar(15), "  
                   "branchCity varchar(25), "  
                   "branchTown varchar(25), "  
                   "branchStreet varchar(25))")  
 
    # Creating the Employee table  
    cursor.execute("CREATE TABLE IF NOT EXISTS Employees "  
                   "(employeeId INT PRIMARY KEY, "  
                   "employeeName varchar(40), "  
                   "employeeSurname varchar(20), "  
                   "employeeDepartment varchar(25), "  
                   "employeeBranch INT, "  
                   "employeeGender varchar(1), "  
                   "FOREIGN KEY (employeeBranch) REFERENCES Branches (branchId))")  
 
    # Creating the Customers table  
    cursor.execute("CREATE TABLE IF NOT EXISTS Customers "  
                   "(customerId INTEGER PRIMARY KEY, "  
                   "customerName varchar(40), "  
                   "customerSurname varchar(20), "  
                   "customerPhone INT, "  
                   "customerEmail TEXT, "  
                   "customerGender varchar(1))")  
 
    # Creating the Vehicles table  
    cursor.execute("CREATE TABLE IF NOT EXISTS Vehicles "  
                   "(vehicleId INTEGER PRIMARY KEY, "  
                   "vehicleBrand varchar(20), "  
                   "vehicleModel varchar(30), "  
                   "vehicleType varchar(8), "  
                   "vehicleAvailable BOOLEAN,"  
                   "vehicleInfo TEXT, "  
                   "vehicleRank DECIMAL)")  
 
    # Creating the Vehicles table  
    cursor.execute("CREATE TABLE IF NOT EXISTS SalesData"  
                   "(saleId INTEGER PRIMARY KEY, "  
                   "customerId INT, "  
                   "vehicleId INT, "  
                   "employeeId INT, "  
                   "branchId INT, "  
                   "saleDate DATE, "  
                   "saleEnd DATE, "  
                   "saleType varchar(1), "  
                   "saleCost MONEY, "  
                   "saleProfit MONEY, "  
                   "FOREIGN KEY (customerId) REFERENCES Customers(customerId),"  
                   "FOREIGN KEY (vehicleId) REFERENCES Vehicles (vehicleId),"  
                   "FOREIGN KEY (employeeID) REFERENCES Employees (EmployeeId),"  
                   "FOREIGN KEY (BranchID) REFERENCES Branches (BranchId))")  
 
    con.commit()  
 
 
#The funciton for populating the table  
def fill():  
    #Current branch datas  
    branches_data = [  
        (1, 'Bayrakli', 'Izmir', 'Bayrakli', 'Vatan Caddesi'),  
        (2, 'Bornova', 'Izmir', 'Bornova', 'Ataturk Caddesi'),  
        (3, 'Atasehir', 'Istanbul', 'Atasehir', 'Bayram Caddesi')]  
 
    # Populating the datas into the related table  
    cursor.executemany("INSERT INTO Branches VALUES (?, ?, ?, ?, ?)", 
branches_data)  
 
 
 
    #Current employee datas  
    employees_data = [  
        (1, 'Ahmet', 'Yılmaz', 'İnsan Kaynakları',3, 'E'),  
        (2, 'Çisem', 'Güre', 'Satış', 3, 'K'),  
        (3, 'Mehmet', 'Arslan', 'Satış', 1, 'E'),  
        (4, 'Zeynep', 'Kurt', 'Pazarlama', 3, 'K'),  
        (5, 'Doğa', 'Kotan', 'Satış', 2, 'E'),  
        (6, 'Fatma', 'Toprak', 'İnsan Kaynakları', 2, 'K'),  
        (7, 'Alp', 'Akış', 'Satış', 1, 'E'),  
        (8, 'Yiğitcan', 'Teke', 'Satış', 3, 'K'),  
        (9, 'Ali', 'Demir', 'Pazarlama', 1, 'E'),  
        (10, 'Aysun', 'Ergin', 'Bilişim Teknolojileri', 3, 'K'),  
        (11, 'Serdar', 'Özdemir', 'Satış', 2, 'E'),  
        (12, 'Melisa', 'Şener', 'Satış', 1, 'K'),  
        (13, 'Mert', 'Kaya', 'Bilişim Teknolojileri', 1, 'E'),  
        (14, 'Nazlı', 'Güneş', 'Satış', 2, 'K'),  
        (15, 'Oğuzhan', 'Kaya', 'Satış', 3, 'E')]  
 
    # Populating the datas into the related table  
    cursor.executemany("INSERT INTO employees VALUES(?,?,?,?,?,?)", 
employees_data)  
 
 
    #Current customer datas  
    customers_data = [  
    (1, 'Furkan', 'Çalışkanerler', '5551234567', 'furkanclskn@email.com', 'E'),  
    (2, 'Ali', 'Kara', '5559876543', 'ali@email.com', 'E'),  
    (3, 'Sibel', 'Çelik', '5555551234', 'sibel@email.com', 'K'),  
    (4, 'Emre', 'Arslan', '5553334445', 'emre@email.com', 'E'),  
    (5, 'Mert', 'Yılmaz', '5556667778', 'mert@email.com', 'E'),  
    (6, 'Nazlı', 'Özdemir', '5551112233', 'nazli@email.com', 'K'),  
    (7, 'Hakan', 'Kurt', '5554445556', 'hakan@email.com', 'E'),  
    (8, 'Zeynep', 'Şahin', '5552223334', 'zeynep@email.com', 'K'),  
    (9, 'Mehmet', 'Güneş', '5557778889', 'mehmet@email.com', 'E'),  
    (10, 'Seda', 'Turan', '5558889990', 'seda@email.com', 'K'),  
    (11, 'Kadir', 'Kaya', '5551112223', 'kadir@email.com', 'E'),  
    (12, 'Cemre', 'Yıldız', '5554445556', 'cemre@email.com', 'K'),  
    (13, 'Murat', 'Arıkan', '5553334445', 'murat@email.com', 'E'),  
    (14, 'Duygu', 'Çınar', '5559876543', 'duygu@email.com', 'K'),  
    (15, 'Gökhan', 'Tunç', '5551234567', 'gokhan@email.com', 'E'),  
    (16, 'Nergis', 'Aksoy', '5558889990', 'nergis@email.com', 'K'),  
    (17, 'Serdar', 'Toprak', '5551234999', 'serdar@email.com', 'E'),  
    (18, 'Seda', 'Aydın', '5556661111', 'seda@email.com', 'K'),  
    (19, 'Eren', 'Özdemir', '5555552222', 'eren@email.com', 'E'),  
    (20, 'Esra', 'Bilgi', '5553337777', 'esra@email.com', 'K'),  
    (21, 'Mert', 'Can', '5559995555', 'mert@email.com', 'E'),  
    (22, 'Fatma', 'Güzel', '5556664444', 'fatma@email.com', 'K'),  
    (23, 'Emir', 'Sarı', '5552221111', 'emir@email.com', 'E'),  
    (24, 'Aylin', 'Başar', '5551114444', 'aylin@email.com', 'K'),  
    (25, 'Mehmet', 'Kartal', '5556663333', 'mehmet@email.com', 'E'),  
    (26, 'Selin', 'Gökçe', '5559998888', 'selin@email.com', 'K'),  
    (27, 'Oğuz', 'Erdoğan', '5552225555', 'oguz@email.com', 'E'),  
    (28, 'Merve', 'Öztürk', '5553336666', 'merve@email.com', 'K'),  
    (29, 'Kerem', 'Akın', '5556667777', 'kerem@email.com', 'E'),  
    (30, 'Nihan', 'Yıldız', '5555558888', 'nihan@email.com', 'K'),  
    (31, 'Hüseyin', 'Karahan', '5551116666', 'huseyin@email.com', 'E'),  
    (32, 'Deniz', 'Çakır', '5554448888', 'deniz@email.com', 'K'),  
    (33, 'Zafer', 'Türk', '5556665555', 'zafer@email.com', 'E'),  
    (34, 'Arzu', 'Güçlü', '5559997777', 'arzu@email.com', 'K'),  
    (35, 'Furkan', 'Demirci', '5552224444', 'furkan@email.com', 'E'),  
    (36, 'Sude', 'Ekmekçi', '5555559999', 'sude@email.com', 'K'),  
    (37, 'Emir', 'Şimşek', '5553335555', 'emir@email.com', 'E'),  
    (38, 'Begüm', 'Kılıç', '5554446666', 'begum@email.com', 'K'),  
    (39, 'Can', 'Şentürk', '5556663333', 'can@email.com', 'E'),  
    (40, 'Ezgi', 'Bayrak', '5558884444', 'ezgi@email.com', 'K'),  
    (41, 'Cem', 'Savran', '5555555555', 'cem@email.com', 'E'),  
    (42, 'Ebru', 'Yaman', '5551118888', 'ebru@email.com', 'K'),  
    (43, 'Selim', 'Gür', '5554445555', 'selim@email.com', 'E'),  
    (44, 'Nil', 'Çetin', '5556666666', 'nil@email.com', 'K'),  
    (45, 'Yiğit', 'Taş', '5559999999', 'yigit@email.com', 'E'),  
    (46, 'Zara', 'Gümüş', '5552222222', 'zara@email.com', 'K'),  
    (47, 'Sefa', 'Kan', '5555551111', 'sefa@email.com', 'E'),  
    (48, 'Ela', 'Akar', '5553333333', 'ela@email.com', 'K'),  
    (49, 'Gözde', 'Kurtuluş', '5554444444', 'gozde@email.com', 'K'),  
    (50, 'Emin', 'Türkmen', '5556666666', 'emin@email.com', 'E')]  
 
    # Populating the datas into the related table  
    cursor.executemany("INSERT INTO customers VALUES(?,?,?,?,?,?)", 
customers_data)  
 
 
    vehicles_data = [  
        (1, 'Renault', 'Clio', 'Hatchback', 1, 'Tamamen hazir.', 4.9),  
        (2, 'Renault', 'Clio', 'Hatchback', 0, 'Ic temizligi yapilmadi.', 4.2),  
        (3, 'Ford', 'Focus', 'Sedan', 1, 'Tamamen hazir.', 3.8),  
        (4, 'Ford', 'Focus', 'Sedan', 1, 'Tamamen hazir.', 4.0),  
        (5, 'Ford', 'Fiesta', 'Hatchback', 1, 'Tamamen hazir.', 3.9),  
        (6, 'Ford', 'Fiesta', 'Hatchback', 1, 'Pasta cila yapilacak.', 3.7),  
        (7, 'Fiat', 'Egea', 'Sedan', 1, 'Muayenesi yaklasti.', 3.8),  
        (8, 'Fiat', 'Egea', 'Sedan', 1, 'Tamamen hazir.', 4.2),  
        (9, 'Citroen', 'C -Elysee', 'Sedan', 0, 'Serviste.', 3.7),  
        (10, 'Citroen', 'C -Elysee', 'Sedan', 1, 'Tamamen hazir.', 4.5),  
        (11, 'Citroen', 'C -Elysee', 'Sedan', 0, 'Balans ayari yapilacak.', 3.9),  
        (12, 'Citroen', 'C -Elysee', 'Sedan', 1, 'Silecek suyu bitti.', 4.3),  
        (13, 'Citroen', 'C -Elysee', 'Sedan', 1, 'Tamamen hazir.', 4.6),  
        (14, 'Renault', 'Symbol', 'Sedan', 1, 'Tamamen hazir.', 4.8),  
        (15, 'Renault', 'Symbol', 'Sedan', 1, 'Tamamen hazir.', 4.7),  
        (16, 'Peugeot', '301', 'Sedan', 1, 'Sigortasi yaklasti.',4.1),  
        (17, 'Dacia', 'Duster', 'SUV', 0, 'Motor Arizasi.', 3.2),  
        (18, 'Dacia', 'Duster', 'SUV', 1, 'Yeni Temizlendi', 3.7),  
        (19, 'Dacia', 'Duster', 'SUV', 1, 'Ic aydinlatma calismiyor', 3.1),  
        (20, 'Ford', 'Tourneo Courier', 'Ticari', 1, 'Kullanima hazir', 4.8),  
        (21, 'Ford', 'Tourneo Courier', 'Ticari', 0, 'Yağ sorunu', 4.2),  
        (22, 'Dacia', 'Sandero Stepway', 'B -SUV', 1, 'Kullanima hazir', 4.1),  
        (23, 'Dacia', 'Sandero Stepway', 'B -SUV', 1, 'Kullanima hazir', 3.9),  
        (24, 'Dacia', 'Sandero Stepway', 'B -SUV', 1, 'Kullanima hazir', 4.3)]  
 
    # Populating the datas into the related table  
    cursor.executemany("INSERT INTO Vehicles VALUES(?,?,?,?,?,?,?)", 
vehicles_data)  
 
    con.commit()  
 
 
#The funciton for creating the sales datas in the given range  
def salesAlgorythm():  
 
    def dateIsValid(day, month, year):  
 
        months30 = [4, 6, 9, 11]  
        ifMonth30 = months30.__contains__(month)  
 
        if month > 12 or month < 1:  
            return False  
 
        if day > 31 or day < 1:  
            return False  
 
        if month == 2 and day > 28:  
            return False  
 
        if ifMonth30 and day > 30:  
            return False  
 
        else: 
            return True  
 
    def generateSaleDate(day, month, year):  
 
        start_day = day + random.randrange(0, 7)  
 
        while (dateIsValid(start_day, month, year) == False):  
 
            start_day = day + random.randrange(0, 3)  
 
        end_day = start_day + random.randrange(1, 7)  
        end_month = month  
        end_year = year  
        if (dateIsValid(end_day, month, year) == False):  
            end_day -= 30 
            if (month == 12):  
                end_month = 1  
                end_year = year + 1  
            else: 
                end_month = month + 1  
        ultimate_list = [(start_day, month, year), (end_day, end_month, end_year)]  
        return ultimate_list  
 
    sales_data = []  
    sellers = cursor.execute("SELECT employeeId from Employees where employeeDepartment = 'Satış'")
    seller_request = cursor.fetchall()  
    seller_set = []  
 
    for i in seller_request:  
        for j in i:  
            seller_set.append(j)  
 
    year = 2019  
    month = 1  
    day = 1 
    inflation_rate = 0.3  
 
    for year_count in range(1, 4):# 3 Years of sale records  
        year += 1  
        month = 1  
        inflation_rate *= 2.0  
 
        for month_count in range(1, 13):# 12 months for each year  
 
            day = 1 
 
            if 5 < month and month < 9: # Summer months higher sale and profit rate
 
                sale_count = random.randrange(9, 12)  
                profit_rate = random.uniform(1.65, 2.15)  
 
            else: 
 
                sale_count = random.randrange(7, 11)  
                profit_rate = random.uniform(0.45, 1.7)  
 
 
            for i in range(1, sale_count + 1):  
 
                sale_cost = 1000 * random.uniform(0.65, 1.5) * inflation_rate  
                sale_profit = (sale_cost * profit_rate) - sale_cost  
                sale_profit = round(sale_profit, 3)  
                sale_cost = round(sale_cost, 3)  
 
                dates = generateSaleDate(day, month, year)  
 
                start_date = dates[0]  
                end_date = dates[1]  
 
                day = start_date[0]  
                month = start_date[1]  
                year = start_date[2]  
 
                if random.randrange(1, 100) < 65: #65% Bireysel satış  
                    saleType = 'B'  
                else: 
                    saleType = 'K'  
 
                saleDate = f"{start_date[0]} -{start_date[1]} -{start_date[2]}"  
                saleEnd = f"{end_date[0]} -{end_date[1]} -{end_date[2]}"  
 
                employee = random.choice(seller_set)  
                query = f"SELECT employeeBranch FROM Employees WHERE employeeId = {employee}"
                cursor.execute(query)  
 
                branch = cursor.fetchall()[0][0]  
 
                customer = random.randrange(1, 50)  
 
                vehicle = random.randrange(1, 24)  
 
                data_tuple = (None, customer, vehicle, employee, branch, saleDate, 
saleEnd, saleType, sale_cost, sale_profit)  
                cursor.execute("INSERT INTO SalesData VALUES(?,?,?,?,?,?,?,?,?,?)", data_tuple)
                con.commit()  
 
            month += 1  
 
 
def triggers():  
    cursor.execute("CREATE TRIGGER updateVehicleAvailability "  
                   "AFTER INSERT ON SalesData "  
                   "FOR EACH ROW "  
                   "BEGIN "  
                   "UPDATE Vehicles "  
                   "SET vehicleAvailable = 0 "  
                   "WHERE vehicleId = NEW.vehicleId;"  
                   " END;")  
 
    con.commit()  
 
con = sqlite3.connect("Rent A Car.db")  # Connection to the database  
time.sleep(1) # Waiting to database
cursor = con.cursor() #Cursor object  
cursor.execute("PRAGMA foreign_keys = ON;")  
con.commit()  
create()  
try: 
    fill() 
except: 
    pass 
salesAlgorythm()  
triggers()  
con.close()  
