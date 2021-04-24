from datetime import datetime
with open(datetime.now().strftime("%d-%m-%Y"),"w")as file:
    file.write("I automated this using python!")