:tocdepth: 3

Fake email 
//////////

.. toctree::
   :maxdepth: 2

   


Purpose of the project
======================

It is a temporary email app to receive all messages, it automatically deletes the email 10 minutes after it is created

Installing
==========
single file::

    pip install fake-email 

get email
=========
single file::

    from fake_email import Email 

    mail=Email().Mail()
    print(mail)
response
========
single file::

    {'mail': 'mcb06928@cdfaq.com', 'session': 'lmtl7ui7lu7halsn1l7wdvba5g'}	
fetch messages
==============
single file::

    from fake_email import Email 
    while True:
    mass=Email(session).inbox()
    if mass:
     print(mass)
     break
response
========
single file::

    {'topic': 'Hi', 'name': 'روكس \\ RUKS', 'from': '**@gmail.com', 'to': 'knz83195@xcoxc.com', 'message': "Hi bro ,I'm muntazir", 'datetime': ['datetime']}

Example
=======
single file::

    from fake_email import Email 
    mail=Email().Mail()
    print(mail)
    while True:
      mass=Email(mail["session"]).inbox()
      if mass:
	print(mass)
	break

Indices and tables
//////////////////

* :ref:`genindex`
* :ref:`search`


.. _modernize: https://t.me/DIBIBl
.. _project website: https://t.me/DIBIBl
