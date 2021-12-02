import pandas
import smtplib

data_path = "data.csv"
data = pandas.read_csv(data_path)

def send_mail(message,receiver):
        try:
            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)
            
            # start TLS for security
            s.starttls()
            
            # Authentication
            s.login("actemp22@gmail.com", "atempaccount99")
            
            # sending the mail
            s.sendmail("actemp22@gmail.com", receiver, message)
            
            print(f"[+] Successfully sent email to {receiver}")

            # terminating the session
            s.quit()
        except:
            return f"[-] Error sending email"

def check_voter_id(data):
    index = 0
    email_null_id = []

    print(f"Following people doesnt have their voter id:\n")

    while True:
        try:
            age = data.iloc[index]['age']
            has_id = data.iloc[index]['has_voterid']
            email = data.iloc[index]['email']

            if age > 18 and has_id == 0:
                email_null_id.append((email))
                print(f"{age},{has_id},{email}")

            index = index + 1
        except:
            break

    return email_null_id
            


if __name__ == "__main__":
    emails = check_voter_id(data)

    for email in emails:
        send_mail("You havent generated your voter id, please do soon.",email)
