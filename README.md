<h1 align="center">fake-email</h1>
<p align="center">A simple library project, a library function to make a temporary email, receive all messages</p>

[![PyPI version](https://img.shields.io/pypi/v/fake-email.svg)](https://pypi.org/project/fake-email)
[![YouTube](https://img.shields.io/static/v1?label=subscribe&logo=youtube&logoColor=ff0000&color=brightgreen&message=4.2k)](https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA)
[![Discord](https://img.shields.io/discord/566880874789076992?logo=telegram)](https://t.me/TBIBB)
[![YouTube](https://img.shields.io/readthedocs/modernize?logo=read-the-docs)](https://fake-email.readthedocs.io/en/latest/)
[![Downloads](https://pepy.tech/badge/fake-email)](https://pepy.tech/project/fake-email)










## Installation :
```
pip install fake-email
```
### Example
```python
from fake_email import Email


mail=Email().Mail()
print(mail)



while True:
	mass=Email(mail["session"]).inbox()
	if mass:
		print(mass)
		break
	
```
### The result

```cs 
 {     
    'topic': 'Hi', 
    'name': 'روكس \\ RUKS', 
    'from': '**@gmail.com', 
    'to': 'knz83195@xcoxc.com', 
    'message': "Hi bro ,I'm muntazir",  
    'datetime': ['datetime']
}
```

### You can enter the private inbox in the fake email through the session
```python 
{
 'mail': 'rjx14056@cdfaq.com',
 'session': 'eywvgnjdwf53ex7z9rq8lxunf9'
}
```
### Example get inbox

```python 
from fake_email import Email

# get inbox

while True:
	mass=Email(session).inbox()
	if mass:
		print(mass)
		break
```

</p>
<p align="center">
  <img alt="muntazir-halim' Github Stats" src="https://github-readme-stats.vercel.app/api?username=muntazir-halim&show_icons=true&include_all_commits=true&hide_border=true" />
 <img src="https://github-readme-stats.anuraghazra1.vercel.app/api/top-langs/?username=muntazir-halim&hide=ruby,perl&hide_border=true" /> 
</p>


