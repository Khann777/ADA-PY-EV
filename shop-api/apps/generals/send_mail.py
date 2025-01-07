from django.core.mail import send_mail

def send_activation_email(email, code):
    activation_url = f'http://localhost:8000/api/account/activate/?u={code}'

    send_mail(
        'Hello, activate your account',
        'To activate your account, go to this link:'
        f'\n{activation_url}',
        'nurdinov.d777@gmail.com',
        [email],
        fail_silently=False,
    )