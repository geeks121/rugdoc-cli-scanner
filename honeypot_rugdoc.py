import requests
import json
import os

def top():
    os.system('python honeypot_rugdoc.py')

# Honeypot API details
honeypot_url = 'https://honeypot.api.rugdoc.io/api/honeypotStatus.js?address='

# color style
class style():  # Class of different text colours - default is white
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

## message box

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)


# ---------------------

msg = "# Honeypot Rugdoc scanner # \n" \
"1. BSC \n" \
"2. Polygon \n" \
"3. Avalanche \n" \
"#------------------------# \n" \
"Not guarantee 100 at least you know what you do"

print_msg_box(msg=msg, indent=2, title='Honeypot RUG Scanner')

# selecting chain
choose = input("Please Select the menu :  ")

#if int(choose) == 1:
#    chain = '&chain=eth'
if int(choose) == 1:
    print(style.YELLOW)
    chain = '&chain=bsc'
elif int(choose) == 2:
    print(style.MAGENTA)
    chain = '&chain=poly'
elif int(choose) == 3:
    print(style.BLUE)
    chain = '&chain=avax'
else:
    print("---------------------------------")
    print(style.CYAN + "ERROR! please select correct menu")
    print("---------------------------------")
    top()

interpretations = {
  "UNKNOWN": (style.RED + 'The status of this token is unknown. '
                          'This is usually a system error but could \n also be a bad sign for the token. Be careful.'),
  "OK": (style.GREEN + ' √ Honeypot tests passed. Our program was able to buy and sell it successfully. \n'
                       'This however does not guarantee that it is not a honeypot.'),
  "NO_PAIRS": (style.RED + '⚠ Could not find any trading pair for this token '
                           'on the default router and could thus not test it.'),
  "SEVERE_FEE": (style.RED + '⚠ A severely high trading fee (over 50%) was '
                             'detected when selling or buying this token.'),
  "HIGH_FEE": (style.YELLOW + '⚠ A high trading fee (Between 20% and 50%) was detected when '
                              'selling or buying this token. Our system was\n however able to sell the token again.'),
  "MEDIUM_FEE": (style.YELLOW + '⚠ A trading fee of over 10% but less then 20%\n was detected when selling '
                                'or buying this token. Our system was however able\n to sell the token again.'),
  "APPROVE_FAILED": (style.RED + '🚨 Failed to approve the token.\n This is very likely a honeypot.'),
  "SWAP_FAILED": (style.RED + '🚨 Failed to sell the token. \n This is very likely a honeypot.')
}

token_address = input("Contract Address :  ")

def honeypot_check(address):
    url = (honeypot_url + address + chain)
    # sending get request and saving the response as response object
    return requests.get(url)
	
	
honeypot = honeypot_check(address=token_address)
d = json.loads(honeypot.content)
for key, value in interpretations.items():
	if d["status"] in key:
		honeypot_status = value
		honeypot_code = key
		print(honeypot_status)

top()
