from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_page(self):
        
        self.driver.get("file:///C:/Users/talpo/Downloads/HTML/QA_Task.html")
        time.sleep(5)

        
        full_name_input = self.driver.find_element(By.ID, "candidateName")
        full_name_input.send_keys("Talpos Bogdan")

        
        email_input = self.driver.find_element(By.ID, "candidateMail")
        email_input.send_keys("talposbogdan20@gmail.com")  

        start_button = self.driver.find_element(By.ID, "startButton")
        start_button.click()

        
        emailuri_valide = ["test@example.com", "user123@gmail.com", "john.doe@domain.com"]
        emailuri_invalide = ["test@example", "user123gmail.com", "john.doe@domain"]

        
        parole_valide = ["TestPassword123", "SecurePwd@123", "StrongPwd!567"]
        parole_invalide = ["password", "12345678", "abc123"]

        
        test_results = []

        
        for email_valid in emailuri_valide:
            try:
                
                email_input = self.driver.find_element(By.ID, "email")
                email_input.clear()  
                email_input.send_keys(email_valid)

                
                time.sleep(5)

                
                for password_valid in parole_valide:
                    try:
                        
                        password_input = self.driver.find_element(By.ID, "password")
                        password_input.clear()  
                        password_input.send_keys(password_valid)

                        
                        login_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
                        login_button.click()

                        
                        time.sleep(5)

                       
                        error_message_email = self.driver.find_element(By.ID, "errorMsgMail")
                        error_message_password = self.driver.find_element(By.ID, "errorMsgPwd")
                        
                        
                        color_email = self.convert_color_to_name(error_message_email.value_of_css_property("color"))
                        color_password = self.convert_color_to_name(error_message_password.value_of_css_property("color"))

                        
                        test_results.append((email_valid, password_valid, self.get_error_message(error_message_email.text), self.get_error_message(error_message_password.text), color_email, color_password))
                    except Exception as e:
                        print("Error occurred:", e)
                        continue
            except Exception as e:
                print("Error occurred:", e)
                continue

            
            time.sleep(3)

        
        for email_invalid in emailuri_invalide:
            try:
                
                email_input = self.driver.find_element(By.ID, "email")
                email_input.clear()  
                email_input.send_keys(email_invalid)

                
                time.sleep(5)

                
                for password_invalid in parole_invalide:
                    try:
                        
                        password_input = self.driver.find_element(By.ID, "password")
                        password_input.clear()  
                        password_input.send_keys(password_invalid)

                        
                        login_button = self.driver.find_element(By.XPATH, "//input[@value='Login']")
                        login_button.click()

                        
                        time.sleep(5)

                        
                        error_message_email = self.driver.find_element(By.ID, "errorMsgMail")
                        error_message_password = self.driver.find_element(By.ID, "errorMsgPwd")
                        
                        
                        color_email = self.convert_color_to_name(error_message_email.value_of_css_property("color"))
                        color_password = self.convert_color_to_name(error_message_password.value_of_css_property("color"))

                        
                        test_results.append((email_invalid, password_invalid, self.get_error_message(error_message_email.text), self.get_error_message(error_message_password.text), color_email, color_password))
                    except Exception as e:
                        print("Error occurred:", e)
                        continue
            except Exception as e:
                print("Error occurred:", e)
                continue

            
            time.sleep(3)

        
        with open("test_results.html", "w") as f:
            f.write("<html><body>")
            f.write("<h1>Test Results</h1>")
            f.write("<table border='1'>")
            f.write("<tr><th>Email</th><th>Password</th><th>Error Message (Email)</th><th>Error Message (Password)</th><th>Email Color</th><th>Password Color</th></tr>")
            for result in test_results:
                f.write(f"<tr><td>{result[0]}</td><td>{result[1]}</td><td>{result[2]}</td><td>{result[3]}</td><td>{result[4]}</td><td>{result[5]}</td></tr>")
            f.write("</table>")
            f.write("</body></html>")

    def tearDown(self):
       
        self.driver.quit()

    def convert_color_to_name(self, color):
        
        color_mapping = {
            "rgba(255, 0, 0, 1)": "Red",
            "rgba(0, 128, 0, 1)": "Green",
            
        }
        return color_mapping.get(color, "Unknown")

    def get_error_message(self, error_message):
        
        if "Invalid email" in error_message:
            return "Invalid Email"
        elif "Invalid Password" in error_message:
            return "Invalid Password"
        elif "Valid password" in error_message:
            return "Valid Password"
        elif "Valid email" in error_message:
            return "Valid Email"
        else:
            return error_message

if __name__ == "__main__":
    unittest.main()
