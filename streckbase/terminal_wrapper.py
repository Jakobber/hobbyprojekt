import connect 
import compute 
import automail 
import fetch 
from html_templates import skuldmail

def start() -> int:
    print(  r"   _____ __                 __   __                       __              __    ")
    print(  r"  / ___// /_________  _____/ /__/ /_  ____ _________     / /_____  ____  / /____")
    print(  r"  \__ \/ __/ ___/ _ \/ ___/ //_/ __ \/ __ `/ ___/ _ \   / __/ __ \/ __ \/ / ___/")
    print(  r" ___/ / /_/ /  /  __/ /__/ ,< / /_/ / /_/ (__  )  __/  / /_/ /_/ / /_/ / (__  ) ")
    print(  r"/____/\__/_/   \___/\___/_/|_/_.___/\__,_/____/\___/   \__/\____/\____/_/____/  ")
    print(  r"                                                                                ")
    print('1. Automail över specifik skuld \n2. Hur mår streckbase?')
    return int(input(""))

def automail():
    _, eng = connect.connect_remote_db()
    df = fetch.get_table_as_pandas(eng, 'Users')
    limit = int(input("Vilken skuldgräns vill du automaila alla över?\n"))
    bad_people = compute.get_debt_over_limit(df, limit)

    while True:
        fetch.print_names_from_table(bad_people)
        print(f"Dessa personer är totalt skyldiga {bad_people['debt'].sum()}kr")
        if str(input("Vill du ta bort någon person? y/n\n")).lower() == 'y':
            print('Det va generöst')
            bad_people = fetch.remove_names_from_table(bad_people)
        else: break
    
    tel = str(input('Vilket nummer ska skulden swishas till?\n'))
    tel_namn = str(input('Namn till detta nummer?\n'))
    
    if str(input(f"Vill du att ett mail ska skickas till \n{list(bad_people['email'])}\ninnehållande telefonummer och namn: \n{tel}\n{tel_namn}\ny/n\n")).lower() == 'y':
        automail.send_mass_email(bad_people['email'], skuldmail.skuld_subject, skuldmail.skuld_body, zip(bad_people['firstname'], bad_people['debt']), (tel, tel_namn))
    
    else: print('fegis')

def check_balance():
    _, eng = connect.connect_remote_db()
    df = fetch.get_table_as_pandas(eng, 'Users')
    pos, neg, all = compute.get_total_debt(df)
    print(f'Folk är skyldiga Streckbase {pos}kr\nStreckbase är skyldiga folk {neg}kr\nTotalt har streckbase därav {all}kr skyldig till sig.')
    

def get_full_transaction():
    pass