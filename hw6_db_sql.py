'''
Name: NENG PAN
Uniqname: panng
'''

import sqlite3 

def question0():
    ''' Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor() # create a cursor to interact with the database
    query = "SELECT * FROM Region" # The SQL commands will be supplied as strings
    result = cursor.execute(query).fetchall() # The cursor is iterable, can be treated as a list
    connection.close()
    return result

def question1():
    ''' Show all fields from the Territory table.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Territory" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question2():
    ''' Show how many employees there are.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM Employee" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question3():
    ''' Show the last 10 rows of the Product table ordered by Id in descending order.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Product ORDER BY Id DESC LIMIT 10" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question4():
    ''' Show the names and unit prices of the three products that have the highest unit prices.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function 
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice FROM Product ORDER BY UnitPrice DESC LIMIT 3" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question5():
    ''' Show the names, unit prices and numbers of units in stock of all products 
    that have between 60 and 100 (including 60 and 100) units in stock.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice, UnitsInStock FROM Product WHERE UnitsInStock BETWEEN 60 AND 100" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question6():
    ''' Show the names of all the products that require a reorder 
    (If the units in stock of a product are lower than its reorder level, the product requires a reorder).
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName FROM Product WHERE UnitsInStock < ReorderLevel" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question7():
    ''' Show Ids of all the orders that were shipped to France where postal code ends with "04".
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT Id FROM [Order] WHERE ShipCountry = 'France' AND ShipPostalCode LIKE '%04'" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question8():
    ''' Show the company names and contact names of all customers who live in the UK and have a fax number on record.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT CompanyName, ContactName FROM Customer WHERE Country='UK' AND Fax <> ''" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question9():
    ''' Show the names and unit prices of all Beverage products.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT ProductName, UnitPrice FROM Product WHERE CategoryID = '1'" 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question10():
    ''' Show the names of all Meat/Poultry products that were discontinued (Discontinued column has a value of 1).
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
    SELECT ProductName 
    FROM Product 
    WHERE Discontinued = '1' AND CategoryId = '6'
    """ 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question11():
    ''' Show order Ids and first names and last names of associated employees of all orders 
    that were shipped to Germany.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
    SELECT [Order].Id, FirstName, LastName 
    FROM [Order]
        JOIN Employee
            ON [Order].EmployeeId = Employee.Id  
    WHERE [Order].ShipCountry = 'Germany'
    """ 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question12():
    ''' Show the order Ids, order dates, and names of the companies 
    that placed the respective orders of all orders that were placed on or before July 10, 2012.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
    SELECT [Order].Id, OrderDate, CompanyName  
    FROM [Order]
        JOIN Customer
            ON [Order].CustomerId = Customer.Id  
    WHERE [Order].OrderDate <= '2012-07-10' 
    """ 
    result = cursor.execute(query).fetchall()
    connection.close()
    return result



#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    pass


if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''

    #result = question9()
    #print_query_result(result)

#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    pass

