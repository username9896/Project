from ifttt_webhook import IftttWebhook

# IFTTT Webhook key, available under "Documentation"
# at  https://ifttt.com/maker_webhooks/.
IFTTT_KEY = 'b-F4U7NhssgKf42FkeqKxdSLYC5zTdTa31AS46cxJ8D'

# Create an instance of the IftttWebhook class,
# passing the IFTTT Webhook key as parameter.
ifttt = IftttWebhook(IFTTT_KEY)

# Trigger the IFTTT event defined by event_name with the content
# defined by the value1, value2 and value3 parameters.
ifttt.trigger('senddata', value1='value1', value2='value2', value3='value3')


event_values = ('vickykumar3611@gmail.com', '1', '2')
# Unpack the tuple / list in the method call
ifttt.trigger('senddata', *event_values)

ifttt.gmail(to='vickykumar3611@gmail.com', subject='This is the subject', body='This is the email body.')




pip install git+https://github.com/DrGFreeman/IFTTT-Webhook.git
