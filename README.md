<h1 align="center">fake-email</h1>
<p align="center">A simple library project, a library function to make a temporary email, receive all messages</p>


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

```json
{
	'topic': 'Hi', 
	'name': 'روكس \\ RUKS', 
	'from': '**@gmail.com', 
	'to': 'knz83195@xcoxc.com', 
	'message': "Hi bro ,I'm muntazir", 
        'datetime': ['datetime']
}
```
</p>
<p align="center">
  <img alt="muntazir-halim' Github Stats" src="https://github-readme-stats.vercel.app/api?username=muntazir-halim&show_icons=true&include_all_commits=true&hide_border=true" />
 <img src="https://github-readme-stats.anuraghazra1.vercel.app/api/top-langs/?username=muntazir-halim&hide=ruby,perl&hide_border=true" /> 
</p>


