from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Mailer:
    def otp_confirmation(self, user):
        message = 'Please confirm transfer to {}'.format(user)
        subject = 'topsport otp confirmation'

        mail_subject = subject
        to_mail = ['topsporttechnologies@gmail.com']
        from_mail = 'Topsport <noreply@topsport.com.ng>'
        mail.send_mail(mail_subject, message, from_mail, to_mail)

    def send_bd_msg(self, username, email):
        message = render_to_string('mails/birthday_msg.html', {'username':username})
        subject = 'Happy Birthday From Topsport'
        print('i reach here')
        mail_subject = subject
        raw_message = strip_tags(message)
        to_email = email
        from_email = 'Topsport <noreply@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)
        print('mail sent successfully')
    def notify_balance(self, amount, username):
        amount = amount/100
        message = render_to_string('mails/admin/insufficient_fund_alert.html', {'amount': amount, 'username': username})
        subject = 'Topsport Insufficient funds'

        mail_subject = subject
        to_email = 'njoagwuanidavid@gmail.com'
        raw_message = strip_tags(message)
        from_email = 'Topplaysport <noreply@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_first_time_mail(self, email, username):
        message = render_to_string('mails/auth/register_success.html', {'username': username})
        subject = 'David from Topsport Checking in'

        mail_subject = subject
        to_email = email
        raw_message = strip_tags(message)
        from_email = 'Topsport <noreply@topsport.com.ng>'
        print('i got here')
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)
        print('here too')

    def send_winning_msg(self, user):
        message = render_to_string('mails/bets/win.html')
        subject = 'YOU ARE A WINNER'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = user.email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_my_mail(self, amount):
        message = render_to_string('mails/bets/test.html', {'amount':amount})
        subject = 'TESTING AMOUNT DISBURSED'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = 'njoagwuanidavid@gmail.com'
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_referrer_msg(self, user, username):
        message = render_to_string('mails/referrals/referee.html', {'username': username})
        subject = 'New Referral Notification'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = user.email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_referrer_winner(self, user, username):
        message = render_to_string('mails/referrals/referral_paid.html', {'username': username})
        subject = 'Referral Notification'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = user.email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_raffle_player(self, user, raffle_id):
        message = render_to_string('mails/raffle/qualification.html', {'username': user.username, 'raffle_id': raffle_id})
        subject = 'Raffle Draw Added'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = user.email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_raffle_winner(self, user):
        message = render_to_string('mails/raffle/won.html', {'username': user.username})
        subject = 'You Are A Winner'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = user.email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def send_support_message(self, username):
        message = render_to_string('mails/support.html', {'username': username})
        subject = 'New message from users'

        mail_subject = 'Topsport - {}'.format(subject)
        to_email = 'info@topsport.com.ng'
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def admin_response(self, message, email, name):
        message = render_to_string('mails/admin/support_response.html', {
            'message': message, 'name': name
        })

        mail_subject = 'Topsport - Support Response'
        to_email = email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)

    def admin_message(self, message, email, title):
        message = render_to_string('mails/admin/custom_mail.html', {
            'message': message
        })

        mail_subject = f'Topsport - {title}'
        to_email = email
        raw_message = strip_tags(message)
        from_email = 'Topsport <info@topsport.com.ng>'
        mail.send_mail(mail_subject, raw_message, from_email, [to_email], html_message=message)
