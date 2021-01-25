import sqlite3
from sqlite3 import Error
import itertools

def initialize(database):
    print("Initializing database")

    try:
        conn = sqlite3.connect(database)
        print("Database connected")
        return conn
    except Error:
        print(Error)
        return 0

def endProgram(conn):
    try:
        conn.close()
        print("Ended program")
    except Error:
        print(Error)

def getMode():
    while True:
        option = input(
            "______ _____  ______          _    ______       _ _     _                             _  ______                                                  _           \n"
            "| ___ /  __ \ | ___ \        | |   | ___ \     (_| |   | |                           | | | ___ \                                                | |          \n"
            "| |_/ | /  \/ | |_/ __ _ _ __| |_  | |_/ /_   _ _| | __| | ___ _ __    __ _ _ __   __| | | |_/ /___  ___ ___  _ __ ___  _ __ ___   ___ _ __   __| | ___ _ __ \n"
            "|  __/| |     |  __/ _` | '__| __| | ___ | | | | | |/ _` |/ _ | '__|  / _` | '_ \ / _` | |    // _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _ | '_ \ / _` |/ _ | '__|\n"
            "| |   | \__/\ | | | (_| | |  | |_  | |_/ | |_| | | | (_| |  __| |    | (_| | | | | (_| | | |\ |  __| (_| (_) | | | | | | | | | | |  __| | | | (_| |  __| |   \n"
            "\_|    \____/ \_|  \__,_|_|   \__| \____/ \__,_|_|_|\__,_|\___|_|     \__,_|_| |_|\__,_| \_| \_\___|\___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__,_|\___|_|   \n"
            "\n"
            "\n"
            "                             _______ \n"
            "                            | ___  o|\n"
            "                            |[_-_]_ |\n"
            "         ______________     |[_____]|\n"
            "        |.------------.|    |[_____]|\n"
            "        ||            ||    |[====o]|\n"
            "        ||            ||    |[_.--_]|\n"
            "        ||            ||    |[_____]|\n"
            "        ||            ||    |      :|\n"
            "        ||____________||    |      :|\n"
            "    .==.|!!  ......    |.==.|      :|\n"
            "    |::| !-.________.-! |::||      :|\n"
            "    |**|  (__________)-.|**||______:|\n"
            "    *==*_.............._*==*______   \n"
            "       /:::::::::::--:::\*;*-.-.  *\ \n"
            "      /::=========.:.-:::\ \ \--\   \ \n"
            "      \ ^^^^^^^^^^^^^^^^ /  \ \__)   \ \n"
            "        ^^^^^^^^^^^^^^^^     *========* \n"
            "\n"
            "\n"
            "Choose the following options:\n"
            "1: Manual (You Pick)\n"
            "2: Recommendations (Program Picks)\n"
            "Input: ")
        try:
            return int(option)
        except ValueError:
            print("Not an option. Choose again.")

def searchParts(listParts):
    yes = ["YES", "Yes", "yes", "Y", "y"]
    no = ["NO", "No", "no", "N", "n"]
    pickable = []

    while True:
        option = input("Would you like to narrow your search? (Yes/No)\n"
                       "Input: ")
        if option in yes:
            while True:
                print("Search is case sensitive!")
                toSearch = input("Search: ")
                print("Name:")
                for i in listParts:
                    if toSearch in i:
                        print(i)
                        pickable.append(i)
                if len(pickable) == 0:
                    print("Not an option. Choose again.")
                elif len(pickable) != 0:
                    return pickable
        elif option in no:
            print("All Parts:")
            for i in listParts:
                print(i)
                pickable.append(i)
            return pickable
        else:
            print("Not an option. Choose again.")

def getCPUPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select cpu_price from cpu where cpu_name = ?''', (select,))
                price = c.fetchone()
                return price[0], select
        print("Not an option. Choose again.")

def getGPUPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select gpu_price from gpu where gpu_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def getMOBOPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select mobo_price from mobo where mobo_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def getCOOLPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select cool_price from cool where cool_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def getMEMPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select mem_price from mem where mem_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def getCASEPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select pccase_price from pccase where pccase_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def getSTORPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select stor_price from stor where stor_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def getPSUPrice(conn, pickable):
    c = conn.cursor()
    while True:
        select = input("Select: ")
        for i in pickable:
            if select in i:
                c.execute(
                    '''select psu_price from psu where psu_name = ?''', (select,))
                price = c.fetchone()
                print(price[0])
                return price[0], select
        print("Not an option. Choose again.")

def manualMode(conn):
    c = conn.cursor()

    print("Choose your CPU:")
    c.execute("""select cpu_name from cpu""")
    listCPU = c.fetchall()
    listCPU = list(itertools.chain(*listCPU))
    pickable = searchParts(listCPU)
    cpupart = getCPUPrice(conn, pickable)
    totalPrice = cpupart[0]
    print("Current total: " + str(totalPrice))

    print("Choose your GPU:")
    c.execute("""select gpu_name from gpu""")
    listGPU = c.fetchall()
    listGPU = list(itertools.chain(*listGPU))
    pickable = searchParts(listGPU)
    gpupart = getGPUPrice(conn, pickable)
    totalPrice = totalPrice + gpupart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Choose your Motherboard:")
    c.execute("""select mobo_name from mobo""")
    listMOBO = c.fetchall()
    listMOBO = list(itertools.chain(*listMOBO))
    pickable = searchParts(listMOBO)
    mobopart = getMOBOPrice(conn, pickable)
    totalPrice = totalPrice + mobopart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Choose your CPU Cooler:")
    c.execute("""select cool_name from cool""")
    listCOOL = c.fetchall()
    listCOOL = list(itertools.chain(*listCOOL))
    pickable = searchParts(listCOOL)
    coolpart = getCOOLPrice(conn, pickable)
    totalPrice = totalPrice + coolpart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Choose your Memory:")
    c.execute("""select mem_name from mem""")
    listMEM = c.fetchall()
    listMEM = list(itertools.chain(*listMEM))
    pickable = searchParts(listMEM)
    mempart = getMEMPrice(conn, pickable)
    totalPrice = totalPrice + mempart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Choose your Case:")
    c.execute("""select pccase_name from pccase""")
    listCASE = c.fetchall()
    listCASE = list(itertools.chain(*listCASE))
    pickable = searchParts(listCASE)
    casepart = getCASEPrice(conn, pickable)
    totalPrice = totalPrice + casepart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Choose your Storage:")
    c.execute("""select stor_name from stor""")
    listSTOR = c.fetchall()
    listSTOR = list(itertools.chain(*listSTOR))
    pickable = searchParts(listSTOR)
    storpart = getSTORPrice(conn, pickable)
    totalPrice = totalPrice + storpart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Choose your PSU:")
    c.execute("""select psu_name from psu""")
    listPSU = c.fetchall()
    listPSU = list(itertools.chain(*listPSU))
    pickable = searchParts(listPSU)
    psupart = getPSUPrice(conn, pickable)
    totalPrice = totalPrice + psupart[0]
    totalPrice = round(totalPrice, 2)
    print("Current total: " + str(totalPrice))

    print("Selected Parts:\n"
          + cpupart[1] + "\n"
          + gpupart[1] + "\n"
          + mobopart[1] + "\n"
          + coolpart[1] + "\n"
          + mempart[1] + "\n"
          + casepart[1] + "\n"
          + storpart[1] + "\n"
          + psupart[1])

def chooseSocket(conn):
    c = conn.cursor()
    c.execute('''select cpu_socket from cpu''')
    socketCheck = c.fetchall()
    while True:
        socket = input("Current Socket Types: AM4, LGA 1200\n"
                       "Choose one: ")
        for i in socketCheck:
            if socket in i:
                return socket
        print("Incorrect Socket Type.\n"
              "Please try again.")

def chooseGPU(conn):
    c = conn.cursor()
    c.execute('''select gpu_price from gpu''')
    gpuCheck = c.fetchall()
    gpuCheck = list(itertools.chain(*gpuCheck))
    c.execute('''select MAX(gpu_price) from gpu''')
    failsafeMAX = c.fetchall()
    failsafeMAX = list(itertools.chain(*failsafeMAX))
    failsafeMAX = float(failsafeMAX[0])
    # print(failsafeMAX)
    c.execute('''select MIN(gpu_price) from gpu''')
    failsafeMIN = c.fetchall()
    failsafeMIN = list(itertools.chain(*failsafeMIN))
    failsafeMIN = float(failsafeMIN[0])
    # print(failsafeMIN)
    while True:
        gpuBudget = input("How much for GPU: ")
        gpuBudget = float(gpuBudget)
        for i in gpuCheck:
            if i <= gpuBudget and failsafeMAX >= gpuBudget >= failsafeMIN:
                return gpuBudget
        print("No available GPU at that price range.\n"
              "Please try again.")

def chooseMEM(conn):
    c = conn.cursor()
    c.execute('''select mem_capacity from mem''')
    memCheck = c.fetchall()
    memCheck = list(itertools.chain(*memCheck))
    c.execute('''select MAX(mem_capacity) from mem''')
    failsafeMAX = c.fetchall()
    failsafeMAX = list(itertools.chain(*failsafeMAX))
    failsafeMAX = float(failsafeMAX[0])
    # print(failsafeMAX)
    c.execute('''select MIN(mem_capacity) from mem''')
    failsafeMIN = c.fetchall()
    failsafeMIN = list(itertools.chain(*failsafeMIN))
    failsafeMIN = float(failsafeMIN[0])
    # print(failsafeMIN)
    while True:
        memCap = input("How much memory: ")
        memCap = int(memCap)
        for i in memCheck:
            if memCap >= i and failsafeMAX >= memCap >= failsafeMIN:
                return memCap
        print("No memory available in that capacity.\n"
              "Please try again.")

def chooseCOOL(conn):
    c = conn.cursor()
    c.execute('''select cool_type from cool''')
    coolCheck = c.fetchall()
    while True:
        coolType = input("Type of Cooling: AIO, AIR\n"
                         "Choose one: ")
        for i in coolCheck:
            if coolType in i:
                return coolType
        print("No cooler available for that type.\n"
              "Please try again.")

def chooseFF(conn):
    c = conn.cursor()
    c.execute('''select mobo_formfactor from mobo''')
    FFCheck = c.fetchall()
    while True:
        caseFF = input("Case Formfactor: ATX, ITX, EATX, MATX\n"
                       "Choose one: ")
        for i in FFCheck:
            if caseFF in i:
                return caseFF
        print("No formfactor of that type available.\n"
              "Please try again.")

def recMode(conn):
    c = conn.cursor()
    budget = input("Input Budget: ")
    limit = input("Amount of Builds: ")
    socket = chooseSocket(conn)
    # print(socket)
    gpuBudget = int(chooseGPU(conn))
    # print(gpuBudget)
    memCap = chooseMEM(conn)
    # print(memCap)
    coolType = chooseCOOL(conn)
    # print(coolType)
    caseFF = chooseFF(conn)
    # print(caseFF)
    c.execute('''SELECT DISTINCT cpu, gpu, motherboard, cooler, mem, pccase, stor, psu, price
    FROM (SELECT DISTINCT mobo_name as motherboard
    , cpu_name as cpu 
    , gpu_name as gpu
    , mem_name as mem
    , mem_capacity as memcap
    , cool_name as cooler
    , psu_name as psu
    , psu_power as psupower
    , pccase_name as pccase
    , stor_name as stor
    , ROUND(SUM(mobo_price + cpu_price + gpu_price + mem_price + cool_price + psu_price + pccase_price + stor_price), -1) as price
    FROM mobo, cpu, gpu, mem, cool, psu, pccase, stor 
    WHERE mobo_socket = ?
    AND cpu_socket = mobo_socket
    AND gpu_price <= ?
    AND mem_capacity <= ?
    AND cool_type = ?
    AND pccase_formfactor = ?
    and mobo_formfactor = pccase_formfactor
    GROUP BY motherboard, cpu, gpu, mem, memcap, cooler, psu, psupower, pccase, stor
    HAVING price < ?) 
    ORDER BY price DESC    
    limit ?''', (socket, gpuBudget, memCap, coolType, caseFF, budget, limit))
    builds = c.fetchall()
    # print(builds)
    print("Recommended Builds: \n{:22s}{:23s}{:30s}{:27s}{:32s}{:31s}{:28s}{:17s}{:7s}".format("CPU", "GPU",
                                                                                               "Motherboard", "Cooler",
                                                                                               "Memory", "Case",
                                                                                               "Storage", "PSU",
                                                                                               "Price"))
    for i in builds:
        print("{:22s}{:23s}{:30s}{:27s}{:32s}{:31s}{:28s}{:17s}{:7s}".format(str(i[0]), str(i[1]), str(i[2]),
                                                                             str(i[3]), str(
            i[4]), str(i[5]),
            str(i[6]), str(i[7]), str(i[8])))

def main():
    database = r"pcparts.db"
    conn = initialize(database)
    while True:
        option = getMode()
        # print(option)
        if option == 1:
            print("Manual Mode Chosen")
            manualMode(conn)
            return False
        elif option == 2:
            print("Recommendations Chosen")
            recMode(conn)
            return False
        else:
            print("Not an option. Choose again.")
    endProgram(conn)
main()
