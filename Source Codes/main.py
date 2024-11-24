from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from  newfile import Ui_MainWindow  
import sqlite3 
from datetime import datetime  

# Rent A Car Tracking System by:
# Alp Dogu Akis,
# Doga Bengu Kotan,
# Cisem Gure,
# Yigitcan Teke
 
con = sqlite3.connect( "Rent A Car.db" ) 
 
cursor = con.cursor()  
 
class main(QMainWindow):  
    def __init__ (self) -> None: 
        super().__init__ () 
        self.qtTasarim = Ui_MainWindow()  
        self.qtTasarim.setupUi( self) 
        self.qtTasarim.ekle.clicked.connect( self.eklebutonu)  
        self.ComboBox()  
        self.populate_table()  
        self.qtTasarim.register_2.clicked.connect( self.customerregister)  
 
    def ComboBox (self): 
        cursor.execute( "SELECT customerId, customerName, customerSurname FROM Customers" )
        values = cursor.fetchall( ) 
        options = []  
        for i in values: 
            item = f"{i[0]}, {i[1][0]}.{i[2]}" 
            options.append(item)  
 
        self.qtTasarim.salescustomer.addItems(options)  
        options.clear()  
 
        cursor.execute( "SELECT vehicleId, vehicleBrand, vehicleModel, vehicleRank FROM Vehicles WHERE vehicleAvailable = 1" )
        values = cursor.fetchall()  
        options = []  
        for i in values: 
            item = f"{i[0]}, {i[1][0]} {i[2]} {i[3]}" 
            options.append(item)  
 
        self.qtTasarim.salesvehicle.addItems(options)  
        options.clear()  
 
        cursor.execute( "SELECT employeeId, employeeName, employeeSurname FROM Employees WHERE employeeDepartment = 'Satış' " )
        values = cursor.fetchall()  
        options = []  
        for i in values: 
            item = f"{i[0]}, {i[1]} {i[2]}" 
            options.append(item)  
 
        self.qtTasarim.salesemployee.addItems(options)  
        options.clear()  
 
        cursor.execute( "SELECT branchName FROM Branches" ) 
        values = cursor.fetchall()  
        options = []  
        for i in values: 
            item = f"{i[0]}" 
            options.append(item)  
 
        self.qtTasarim.salesbranch.addItems(options)  
        options.clear()  
 
    def fetch_data_from_database (self): 
        cursor.execute( "SELECT * FROM SalesData" ) 
        data = cursor.fetchall()  
        return data 
 
    def populate_table (self): 
        sales_data = self.fetch_data_from_database()  
 
        self.qtTasarim.tableWidget.setRowCount( len(sales_data))  
        self.qtTasarim.tableWidget.setColumnCount( len(sales_data[ 0])) 
 
        for row_index , row_data in enumerate (sales_data):  
            for col_index , cell_value in enumerate (row_data):  
                item = QTableWidgetItem( str(cell_value))  
                self.qtTasarim.tableWidget.setItem(row_index , col_index , item) 
 
    def customerregister (self): 
        cname = self.qtTasarim.cName.text()  
        csurname = self.qtTasarim.cSurname.text()  
        cphone = self.qtTasarim.cPhone.text()  
        cEmail = self.qtTasarim.cEmail.text()  
        cgender = self.qtTasarim.cGender.currentText()  
 
        if not cname or not csurname or not cphone or not cEmail or cgender == "Select" :
            error_message = "<font color='red'>Please enter values.</font> " 
            self.qtTasarim.cMesage.setText(error_message)  
            return 
 
        if not cphone.isdigit() or len(cphone) != 10: 
            error_message = "<font color='red'>Invalid phone number.</font>"  
            self.qtTasarim.cMesage.setText(error_message)  
            return 
 
        data_tuple = ( None, cname, csurname , cphone, cEmail, cgender[ 0]) 
        cursor.execute( "INSERT INTO Customers VALUES (?,?,?,?,?,?)" , data_tuple)  
        con.commit()  
        error_message = f"<font color='green'> {cname} has successfully registered.</font>"
        self.qtTasarim.cMesage.setText(error_message)  
        self.qtTasarim.salescustomer.clear()  
 
        cursor.execute( "SELECT customerId, customerName, customerSurname FROM Customers" )
        values = cursor.fetchall()  
        options = []  
        for i in values: 
            item = f"{i[0]}, {i[1][0]}.{i[2]}" 
            options.append(item)  
 
        self.qtTasarim.salescustomer.addItems(options)  
        options.clear()  
 
 
    def eklebutonu (self): 
        customer = self.qtTasarim.salescustomer.currentText()  
        vehicle = self.qtTasarim.salesvehicle.currentText()  
        employee = self.qtTasarim.salesemployee.currentText()  
        branch = self.qtTasarim.salesbranch.currentText()  
        stype = self.qtTasarim.comboBox.currentText()  
        cost = self.qtTasarim.salescost.text()
        profit = self.qtTasarim.salesprofit.text()
        date = self.qtTasarim.salesstartdate.text()
        enddate = self.qtTasarim.salesenddate.text()
 
        if not (customer and vehicle and employee and branch and stype): 
            error_message = "<font color='red'>Please select values for customer, vehicle, employee, branch, and type.</font>"
            self.qtTasarim.salesMesage.setText(error_message)  
            return 
 
        try: 
            cost = float(cost) 
            profit = float(profit)  
        except ValueError :
            error_message = "<font color='red'>Invalid cost or profit value. Please enter a valid number.</font>"
            self.qtTasarim.salesMesage.setText(error_message)  
            return 
 
        date_format = "%m-%d-%Y"
        try: 
            datetime.strptime(date, date_format)
            datetime.strptime(enddate, date_format)
        except ValueError:
            error_message = "<font color='red'>Invalid date format. Please enter the date in the format mm -dd-yyyy.</font>"
            self.qtTasarim.salesMesage.setText(error_message)  
            return

        querry = "SELECT branchId FROM Branches WHERE branchName = ?"
        cursor.execute(querry, (branch,))
        fetched = cursor.fetchall()
        print(fetched)
        branchid = int(fetched[0][0])
        customerid = int(customer.split(',')[0])
        vehicleid = int(vehicle.split(',')[0])
        employeeid = int(employee.split(',')[0])
        types = stype[0]
 
        data_tuple = ( None, customerid , vehicleid , employeeid , branchid , date, enddate, types, cost, profit)
        cursor.execute( "INSERT INTO SalesData VALUES(?,?,?,?,?,?,?,?,?,?)" , data_tuple)
        con.commit()  
 
        self.qtTasarim.salesvehicle.clear()  
        cursor.execute("SELECT vehicleId, vehicleBrand, vehicleModel, vehicleRank FROM Vehicles WHERE vehicleAvailable = 1" )
        values = cursor.fetchall()  
        options = []
        for i in values: 
            item = f"{i[0]}, {i[1][0]} {i[2]} {i[3]}" 
            options.append(item)  
 
        self.qtTasarim.salesvehicle.addItems(options)  
        options.clear()  
 
        self.populate_table()  
        system_message = "<font color='green'>Added successfully.</font>"  
        self.qtTasarim.salesMesage.setText(system_message)  
        return 
 
 
app = QApplication([])  
pencere = main()  
pencere.show()  
app.exec_()  
con.close()