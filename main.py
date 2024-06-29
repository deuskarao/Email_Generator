import json
import random
import argparse


class Main:
    def __init__(self,
                 MAIL_MASS = 0,

                 names_list:list = [],
                 surname_list:list = [],
                 ext_list:list = [],
                 ) -> None:
        
        self.MAIL_MASS = MAIL_MASS

        self.names_list = names_list
        self.surname_list = surname_list
        self.ext_list = ext_list
    
    def get_parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-mass', dest='mail_mass', type=int, default=100, help='How many mails?')
        argpass = parser.parse_args()

        self.MAIL_MASS = argpass.mail_mass
        
    def get_json_out(self):
        with open ("data.json", "r") as f:
            data = json.load(f)
            
            self.names_list = data["names"]
            self.surname_list = data["surnames"]
            self.ext_list = data["extens"]
        
        '''
            print(f"""
                    Names:
                    {self.names_list}

                    Surnames:
                    {self.surname_list}

                    Extensions:
                    {self.ext_list}
              """)
        '''
        
    def out_write(self, get_list):
        with open("emails.txt", "a") as writer:
            writer.writelines(f"{get_list}\n")
            
    def create_v_loop(self):
        for i in range(self.MAIL_MASS):
            out_string = ""

            w = random.choice(self.names_list)
            ww = random.choice(self.surname_list)
            www = random.choice(self.ext_list)

            out_string = f"{w}{ww}{www}"

            self.out_write(out_string)
        self.out_write(f"\nTOTAL: {self.MAIL_MASS}")
        

starter = Main()
starter.get_parse()
starter.get_json_out()
starter.create_v_loop()
