import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
from db.CreateZoom import CreateZoom
from datetime import datetime, timezone, timedelta
import pytz

sender_email = "sunprairiewestjobsearch@gmail.com"
password = "dfdc kmjz qxuo sgmp"
smtp_server = "smtp.gmail.com"
smtp_port = 587

class CreateEmail:

    def sendStudentEmail(self, studentFirstName, studentEmail, jobTitle, interviewDate, interviewTime, additionalComments):
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = studentEmail
        message["Subject"] = "Request For Interview!"

        datetime_str = f"{interviewDate} {interviewTime}"
        naive_dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        
        # Define your local timezone (e.g., 'America/Chicago' for CDT)
        local_timezone = pytz.timezone('America/Chicago') 
                
        # Localize the naive datetime object
        local_aware_dt = local_timezone.localize(naive_dt)
                
        # Convert to UTC
        utc_dt = local_aware_dt.astimezone(timezone.utc)

        iso_format_startTime_string = utc_dt.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        
        createZoom = CreateZoom()
        zoom_link = createZoom.create_zoom_meeting(jobTitle, iso_format_startTime_string)

        body = "Hello " + studentFirstName + "!<br><br>You have been invited to interview for the following position:<br><br><B>" + jobTitle + "</B><br><br>The employer has set the following date and time for the interview:<br><br><B>Date: " + interviewDate + "<br>Time: " + interviewTime + "</B>"
        body += "<br><br>Here are additional comments the employer had: <br><br><B>'" + additionalComments + "'"
        body += "<br><br>Here is the Zoom Link for you to use:<br><br></B>" + zoom_link['start_url']
        body += "<br><br>If this time does not work for you, please contact the employer.<br><br>Congratulations! Best of luck!<br><br><br><B>~ The Sun Prairie West Job Search Team</B>"
        
        message.attach(MIMEText(body, "html"))

        try:
            # For TLS (port 587)
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            # For SSL (port 465)
            # server = smtplib.SMTP_SSL(smtp_server, smtp_port)

            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, studentEmail, text)
            
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()


#createemail = CreateEmail()
#createemail.sendStudentEmail("Sanjay", 'sanjayjagadeesh2021@gmail.com', "CEO", "2025-08-15", "12:20")